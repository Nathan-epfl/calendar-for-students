#%%
from os import chdir,path
import re
file_directory= path.dirname(__file__)
wd = re.findall(".+Scripts",file_directory)[0]
chdir(wd)
#%%
hours_per_week = 27
dict_of_choices = {
    'maths AA_SL': {},
    'physics HL': {'option' : ['Astrophysics']},
    'chemistry HL': {'option' : ['Energy']},
    'biology HL': {'option' : ['Human physiology']},
    'geography SL' : {'HL' : 0,'option':['Extreme environments','Leisure, sport and tourism']},
    'history HL' : {'HL' : ['History of the Americas'],'option' : ['Society and economy (750–1400)','Causes and effects of wars (750–1500)','Dynasties and rulers (750–1500)']},
    'philosophy HL' : {'option':['Ethics','Philosophy of science']}
}
dict_of_coeffs_of_subj = {
    'maths AA_SL': 3,
    'physics HL': 9,
    'chemistry HL': 4,
    'biology HL': 3,
    'geography SL' : 1,
    'history HL' : 1,
    'philosophy HL' : 0
}
start = '1 jan 2022'
# %%
from year_calendar.python_files.year_calendar_for_students import *
all_steps = year_calendar_for_students(
    dict_of_choices,
    dict_of_coeffs_of_subj,
    hours_per_week,
    'year_calendar\\xls_files\\template_calendar.xlsx',
    'year_cal_test_25_07_22_2',
    order=[[2,3,1],[2,1,3]],
    delete_original_calendar = True,
    run_macro = False, #True doesn't work
    date_of_start_of_calendar = start
)
#%%
all_steps["week_dfs"][0]
#%%some tests

number_of_days = len(all_steps["df_hours_per_day"][all_steps["df_hours_per_day"] != 0].dropna(axis = 1,how = 'all').columns)
df_summary = pd.DataFrame(index = all_steps["df_hours_per_day"].index)
df_summary['counted_per_subj']=[sum(all_steps["df_hours_per_day"].loc[x]) for x in all_steps["df_hours_per_day"].index] 
df_summary['expected_per_subj']=[dict_of_coeffs_of_subj[x] * number_of_days * hours_per_week / sum(dict_of_coeffs_of_subj.values()) / 7 for x in all_steps["df_hours_per_day"].index]
df_summary.loc['sum']=[sum(df_summary[x]) for x in df_summary.columns] 
#%% gives the total gap between expected and given hours per subject
df_summary

# %% gives the coefficients of last month
all_steps["df_hours_per_day"].iloc[:,-21:-1]

# %%
all_steps["df_hours_per_day"].iloc[:,-51:-1].to_excel('testing_27_06_22.xlsx')
# %%
