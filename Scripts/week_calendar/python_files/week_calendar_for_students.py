#%% function that takes a calendar, a list,an integer, a list and a float and gives a calendar exported in excel

import pandas as pd
def week_calendar_for_students( calendar_from_student = pd.core.frame.DataFrame,
                                subj_with_coeffs = list,
                                hours_of_work = int,
                                final_calendar_name = str,
                                coeff_per_day = [1] * 7,
                                time_unit = 0.5,
                                order = [[1,2,3],[2,1,3]],
                                delete_original_calendar = False, 
                                run_macro = True
                                ):
    

    '''
    'calendar_from_student' is the name of the xlsx ('.xlsx' included) file containing the student's schedule
    'subj_with_coeff is a list of 2-lists containing name of subject and coefficient of the subject 
    'hours_of work' is the (approximate) amount of hours the students wants to work
    'coeff_per_day' is a 7-list with a coefficient for each day of the week, starting with monday
    'time_unit' is the interval of time in the calendar. It must correspond with 'calendar_from_student'!
    if True is given at the end, then the final calendar will have deleted the 'calendar_from_student' part
    '''
    from os import chdir, path, startfile
    import re
    file_directory= path.dirname(__file__)
    wd = re.findall(".+Scripts",file_directory)[0]
    chdir(wd)

  
    import pandas as pd


    #we import all functions that are used
    from week_calendar.python_files.secondary_functions_for_week_calendar_for_students import clean_cal
    from week_calendar.python_files.count_hours_each_day import count_hours_each_day
    from week_calendar.python_files.redistribute_hours_with_objective_func import redistribute_hours_with_objective_func
    from week_calendar.python_files.fill_week_calendar_for_students import put_hours_in_calendar, cal_with_subjects_only
    from week_calendar.python_files.set_priority import set_priority,order_hours_df


    #we create two templates of subjects and proportion
    original_cal_from_student_in_pandas = clean_cal(calendar_from_student)#converting calendar from student in pd

    reordered_cal_from_student_in_pandas = set_priority(original_cal_from_student_in_pandas,order)#reordering calendar to fit priority

    df_count_hours_each_day = count_hours_each_day(subj_with_coeffs,hours_of_work,coeff_per_day) #exact hours for each subject and day
    # print(df_count_hours_each_day)
    
    redistrib = redistribute_hours_with_objective_func(df_count_hours_each_day,time_unit) #hours rounded and redistributed to fit the coefficients
    # print(redistrib)
    temp_hour_in_cal_and_remaing_hours = put_hours_in_calendar(redistrib,reordered_cal_from_student_in_pandas.drop(['key_0'], axis = 1),time_unit)#2list with subjects integrated in the student's rearanged calendar and remaining hours
    temp_hour_in_cal = temp_hour_in_cal_and_remaing_hours[0]
    remaining_hours = temp_hour_in_cal_and_remaing_hours[1]
    temp_hour_in_cal.insert(0,'key_0',reordered_cal_from_student_in_pandas['key_0'])#inserting the column corresponding to weekdays

    hour_in_cal = order_hours_df(temp_hour_in_cal) #creating final df

    writer = pd.ExcelWriter("examples_of_schedule\\" + final_calendar_name +'.xlsx', engine = 'xlsxwriter')
    workbook  = writer.book
    workbook.filename = str(final_calendar_name) +'.xlsm'

    workbook.add_vba_project('week_calendar\\secondary_files\\vbaProject.bin')

    if delete_original_calendar == True:
        cal_with_subjects_only(hour_in_cal,original_cal_from_student_in_pandas).to_excel(writer, sheet_name = 'Sheet1') #non subject cells from calendar removed

    else:
        hour_in_cal.to_excel(writer, sheet_name = 'Sheet1')

    #gives writing, viewing and executing permissions to everyone... doesn't work
    # writer.save()
    # os.chmod(path.abspath(workbook.filename),777)
    
    worksheet = writer.sheets['Sheet1']




    # Add a button tied to a macro in the VBA project.
    worksheet.insert_button('K15', {'macro':   'nice_everything',
                                'caption': 'Make it nice!',
                                'width':   120,
                                'height':  70})
                                
    writer.save()
    writer.close()
    
    #doesn't work, authorization issues
    # os.unlink(path.abspath(final_calendar_name)+'.xlsx')

    import win32com.client
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Workbooks.Open(path.abspath(workbook.filename))
    if run_macro == True:
        xl.Application.Run(workbook.filename + '!Module2.nice_everything')
    
    # import portalocker#file control module

    # portalocker.unlock(path.abspath(workbook.filename))
    # xl.protection = False

    
    startfile(path.abspath(workbook.filename), 'open')
    # xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly = 1" part from the open function.
    # xl.Application.Quit() # Comment this out if your excel script closes
    xl.Workbooks.Close()
    




    return remaining_hours

# %%
