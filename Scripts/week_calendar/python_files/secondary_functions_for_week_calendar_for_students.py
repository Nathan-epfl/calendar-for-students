#This file contains secondary functions that are necessary to to run the main functions
#%% used before for "count_hours_each_day", but now useless

#function that sends 'Monday' to 'Tuesday', ... 'Sunday' to 'Monday'
def next_day(day_to_shift = str):
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for day in days:
        if day == day_to_shift:
            return days[(days.index(day)+1)%len(days)]



#function that sends 'Sunday' to 'Saturday', .... 'Monday' to 'Sunday'
def previous_day(day_to_shift = str):
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for day in days:
        if day == day_to_shift:
            return days[(days.index(day)-1)%len(days)]
#%%used for "redistribute_hours"

import pandas as pd

#function that gives next row to a dataframe
def next_row(row_entry = str, df = pd.core.frame.DataFrame):
    list_of_rows = list(df.index.values)
    for row in df.index:
        if row == row_entry:
            return list_of_rows[(list_of_rows.index(row)+1)%len(list_of_rows)]



#function that gives previous row to a dataframe
def previous_row(row_entry = str ,df = pd.core.frame.DataFrame):
    list_of_rows=list(df.index.values)
    for row in df.index:
        if row == row_entry:
            return list_of_rows[(list_of_rows.index(row)-1)%len(list_of_rows)]



#function that rounds "x" down or up to a factor "k", up or down depending on "type"
def round_up_down(x, k, type = str):
    if float(int(x/k)*k-x)==float(0):
        return x
    elif type=='down':
        return ((x/k)//1)*k
    elif type=='up':
        return (((x/k)//1)+1)*k




# %% used for "fill_calendar_for_students"
# 
# function that converts nan's into strings


import math 
def nan_to_str(string = str):
    try:
        if math.isnan(string)==True:
            string = ''
            return string
    except Exception:
        return string

# function that takes an xlsx file and gives a pandas dataframe of the xlsx with nan's converted into empty strings
import pandas as pd
def clean_cal(path_of_excel = str):
    calen=pd.read_excel(path_of_excel,index_col=0)
    for col in calen.columns:
        calen[col] = calen[col].apply(nan_to_str)
    return calen

#%% 
# out_clean_cal = clean_cal('week_calendar\\excel_templates\\template_calendar.xlsx')
# %%
# schedule
# %%
