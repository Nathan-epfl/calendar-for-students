#%% get next monday (even if today's monday)
import datetime
def n_mondays_after(i):
    now = datetime.datetime.now()
    today = datetime.datetime.now() - datetime.timedelta(hours = now.hour,
                            minutes = now.minute,
                             seconds = now.second,
                             microseconds = now.microsecond)
    if today.weekday() != 0:
        return today + datetime.timedelta(days = (-datetime.datetime.now().weekday())%7 + 7 * (i - 1))
    else:
        return today + datetime.timedelta(days = 7 * i)


#%% model for each subject
import math
import datetime
def exp_coefficient_each_week_of_subjects(dict_of_subj,today = datetime.datetime.today()):
    coeff_each_day_all_subjects = {subj : [] for subj in dict_of_subj}
    final_list_of_days_before_exam = []
    
    for subj in dict_of_subj.keys():
        timedelta_before_exam = dict_of_subj[subj].last_exam_date - today
        days_before_exam = timedelta_before_exam.days
        list_of_each_days_before_exam = [today +datetime.timedelta(days = x) for x in range(days_before_exam)]
        if len(final_list_of_days_before_exam) < len(list_of_each_days_before_exam):
            final_list_of_days_before_exam = list_of_each_days_before_exam
        
        for t in range(days_before_exam):
            subj_coeff_each_day = math.exp(
                t + math.log(2 - dict_of_subj[subj].weight) - days_before_exam + 1
            ) + dict_of_subj[subj].weight
            coeff_each_day_all_subjects[subj].append(round(subj_coeff_each_day,3))
    
    
    final_df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in coeff_each_day_all_subjects.items() ])).fillna(0)
    final_df.index = final_list_of_days_before_exam
    final_df['sum_of_coeffs'] = sum(final_df[col] for col in final_df.columns)
    
    
    return final_df
    

#%%
import pandas as pd
def poly_deg_n_coefficient_each_week_of_subjects(dict_of_subj,degree,today = datetime.datetime.today()):
    coeff_each_day_all_subjects = {subj : [] for subj in dict_of_subj}
    for subj in dict_of_subj.keys():
        timedelta_before_exam = dict_of_subj[subj].last_exam_date - today
        days_before_exam = timedelta_before_exam.days
        list_of_each_days_before_exam = [today +datetime.timedelta(days = x) for x in range(days_before_exam + 1)]
        for t in range(days_before_exam + 1):
            subj_coeff_each_day = (
                ((1 - dict_of_subj[subj].weight) / (days_before_exam ** degree)) * (t ** degree)
                +dict_of_subj[subj].weight
                )
            coeff_each_day_all_subjects[subj].append(round(subj_coeff_each_day,3))
    final_df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in coeff_each_day_all_subjects.items() ])).fillna(0)
    final_df.index = list_of_each_days_before_exam
    final_df['sum_of_coeffs'] = sum(final_df[col] for col in final_df.columns)
    return final_df





#%%
# example_of_student_curriculum['maths AA_SL'].weight = 0.1
# example_of_student_curriculum['physics HL'].weight = 0.2
# example_of_student_curriculum['geography SL'].weight = 0.1
# example_of_student_curriculum['history HL'].weight = 0.4
# example_of_student_curriculum['philosophy HL'].weight = 0.2
# poly_deg_n_coefficient_each_week_of_subjects(example_of_student_curriculum,40)






# %%
#function that gives next row to a dataframe
def next_row(row_entry,df):
    list_of_rows = list(df.index.values)
    for row in df.index:
        if row == row_entry:
            return list_of_rows[(list_of_rows.index(row) + 1)%len(list_of_rows)]

#function that gives previous row to a dataframe
def previous_row(row_entry,df):
    list_of_rows = list(df.index.values)
    for row in df.index:
        if row == row_entry:
            return list_of_rows[(list_of_rows.index(row) - 1)%len(list_of_rows)]



#function that rounds "x" down or up to a factor "k", up or down depending on "type"
def round_up_down(x,k,type):
    if float(int(x / k) * k - x) == float(0):
        return x
    elif type == 'down':
        return ((x / k) // 1) * k
    elif type == 'up':
        return (((x / k) // 1) + 1) * k

# %%
