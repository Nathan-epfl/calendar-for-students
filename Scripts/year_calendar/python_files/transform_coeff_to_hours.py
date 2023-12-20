#%%transform coeff to hours
import copy
import datetime
import numpy
import pandas as pd
from year_calendar.python_files.IB_subject_class import *
from year_calendar.python_files.secondary_func_of_year_cal_for_students import *
from week_calendar.python_files.secondary_functions_for_week_calendar_for_students import *

def transform_coeff_to_hours(
    subjects,
    total_hours_per_week,
    func_on_coeffs,
    today = datetime.datetime.today(),
    calendar_from_student = 'year_calendar\\xls_files\\template_calendar.xlsx'
):
    '''
    function that takes a dict of subjects and ib_subject objects, (approximated) hours of work per week,
    a function that will change the coefficients from day to day to increase it a few days before the exam,
    the date of start of the calendar and the schedule of the student
    and outputs a dataframe of each hour of each subject for each remaining days before exam

    it first gives a naive amount of hours per day, with hours growing before last exam date,
    and then changes the hours to fit the amount of hours in the year
    '''

    today = pd.to_datetime(today)

    # before = datetime.datetime.now() #just here to know how long the program takes
    
    subjects_copy = copy.deepcopy(subjects) #deepcopy of subjects of student
    
    total_of_weights = sum(subjects[subj].weight for subj in subjects) #computes the total of weights

    date_of_last_exam_of_all_subjects = datetime.datetime.now() #temporary date of final exam set to now
    
    #setting last exam date
    for subj in subjects_copy:
        if subjects[subj].last_exam_date > date_of_last_exam_of_all_subjects:
            date_of_last_exam_of_all_subjects = subjects[subj].last_exam_date
    
    #setting timedelta before last exam
    timedelta_before_end_of_exams = date_of_last_exam_of_all_subjects - today #computes how much time is left before the end of the exams
    
    #dict of subjects and expected annual hours of work for each subject
    expected_annual_hours_per_subject = {
        subj: 
        subjects[subj].weight / total_of_weights * total_hours_per_week / 7 * timedelta_before_end_of_exams.days
        for subj in subjects
    }

    
    #setting dict_of_variation_per_subj, which will be the variable readjusting on each loop
    dict_of_variations_per_subj = {subj : 0 for subj in subjects}

    #setting all gaps list to contain each biggest gap of all loops
    all_gaps = []



    #creating list of coeffs per day
    calendar_from_student_in_pandas = clean_cal(calendar_from_student)
    list_of_free_hours_each_week_from_calendar_student_in_pandas = [
        len(calendar_from_student_in_pandas[x][calendar_from_student_in_pandas[x] == '']) / 2 
        for x in calendar_from_student_in_pandas.columns
    ]
    total_hours_free_per_week = sum(list_of_free_hours_each_week_from_calendar_student_in_pandas)


    #creating a loop to readjust the coefficients of each subject 
    #(since the coefficients are varying through time, they might not respect the initial choice of the student)
    for _ in range(100):

        #readjusting each subject's weight
        for subj in subjects_copy:
        
            subjects_copy[subj].weight = subjects[subj].weight * (1 + dict_of_variations_per_subj[subj])
    



        #normalizing weights
        total_of_temp_weights = sum(subjects[subj].weight for subj in subjects_copy)
        for subj in subjects:
            subjects_copy[subj].weight = subjects_copy[subj].weight / total_of_temp_weights
        

         #creating temporary df_of_coeffs per subject, based on the function given
        temp_df_of_coeffs = func_on_coeffs(subjects_copy,today)



        #converting coefficients to hours in two steps

        #first step
        temp_df_of_coeffs = temp_df_of_coeffs.divide(
            temp_df_of_coeffs['sum_of_coeffs']
            ,axis = 0
        ).drop('sum_of_coeffs',axis = 1)


        #second step, with change based on availabilities per weekday
        def change_coeff_based_on_free_time_per_week(day_series,weekday):
            return day_series.apply(lambda x: x * list_of_free_hours_each_week_from_calendar_student_in_pandas[weekday] / total_hours_free_per_week * 7)
        temp_df_of_coeffs = temp_df_of_coeffs.apply(lambda x: change_coeff_based_on_free_time_per_week(x,x.name.weekday()),axis = 1)
        temp_df_of_coeffs = temp_df_of_coeffs.mul(total_hours_per_week / 7)


        #computing resulting annual hours per subject
        annual_hours_per_subject = {
            subj:
            sum(temp_df_of_coeffs[subj])
            for subj in subjects
        }
        
        #computing biggest gap on the subjects between annual hours and expected annual hours
        biggest_gap_on_temp_df = numpy.max([abs(expected_annual_hours_per_subject[subj] - annual_hours_per_subject[subj]) for subj in subjects])
        
        #appending to all gaps to keep a record
        all_gaps.append(biggest_gap_on_temp_df)
        
        #taking smallest biggest gap to compare with present biggest gap
        temp_min_max = numpy.min(all_gaps)

        #setting final df to be temp df if the new gap is the smallest one
        if len(all_gaps) > 1:
            if biggest_gap_on_temp_df <= temp_min_max:
                final_df_of_coeffs = temp_df_of_coeffs
        else:
            final_df_of_coeffs = temp_df_of_coeffs

        #breaking loop if the gap is small enough. The function was set on march the 2nd 2021, depending on
        #some tests made. It's a line of best fit calculated when the loop is length 200
        
        ############### needs to be changed################

        if temp_min_max < 0.03 * total_hours_per_week + 0.42:
            break
        #####################################################

        #readjusting coefficients for each subject to do next loop
        for subj in subjects_copy:
            if annual_hours_per_subject[subj] < expected_annual_hours_per_subject[subj] - 1:
                dict_of_variations_per_subj[subj] = dict_of_variations_per_subj[subj] + 0.01
            elif annual_hours_per_subject[subj] > expected_annual_hours_per_subject[subj] + 1:
                dict_of_variations_per_subj[subj] = dict_of_variations_per_subj[subj] - 0.01
        
        # print(biggest_gap_on_temp_df)

    
    # ############ uncomment following to do some tests################
    # min_of_max = numpy.min(all_gaps)
    # print(min_of_max)
    # print(all_gaps[-1])

    # annual_hours_per_subject = {
    #         subj:
    #         sum(final_df_of_coeffs[subj])
    #         for subj in subjects
    #     }
        
    # biggest_gap_on_final_df = numpy.max([abs(expected_annual_hours_per_subject[subj] - annual_hours_per_subject[subj]) for subj in subjects])
    # print(biggest_gap_on_final_df)
    # ##########################################################


    # after = datetime.datetime.now()
    # print(after - before)
    
    return final_df_of_coeffs.T
# %% tests
# out_transform_coeff_to_hours = transform_coeff_to_hours(
    out_change_coeffs_of_subjects,
    25,
    exp_coefficient_each_week_of_subjects
# )

# %%
# out_transform_coeff_to_hours
# %%
