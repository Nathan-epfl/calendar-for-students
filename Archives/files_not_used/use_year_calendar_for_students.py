#%%
#use_year_calendar_for_students




########################################################################################################################################################################
########################################################################################################################################################################

#%% from redistribute houes on each week
from IB_subject_class import *
import extract_subj_from_dict as extract
import change_coeffs_of_subjects as change_coeffs
import compute_hours_on_year as compute
from transform_coeff_to_hours import transform_coeff_to_hours
from redistribute_hours_of_subj_each_day_of_year import redistribute_hours_each_day_of_year
from secondary_func_of_year_cal_for_students import *
tot_hour_per_week=28
today='1 sept 2021'

#%%
example_of_student_curriculum=extract.extract_subj_from_dict(dict_of_choices_at_end_of_file_ib_subject)

#%%
student_curr_coeff_changed=change_coeffs.change_coeffs_of_subjects(
    example_of_student_curriculum,
    
)

#%%
subj_with_hours_per_year_and_coeffs=compute.compute_hours_on_year(student_curr_coeff_changed,tot_hour_per_week,today=today)


#%%
example_of_student_curriculum['maths AA_SL'].weight=3
example_of_student_curriculum['physics HL'].weight=2
example_of_student_curriculum['geography SL'].weight=3
example_of_student_curriculum['history HL'].weight=1
example_of_student_curriculum['philosophy HL'].weight=2

df_of_coeff_per_day_exponential=transform_coeff_to_hours(
    example_of_student_curriculum,
    tot_hour_per_week,
    exp_coefficient_each_week_of_subjects,
    today=today
)
# df_of_coeff_per_day_polynomial=transform_coeff_to_hours(example_of_student_curriculum,25,lambda x,y=datetime.datetime.today(): poly_deg_n_coefficient_each_week_of_subjects(x,40,y))
# %%
redistribute_hours_each_day_of_year(df_of_coeff_per_day_exponential,0.5)

#%%
df_of_coeff_per_day_exponential.iloc[:,-15:]
# %%
#pretty confident we need exponential one, because it will keep the days of increase to a steady 4-6 days, where polynomial depends on the amount of total days
# redistribute_hours_each_day_of_year(df_of_coeff_per_day_polynomial,0.5)
#%%

# ,today=pd.to_datetime('1 sept 2020'))




subj_with_hours_per_year_and_coeffs[1]


# %%
