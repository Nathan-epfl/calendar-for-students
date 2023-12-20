


#%%lots of tests



#%%
#we set the current folder as main to call calendar_for_students
from os import chdir,path
wd= path.dirname(__file__)
chdir(wd)
from secondary_functions_for_week_calendar_for_students import clean_cal,nan_to_str
#we create two templates of subjects and proportion
arg_ex=[['maths',0.3],['physics',0.3],['geography',0.3],['English',0.1]]
arg_ex2=[['maths',0.7],['physics',0.3]]
template_cal_half_hours=clean_cal('template_calendar.xlsx')

#we import all functions that are used
from count_hours_each_day import count_hours_each_day
from redistribute_hours import redistribute_hours
from fill_week_calendar_for_students import put_hours_in_calendar, cal_with_subjects_only
import datetime

#each block starts with a timer
start_time = datetime.datetime.now()
df_count1=count_hours_each_day(arg_ex2,26,[1,1,2,1,1,4,4]) #exact hours for each subject and day
redistrib1=redistribute_hours(df_count1,0.5) #hours rounded and redistributed to fit the coefficients
hour_in_cal1=put_hours_in_calendar(redistrib1,template_cal_half_hours) #subjects integrated in the student's calendar
cal_sub_only1=cal_with_subjects_only(hour_in_cal1,template_cal_half_hours) #non subject cells from calendar removed
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
df_count2=test=count_hours_each_day(arg_ex,18,[0,0,1,1,1,1,1])
redistrib2=redistribute_hours(df_count2,0.5)
hour_in_cal2=put_hours_in_calendar(redistrib2,template_cal_half_hours)
cal_sub_only2=cal_with_subjects_only(hour_in_cal2,template_cal_half_hours)
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
df_count3=test=count_hours_each_day(arg_ex2,40,[0,1,1,3,1,7,4])
redistrib3=redistribute_hours(df_count3,0.5)
hour_in_cal3=put_hours_in_calendar(redistrib3,template_cal_half_hours)
cal_sub_only3=cal_with_subjects_only(hour_in_cal3,template_cal_half_hours)
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
df_count4=test=count_hours_each_day(arg_ex,20,[8,1,1,1,1,0,0])
redistrib4=redistribute_hours(df_count4,0.5)
hour_in_cal4=put_hours_in_calendar(redistrib4,template_cal_half_hours)
cal_sub_only4=cal_with_subjects_only(hour_in_cal4,template_cal_half_hours)
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
df_count5=test=count_hours_each_day(arg_ex2,12,[2,4,3,1,1,4,4])
redistrib5=redistribute_hours(df_count5,0.5)
hour_in_cal5=put_hours_in_calendar(redistrib5,template_cal_half_hours)
cal_sub_only5=cal_with_subjects_only(hour_in_cal5,template_cal_half_hours)
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
df_count6=test=count_hours_each_day(arg_ex2,40,[1,2,2,1,1,1,1])
redistrib6=redistribute_hours(df_count6,0.5)
hour_in_cal6=put_hours_in_calendar(redistrib6,template_cal_half_hours)
cal_sub_only6=cal_with_subjects_only(hour_in_cal6,template_cal_half_hours)
end_time = datetime.datetime.now()
print(end_time - start_time)
# %%
import pandas as pd
exp_hour_in_cal3=hour_in_cal3.to_excel('nice_hour_in_cal3.xlsx')
exp_sub_only3=cal_sub_only3.to_excel('nice_cal_sub_only3.xlsx')

# %%
exp_sub_only3=cal_sub_only3.to_excel('nice_cal_sub_only3.xlsx')
