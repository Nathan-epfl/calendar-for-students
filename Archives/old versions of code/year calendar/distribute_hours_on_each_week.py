





#%% distribute hours on each week
import pandas as pd
from secondary_func_of_year_cal_for_students import n_mondays_after
import datetime
def distribute_hours_on_each_week(subj_and_hours_on_year_and_coeffs,total_hours_per_week,end_of_exams):
    remaining_timedelta = pd.to_datetime(end_of_exams) - datetime.datetime.now()
    remaining_weeks = remaining_timedelta.days // 7
    
    df_with_subj_and_hours_each_week = subj_and_hours_on_year_and_coeffs[1]
    for i in range(remaining_weeks + 1):
        df_with_subj_and_hours_each_week[n_mondays_after(i + 1)] = 0

    
    return df_with_subj_and_hours_each_week

#%% testing
from IB_subject_class import *
import extract_subj_from_dict as extract
import change_coeffs_of_subjects as change_coeffs
import compute_hours_on_year as compute
tot_hour_per_week = 28
exam_date = '20 May 2021'
example_of_student_curriculum = extract.extract_subj_from_dict(dict_of_choices_at_end_of_file_ib_subject)
student_curr_coeff_changed = change_coeffs.change_coeffs_of_subjects(
    example_of_student_curriculum,
    {'maths AA_SL': 3,'physics HL': 4,'geography SL' : 1,'history HL' : 3,'philosophy HL' : 4}
)
subj_with_hours_per_year_and_coeffs = compute.compute_hours_on_year(student_curr_coeff_changed,tot_hour_per_week,today = '1 sept 2020')

x = distribute_hours_on_each_week(subj_with_hours_per_year_and_coeffs,tot_hour_per_week,exam_date)
# %%
x
# %%
