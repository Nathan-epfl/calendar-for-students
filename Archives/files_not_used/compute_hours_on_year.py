#%% distribute_hours_on_year
from IB_subject_class import *
import pandas as pd
import copy
import datetime
def compute_hours_on_year(dict_of_of_subjects_with_coeff_changed,
                             total_hours_per_week,
                             today=datetime.datetime.now()
                             ):
    # function that takes a dictionary of subjects, an (approximate) amount of hours 
    # the student wants to work on each week and the date of start of the calendar
    #and outputs a 2- list [{<subject>: <adapted coefficient according to teaching hours>}, <df containing hours per subtopic>]
    # global subjects #"subjects" is in ib_subject.py script
    dict_of_subj_copy=copy.deepcopy(dict_of_of_subjects_with_coeff_changed)
    today=pd.to_datetime(today)
    date_of_last_exam_of_all_subjects=today
    for subj in dict_of_subj_copy:
        if dict_of_subj_copy[subj].last_exam_date>date_of_last_exam_of_all_subjects:
            date_of_last_exam_of_all_subjects=dict_of_subj_copy[subj].last_exam_date
    
    remaining_timedelta=pd.to_datetime(date_of_last_exam_of_all_subjects)-today
    remaining_weeks=remaining_timedelta.days//7
    sum_every_subj_coefficients=0       

    
    #isolating core from other subjects
    for subj in dict_of_subj_copy:
        dict_of_subj_copy[subj].syllabus=dict_of_of_subjects_with_coeff_changed[subj].syllabus
        dict_of_subj_copy[subj].syllabus.rename(columns = {'hours_'+dict_of_subj_copy[subj].level : 'coefficient'}, inplace = True) 
        sum_every_subj_coefficients+=sum(dict_of_subj_copy[subj].syllabus['coefficient'])
    
    #creating new collumn that sets the amount of hours of work for each section
    for subj in dict_of_subj_copy:
        dict_of_subj_copy[subj].syllabus['total_amount_of_hours']=\
            dict_of_subj_copy[subj].syllabus['coefficient'].apply(
                lambda x : total_hours_per_week*remaining_weeks*x/sum_every_subj_coefficients)


    #creating a dataframe containing every core subject of every topic
    df_subj_syllabus_coeffs_tot_hours=pd.concat(
        [dict_of_subj_copy[subj].syllabus for subj in dict_of_subj_copy],
        keys=[dict_of_subj_copy[subj].name for subj in dict_of_subj_copy],
        names=['subject'])

    # creating the dictionnary dict_of_subj_and_coeffs containing each main subject and coeff
    dict_of_subj_and_coeffs={
        subj : \
        sum(df_subj_syllabus_coeffs_tot_hours.loc[subj]['coefficient'])
    for subj in set(df_subj_syllabus_coeffs_tot_hours.index.get_level_values(0)) }


    sum_of_all_coeffs=sum(val for val in dict_of_subj_and_coeffs.values())
    for subj in dict_of_subj_and_coeffs.keys():
        dict_of_subj_and_coeffs[subj]=dict_of_subj_and_coeffs[subj]/sum_of_all_coeffs*total_hours_per_week
    return [dict_of_subj_and_coeffs,df_subj_syllabus_coeffs_tot_hours]
#%%
# import extract_subj_from_dict as extract
# import change_coeffs_of_subjects as change_coeffs
# from IB_subject_class import *
# example_of_student_curriculum=extract.extract_subj_from_dict(dict_of_choices_at_end_of_file_ib_subject)

# #%%
# student_curr_coeff_changed=change_coeffs.change_coeffs_of_subjects(example_of_student_curriculum,
#     {'maths AA_SL': 3,'physics HL': 4,'geography SL' : 1,'history HL':2, 'philosophy HL' : 4}
#     )
#%%
hours_on_year=compute_hours_on_year(coeff_changed,24,today='1 sept 2021')
# %%
# %%
