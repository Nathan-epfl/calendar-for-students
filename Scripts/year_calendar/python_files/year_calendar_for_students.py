#%%
#%%

import copy
from year_calendar.python_files.IB_subject_class import *
from year_calendar.python_files.extract_subj_from_dict import extract_subj_from_dict
from year_calendar.python_files.change_coeffs_of_subjects import change_coeffs_of_subjects
from year_calendar.python_files.transform_coeff_to_hours import transform_coeff_to_hours
from year_calendar.python_files.redistribute_hours_of_subj_each_day_of_year import redistribute_hours_each_day_of_year
from year_calendar.python_files.secondary_func_of_year_cal_for_students import *
from year_calendar.python_files.year_excel_calendar_for_students import year_excel_calendar_for_students

def year_calendar_for_students(
    subjects_and_options = dict,
    subjects_and_coefficients = dict,
    total_hours_per_week = int,
    ###########part year_excel_cal
    calendar_from_student = pd.core.frame.DataFrame,
    final_calendar_name = str,
    order=[[1,2,3],[2,3,1]],
    delete_original_calendar = False, #if true, then the schedule of "calendar_for_student" will be removed in the final calendar
    run_macro = True, #cannot be changed yet
    ###########
    date_of_start_of_calendar = datetime.datetime.now(), #when the calendar starts
    minimum_time_interval = 0.5 #cannot be changed yet
):
    '''
    main function of the project. It takes:

    the student's curriculum (subjects_and_options)
    The student's needs in each subject (subjects_and_coefficients)
    The amount of hours per week the student is willing to work
    The schedule of the student, following the template_calendar_xlsx format in folder xls_files (calendar_from_students)
    The final calendar output name
    An order of priorities (order), see week_calendar/python_files/set_priority.py for details

    some secondary arguments
    

    It creates:
    an xlsm workbook containing each week's schedule

    it returns a dictionary containing:
    the new student's curriculum with coefficients changed (dict_of_student_curriculum_coeff_changed)
    a dataframe subject/day containing hours of work (df_of_hours_per_day_redistributed)
    a list of dataframes subject/day splitted for each remaining week (list_of_df_of_days_splitted_each_week)
    a dataframe subject/day showing the coefficients change each day (df_of_coeff_per_day_exponential)
    '''
    
    ############### Filter out the folowwing warning####################
    #  warn(msg)
    #C:\Users\******\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\openpyxl\worksheet\_reader.py:312: UserWarning: Unknown extension is not supported and will be removed
    import warnings
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    ########################################################   
    
    #packages
    from os import chdir,path
    import re

    #setting main directory as Script directory
    file_directory= path.dirname(__file__)
    wd = re.findall(".+Scripts", file_directory)[0]
    chdir(wd)

    #copying the dictionaries
    subjects_and_options_coeff_zero_removed = copy.deepcopy(subjects_and_options)
    subjects_and_coefficients_zero_removed = copy.deepcopy(subjects_and_coefficients)

    #removing usbjects with coefficient zero
    for subj in subjects_and_coefficients.keys():

        if subjects_and_coefficients[subj] == 0:

            subjects_and_coefficients_zero_removed.pop(subj)
            subjects_and_options_coeff_zero_removed.pop(subj)


    date_of_start_of_calendar = pd.to_datetime(date_of_start_of_calendar)
    dict_of_student_curriculum = extract_subj_from_dict(
        subjects_and_options_coeff_zero_removed,
        IA = False
    )
    
    # setting weightings
    for subj in dict_of_student_curriculum.keys():
        dict_of_student_curriculum[subj].weight = subjects_and_coefficients_zero_removed[subj]

    dict_of_student_curriculum_coeff_changed = change_coeffs_of_subjects(
        dict_of_student_curriculum,
        subjects_and_coefficients_zero_removed
    )

    #useful when we will do a calendar for each topic
    # subj_with_hours_per_year_and_coeffs = compute.compute_hours_on_year(
    #     dict_of_student_curriculum_coeff_changed,
    #     total_hours_per_week,
    #     date_of_start_of_calendar,
    #     minimum_time_interval
    # )

    df_of_coeff_per_day_exponential = transform_coeff_to_hours(
        dict_of_student_curriculum_coeff_changed,
        total_hours_per_week,
        exp_coefficient_each_week_of_subjects,
        date_of_start_of_calendar,
        calendar_from_student
    )

    df_of_hours_per_day_redistributed = redistribute_hours_each_day_of_year(
        df_of_coeff_per_day_exponential,
        minimum_time_interval
    )


    #adding days to start on monday before creation of calendar (with 0 hours in each subj)
    if df_of_hours_per_day_redistributed.columns[0].weekday != 0:
        
        empty_column=[float(0) for x in range(len(df_of_hours_per_day_redistributed.index))]
        days_to_add_at_the_start = df_of_hours_per_day_redistributed.columns[0].weekday()
        
        for x in range(days_to_add_at_the_start):
            
            df_of_hours_per_day_redistributed.insert(0,date_of_start_of_calendar - datetime.timedelta(days = x + 1),empty_column)
    
    #adding days to start on sunday after end of exams (with 0 hours in each subj)
    if df_of_hours_per_day_redistributed.columns[-1].weekday != 6:
        
        empty_column=[float(0) for x in range(len(df_of_hours_per_day_redistributed.index))]
        days_to_add_at_the_end = 6 - df_of_hours_per_day_redistributed.columns[-1].weekday()
        date_of_end_of_calendar = df_of_hours_per_day_redistributed.columns[-1]
        
        for x in range(days_to_add_at_the_end):
            
            df_of_hours_per_day_redistributed.insert(len(df_of_hours_per_day_redistributed.columns),date_of_end_of_calendar + datetime.timedelta(days = x + 1),empty_column)
    
    
    #splitting df into multiple dfs for each week
    number_of_weeks = int(len(df_of_hours_per_day_redistributed.columns) / 7)
    list_of_df_of_days_splitted_each_week=[df_of_hours_per_day_redistributed.iloc[:,7 * x:7*(x + 1)] for x in range(number_of_weeks)]
    
    
    list_of_df_start_and_end_date_each_week=[
        str(list_of_df_of_days_splitted_each_week[x].columns[0].day)
        + '.'
        + str(list_of_df_of_days_splitted_each_week[x].columns[0].month)
        + '-'
        + str(list_of_df_of_days_splitted_each_week[x].columns[-1].day)
        + '.'
        + str(list_of_df_of_days_splitted_each_week[x].columns[-1].month) 
        for x in range(number_of_weeks)]
    # print(list_of_df_start_and_end_date_each_week)
    
    for df in list_of_df_of_days_splitted_each_week:
        
        df.columns=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        df.index=[dict_of_student_curriculum[x].name for x in df.index]


    year_excel_calendar_for_students(calendar_from_student,
                                list_of_df_of_days_splitted_each_week,
                                list_of_df_start_and_end_date_each_week,
                                final_calendar_name,
                                order,
                                delete_original_calendar, 
                                run_macro,
                                minimum_time_interval
                                )


    return {
        "curriculum" : dict_of_student_curriculum_coeff_changed,
        "df_hours_per_day" : df_of_hours_per_day_redistributed,
        "week_dfs" : list_of_df_of_days_splitted_each_week,
        "df_coeffs_per_day" : df_of_coeff_per_day_exponential,
    }

# %%
