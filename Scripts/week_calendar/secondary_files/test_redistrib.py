#%% function that takes a calendar, a list,an integer, a list and a float and gives a calendar exported in excel

#'calendar_from_student' is the name of the xlsx ('.xlsx' included) file containing the student's schedule
#'subj_with_coeff is a list of 2-lists containing name of subject and coefficient of the subject 
#'hours_of work' is the (approximate) amount of hours the students wants to work
#'coeff_per_day' is a 7-list with a coefficient for each day of the week, starting with monday
#'time_unit' is the interval of time in the calendar. It must correspond with 'calendar_from_student'!
#if True is given at the end, then the final calendar will have deleted the 'calendar_from_student' part

def week_calendar_for_students_up_to_redistrib(  calendar_from_student,
                                subj_with_coeffs,
                                hours_of_work,
                                final_calendar_name,
                                coeff_per_day=[1]*7,
                                time_unit=0.5,
                                order=[[1,2,3],[2,3,1]],
                                delete_original_calendar=False, 
                                run_macro=True
                                ):
    import re
    import pandas as pd
    import xlsxwriter
    from openpyxl import load_workbook


    from os import chdir,path,remove
    wd= path.dirname(__file__)
    chdir(wd)
    #we import all functions that are used
    from secondary_functions_for_week_calendar_for_students import clean_cal,nan_to_str
    from count_hours_each_day import count_hours_each_day
    from redistribute_hours_with_objective_func import redistribute_hours_with_objective_func
    from fill_week_calendar_for_students import put_hours_in_calendar, cal_with_subjects_only
    from set_priority import set_priority,order_hours_df



    #we create two templates of subjects and proportion
    original_cal_from_student_in_pandas=clean_cal(calendar_from_student)#converting calendar from student in pd

    reordered_cal_from_student_in_pandas=set_priority(original_cal_from_student_in_pandas,order)#reordering calendar to fit priority

    df_count_hours_each_day=count_hours_each_day(subj_with_coeffs,hours_of_work,coeff_per_day) #exact hours for each subject and day
    
    
    print('done!')
    return reordered_cal_from_student_in_pandas



# %%
from os import chdir,path
wd= path.dirname(__file__)
chdir(wd)
from week_calendar_for_students import week_calendar_for_students
final_df_pd=week_calendar_for_students_up_to_redistrib(
    wd+ '\\excel_templates\\template_calendar_empty.xlsx', #name of the xlsx ('.xlsx' included) file containing the student's schedule
    [['English',4],['francais',4],['maths',7],['biologie',0],['chem',10],['histoire',8]], # list of 2-lists containing name of subject and coefficient of the subject 
    33, #the (approximate) amount of hours the students wants to work
    'closexls_hope_that_no_small_hours', #name of output file
    [7]*7, #7-list with a coefficient for each day of the week, starting with monday
    time_unit=0.5, #the interval of time in the calendar. It must correspond with the original calendar!
    order=[[1,2,3],[1,2,3]],
    delete_original_calendar=True, #False by default, if True is given at the end, then the final calendar will have deleted the 'calendar_from_student' part
    run_macro=False) #True by default. If "False" given, then the excel doesn't run the macro to make the calendar nice, and the user can apply small modifications

# %%

# %%
