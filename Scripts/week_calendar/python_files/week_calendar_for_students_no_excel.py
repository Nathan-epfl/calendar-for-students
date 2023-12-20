#%% function that takes a calendar, a list,an integer, a list and a float and gives a calendar exported in excel

#'calendar_from_student' is the name of the xlsx ('.xlsx' included) file containing the student's schedule
#'subj_with_coeff is a list of 2-lists containing name of subject and coefficient of the subject 
#'hours_of work' is the (approximate) amount of hours the students wants to work
#'coeff_per_day' is a 7-list with a coefficient for each day of the week, starting with monday
#'time_unit' is the interval of time in the calendar. It must correspond with 'calendar_from_student'!
#if True is given at the end, then the final calendar will have deleted the 'calendar_from_student' part

def week_calendar_for_students_no_excel(  calendar_from_student,
                                subj_with_coeffs,
                                hours_of_work,
                                coeff_per_day = [1] * 7,
                                time_unit = 0.5,
                                order = [[1,2,3],[2,1,3]],
                                ):

    from os import chdir,path
    import re
    file_directory= path.dirname(__file__)
    print(file_directory)
    wd = re.findall(".+Scripts",file_directory)[0]
    print(wd)
    chdir(wd)
    
    #we import all functions that are used
    from week_calendar.python_files.secondary_functions_for_week_calendar_for_students import clean_cal
    from week_calendar.python_files.count_hours_each_day import count_hours_each_day
    from week_calendar.python_files.redistribute_hours_with_objective_func import redistribute_hours_with_objective_func
    from week_calendar.python_files.fill_week_calendar_for_students import put_hours_in_calendar
    from week_calendar.python_files.set_priority import set_priority,order_hours_df



    #we create two templates of subjects and proportion
    
    original_cal_from_student_in_pandas = clean_cal(calendar_from_student)#converting calendar from student in pd

    reordered_cal_from_student_in_pandas = set_priority(original_cal_from_student_in_pandas,order)#reordering calendar to fit priority

    df_count_hours_each_day = count_hours_each_day(subj_with_coeffs,hours_of_work,coeff_per_day) #exact hours for each subject and day
    
    redistrib = redistribute_hours_with_objective_func(df_count_hours_each_day,time_unit) #hours rounded and redistributed to fit the coefficients
    
    
    temp_hour_in_cal_and_remaining_hours = put_hours_in_calendar(redistrib,reordered_cal_from_student_in_pandas.drop(['key_0'], axis = 1),time_unit)#2list with subjects integrated in the student's rearanged calendar and remaining hours
    temp_hour_in_cal = temp_hour_in_cal_and_remaining_hours[0]
    remaining_hours = temp_hour_in_cal_and_remaining_hours[1]
    temp_hour_in_cal.insert(0,'key_0',reordered_cal_from_student_in_pandas['key_0'])#inserting the column corresponding to weekdays

    hour_in_cal = order_hours_df(temp_hour_in_cal) #creating final df

    return hour_in_cal




# %%
