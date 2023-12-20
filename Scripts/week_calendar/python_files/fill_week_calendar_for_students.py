#%%
'''
function that takes a student's schedule and incorporates subjects to study to it
the function takes a value from redistributes_hours function 
and a value from clean_cal function in secondary_functions_for_calendar_for_students 
and gives a calendar filled with subjects to study
'''

from week_calendar.python_files.secondary_functions_for_week_calendar_for_students import next_day,next_row,previous_row
import pandas as pd
import numpy as np

def put_hours_in_calendar(df_hours = pd.core.frame.DataFrame, schedule_of_student = pd.core.frame.DataFrame, time_unit=0.5):


    #creates cal as a list and fills cal with weeks as dataframes
    schedule=schedule_of_student.copy()

    hours_to_fill=df_hours.copy().drop(['coeff','expected_coeff'])

    
    for day in hours_to_fill.columns: #iterating on days
        #hours_to_fill=hours_to_fill.reindex(index=np.roll(hours_to_fill.index,1)) #we cycle 'hours_to_fill' to change priority of subjects
        hours_to_fill=hours_to_fill.sort_values(day,ascending=False) #we sort the subjects hours in decreasing order 
        for sub in hours_to_fill.index: #iterating on subject
            for hour in schedule.index: #iterating on hours
                #fills the cell if it is not the only half an hour in the day of that subject, otherwise it will go to next day
                if (schedule.loc[hour,day] == '') and (hours_to_fill.loc[sub,day]>0) and (((schedule.loc[next_row(hour,schedule),day]=='') and (hours_to_fill.loc[sub,day]>0.5)) or (schedule.loc[previous_row(hour,schedule),day]==sub)):
                    schedule.loc[hour,day] = sub
                    hours_to_fill.loc[sub,day] = hours_to_fill.loc[sub,day] - time_unit #emptying hours
                                #break
                                #print(counthours)
            hours_to_fill.loc[sub,next_day(day)] += hours_to_fill.loc[sub,day] #if hours could not be fitted, they go to next day
    remaining_hours=hours_to_fill.copy()
    return schedule, remaining_hours


# %%
import pandas as pd
def cal_with_subjects_only(cal,schedule):
    cal_sub_only=cal.copy()
    for day in cal.columns:
        for hour in cal.index:
            if cal.loc[hour,day]==schedule.loc[hour,day]:
                cal_sub_only.loc[hour,day]=''
    return cal_sub_only

#%%
# out_schedule, out_remaining_hours = put_hours_in_calendar(out_redistribute_hours_with_objective_func,out_set_priority)
# %%
# out_schedule
# %%
#final_schedule_without_original=cal_with_subjects_only(final_schedule_with_original[0],schedule)
# %%
#final_schedule_without_original
# %%
