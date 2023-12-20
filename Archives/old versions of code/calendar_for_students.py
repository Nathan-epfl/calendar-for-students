# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:11:59 2020

@author: vicki_la_tombe
"""





#%%defining count of hours for each day

# setting this file location as default
from os import chdir, getcwd
wd=getcwd()
chdir(wd)

import secondary_functions_for_calendar_for_students as sec_fun
#import pandas as pd
#count_hours_each_day takes subjects, hours in total, max per day and order, 
#and outputs dataframe with days as columns, subjects as rows,
#each cell is the amount of hours of each subject that day
def count_hours_each_day(subjects_and_coeffs,hours_in_total,coeff_per_day=[1]*7):
    #'subjects' is a list containing [subject,coeff between 0 and 1] for each subject, 
    #example:[['maths',0.7],['physics',0.1],['geography',0.2],['English',0.1]]
    #the coeffs must add-up to 1 in order to have the correct amount of total hours (see next argument)
    #the first subject will have priority on the others when filling the calendar
    #
    #'hours' is an integer representing the total mount of work per week dedicated to studying. 
    #If it is too big, the function will end when the calendar is full
    #
    #'max_per_day' is the maximum amount of hours of a subject per day
    #'max_per_day' has priority over 'hours'. So if a subjects wants to be studied more than the max_per_day,
    #it will stop at max_per_day
    #
    #by default, calendar is filled from Monday to Sunday
    #if 'reversed' passed, then calendar is filled Sunday first, Saturday second,...    
    #creating list of subjects
    subjects=[]
    for i in range(0,len(subjects_and_coeffs)):
        subjects.append(subjects_and_coeffs[i][0])
    
    
    #creating empty dataframe
    df_hours_each_day_empty=pd.DataFrame(\
    0,\
    index=subjects,\
    columns=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    df_hours_each_day=df_hours_each_day_empty
    
    
    #adding the coeffs, and defining the sum_of_coeff
    df_hours_each_day.loc['coeff']=coeff_per_day
    sum_of_coeffs=sum(df_hours_each_day.loc['coeff'])
    
    
    #creating total hours of each subject, with last row 0 because it will correspond to coefficient
    hours_per_subject=[]
    for k in range(0,len(subjects_and_coeffs)):
        hours_per_subject.append((((((subjects_and_coeffs[k][1]*hours_in_total) )))))
        #+0.25)*10)//5)*5/10))
    hours_per_subject.append(0)
    
    
    #including it to the dataframe
    df_hours_each_day['total hours']=hours_per_subject
    
    #filling 'df_hours_each_day' with corresponding hours
    for day in df_hours_each_day.drop(labels='total hours', axis=1).columns: #iterating on days
        for sub in df_hours_each_day.drop(labels='coeff', axis=0).index: #iterating on subjects
            df_hours_each_day.loc[sub,day]=df_hours_each_day.loc[sub,'total hours']*\
                                            df_hours_each_day.loc['coeff',day]/\
                                            sum_of_coeffs\
                                            #+0.25)*10//5*5/10
    return df_hours_each_day.drop(labels='total hours',axis=1)
 #df.drop(labels='total hours', axis=1) # axis 1 drops columns, 0 will drop rows that match index value in labels

#%% testing count_hours_each_day
arg_ex=[['maths',0.3],['physics',0.3],['geography',0.3],['English',0.1]]
test=count_hours_each_day(arg_ex,23,[1,4,1,1,1,4,4])
#test['corresponds']=test.loc[:,'Monday':'Sunday'].sum(axis=1)
#testo=test[test.loc['coeff','Monday':'Sunday']>2]
#testi=test[(test.loc['coeff']>2).transpose()]
testou=test.T[test.loc['coeff'].lt(2)].T
testidlou=testou.shift(-1,axis=1)


#%% function that redistributes hours to have a whole number and distributed according to the coefficients, and then rounds to the "time_unit" entered
import numpy as np
import secondary_functions_for_calendar_for_students as sec_fun
import pandas as pd
def redistribute_hours(df,time_unit):
    #df must be a dataframe coming from the function 'count_hours_each_day'
    total_hours=df.drop(index='coeff').values.sum()
    df_without_coeff=df.drop(labels='coeff', axis=0).copy()
    list_of_filled_days=[] #creating a list to store all the days that are filled in a given subject
    for sub in df_without_coeff.index: #iterating on subjects
        for day_to_empty in df_without_coeff.columns: #iterating on days to empty
            if 0<df_without_coeff.loc[sub,day_to_empty]<0.75:
                for day_to_fill in df_without_coeff.drop(columns=day_to_empty).columns:
                        if (df_without_coeff.loc[sub,day_to_empty]<=df_without_coeff.loc[sub,day_to_fill]<1):
                            df_without_coeff.loc[sub,day_to_fill]+=df_without_coeff.loc[sub,day_to_empty]
                            df_without_coeff.loc[sub,day_to_empty]=0
                            if 0<df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_fill]<0.75:
                                df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_empty]+=df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_fill]
                                df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_fill]=0
                            if (day_to_fill in list_of_filled_days)==False:
                                list_of_filled_days.append(day_to_fill)
                            break
    df_final=df_without_coeff.copy()
    df_final.loc['coeff']=df_final.iloc[:,:].sum().T
    df_final.loc['coeff']=df_final.loc['coeff'].apply(lambda x: x*sum(df.loc['coeff'])/total_hours)
    df_final.loc['expected_coeff']=df.loc['coeff']
    for sub in df_final.drop(['coeff','expected_coeff']).index:
        for day in df_final.columns:
            if df_final.loc['coeff',day]<df_final.loc['expected_coeff',day]:
                df_final.loc[sub,day]=sec_fun.round_up_down(df_final.loc[sub,day],time_unit,'up')
            else:
                df_final.loc[sub,day]=sec_fun.round_up_down(df_final.loc[sub,day],time_unit,'down')
            df_final.loc['coeff']=df_final.drop(['coeff','expected_coeff']).iloc[:,:].sum().T
            df_final.loc['coeff']=df_final.loc['coeff'].apply(lambda x: x*sum(df.loc['coeff'])/total_hours)            

    return df_final
#yobis=redistribute_hours(test,0.25)
#yobisbis=redistribute_hours(test,0.5)

#need to fix the 0.5 happening if roundup happens

#%%
def put_hours_in_calendar(df_hours,schedule):
    #'df_hours' is a dataframe with subjects as rows (with an additional row for coefficient), and days of the week as columns
    #schedule is the list of all unavailabilities, in the form of a list of 2-lists, containing start time of occupation and end time of occupation 




#%%find a nice way to distribute hours!!!!!!
#print(test.drop(index='coeff').values.sum())
#%%find a nice way to distribute hours!!!!!!
#%%find a nice way to distribute hours!!!!!!
#%% defining calendar function
import pandas as pd
#from datetime import date

#problem because no math in the dataframe at the begining
    
def fill_calendar_for_students(calendar,subjects,hours,max_per_day,order='normal'):
    #calendar must be an excel calendar with rows as hours, and columns as days of the week
    #
    #'subjects' is a list containing [subject,coeff between 0 and 1] for each subject, 
    #example:[['maths',0.7],['physics',0.1],['geography',0.2],['English',0.1]]
    #the coefficients must add-up to 1 in order to have the correct amount of total hours (see next argument)
    #the first subject will have priority on the others when filling the calendar
    #
    #'hours' is an integer representing the total mount of work per week dedicated to studying. 
    #If it is too big, the function will end when the calendar is full
    #
    #'max_per_day' is the maximum amount of hours of a subject per day
    #'max_per_day' has priority over 'hours'. So if a subjects wants to be studied more than the max_per_day,
    #it will stop at max_per_day
    #
    #by default, calendar is filled from Monday to Sunday
    #if 'reversed' passed, then calendar is filled Sunday first, Saturday second,...

   

    '''
    #create empty year calendar, cal=[dfweek1,dfweek2,...,dfweek52]
    hoursday=[]
    empty68=[]
    for k in range(700,2400,25):
        hoursday.append(k/100)
    for k in range(0,68):
        empty68.append('')  
    df=pd.DataFrame({'Monday':empty68,'Tuesday':empty68,'Wednesday':empty68,'Thursday':empty68,'Friday':empty68,'Saturday':empty68,'Sunday':empty68}, index=hoursday)
    for i in range(0,1):
        cal.append(df)
    '''
    
    
    #changes order of priority if 'reversed' is plugged
    if order=='reversed':
        calendar=calendar[calendar.columns[::-1]]
        
        

    #creates cal as a list and fills cal with weeks as dataframes
    cal=[]
    for k in range(0,1): #change 1 to 52 when we will have a year calendar
        cal.append(calendar)



    #create 'counthours', wich is a list containing numer of hours in each subject
    #temp is an array containing [[sub1,coeff,#hours],[sub2,coeff,#hours],...]
    temp=[x[:] for x in subjects]
    n=len(temp) #n represents total amount of subjects
    counthours=[]
    for k in range(0,n):
        temp[k].append(((((temp[k][1]*hours)*10)//5)*5/10))
        counthours.append(temp[k][2])
        print(counthours)
        
    #creates calendar for students, by iterating first through subject, then week, then empty cells to fill
    for subj in range(0,n): #iterating on subject
        for week in range (0,len(cal)): #iterating over weeks
            for col in cal[week].loc('Monday','Tuesday').columns: #iterating on days
                for ind in cal[week].index: #iterating on hours
                    try:
                        if cal[week].groupby([col]).size()[temp[subj][0]]<max_per_day*2:
                            if counthours[subj]>0:
                                if cal[week].loc[ind,col]=='':
                                    cal[week].loc[ind,col]=temp[subj][0]
                                    counthours[subj]=counthours[subj]-0.5 #emptying hours
                                    #break
                                    #print(counthours)
                    except KeyError:
                         if counthours[subj]>0:
                            if cal[week].loc[ind,col]=='':
                                cal[week].loc[ind,col]=temp[subj][0]
                                counthours[subj]=counthours[subj]-0.5 #emptying hours

    #'''
    print(counthours)
    
    
    #empties calendar from strings that are not of the subject, by creating 'subjonly', a list containing each cubject,
    #and erasing all the strings that are not in the list
    subjonly=[]
    for i in range(0,len(subjects)):
        subjonly.append(subjects[i][0])
        
    for week in range (0,len(cal)): #iterating over weeks
            for col in cal[week].columns: #iterating on days
                for ind in cal[week].index: #iterating on hours
                        if (cal[week].loc[ind,col] in subjonly)==False:
                            cal[week].loc[ind,col]=''
                    
    #reverses back the order of days of week to get monday first, tuesday second,...                
    if order=='reversed':
        for k in range(0,len(cal)):
            cal[k]=cal[k][cal[k].columns[::-1]]
    
    return cal[0]




#%% converts empty cells of df to empty string
import math 
def nan_to_str(x):
    try:
        if math.isnan(x)==True:
            x=''
            return x
    except Exception:
        return x
def clean_cal(x):
    calen=pd.read_excel(x,index_col=0)
    for col in calen.columns:
        calen[col]=calen[col].apply(nan_to_str)
    return calen
    
    
    
#%% new cell
arg_ex=[['maths',0.5],['physics',0.2],['geography',0.2],['English',0.1]]
cal=fill_calendar_for_students(clean_cal('template_calendar.xlsx'),arg_ex,23,2,'reversed')

cal.to_excel('cal.xlsx')

cal2bis=fill_calendar_for_students(clean_cal('template_calendar.xlsx'),arg_ex,20,2)
#cal2.to_excel('cal2.xlsx')

#%%

cal2bis=fill_calendar_for_students(clean_cal('template_calendar.xlsx'),arg_ex,20,2)



#%% debug test

for x in range(0,6):
    print(x)


#%%calendar per hour
def mfill_calendar_for_students_hour(calendar,subjects,hours,max_per_day,order='normal'):
    #calendar must be an excel calendar with rows as hours, and columns as days of the week
    #
    #'subjects' is a tuple containing [subject,coeff between 0 and 1] for each subject, 
    #example:[['maths',0.7],['physics',0.1],['geography',0.2],['English',0.1]]
    #the coefficients must add-up to 1 in order to have the correct amount of total hours (see next argument)
    #the first subject will have priority on the others when filling the calendar
    #
    #'hours' is an integer representing the total mount of work per week dedicated to studying. 
    #If it is too big, the function will end when the calendar is full
    #
    #'max_per_day' is the maximum amount of hours of a subject per day
    #'max_per_day' has priority over 'hours'. So if a subjects wants to be studied more than the max_per_day,
    #it will stop at max_per_day
    #
    #by default, calendar is filled from Monday to Sunday
    #if 'reversed' passed, then calendar is filled Sunday first, Saturday second,...

   

    '''
    #create empty year calendar, cal=[dfweek1,dfweek2,...,dfweek52]
    hoursday=[]
    empty68=[]
    for k in range(700,2400,25):
        hoursday.append(k/100)
    for k in range(0,68):
        empty68.append('')  
    df=pd.DataFrame({'Monday':empty68,'Tuesday':empty68,'Wednesday':empty68,'Thursday':empty68,'Friday':empty68,'Saturday':empty68,'Sunday':empty68}, index=hoursday)
    for i in range(0,1):
        cal.append(df)
    '''
    
    
    #changes order of priority if 'reversed' is plugged
    if order=='reversed':
        calendar=calendar[calendar.columns[::-1]]
        
        

    #creates cal as a list and fills cal with weeks as dataframes
    cal=[]
    for k in range(0,1): #change 1 to 52 when we will have a year calendar
        cal.append(calendar)



    #create 'counthours', wich is a list containing numer of hours in each subject
    #temp is an array containing [[sub1,coeff,#hours],[sub2,coeff,#hours],...]
    temp=[x[:] for x in subjects]
    n=len(temp) #n represents total amount of subjects
    counthours=[]
    for k in range(0,n):
        temp[k].append(((((temp[k][1]*hours)//1))))
        counthours.append(temp[k][2])
        print(counthours)
        
    #creates calendar for students, by iterating first through subject, then week,
    #then empty cells to fill, first column, next day
    for subj in range(0,n): #iterating on subject
        for week in range (0,len(cal)): #iterating over weeks
            for ind in cal[week].index: #iterating on hours
                for col in cal[week].columns: #iterating on days
                    try:
                        if cal[week].groupby([col]).size()[temp[subj][0]]<max_per_day:
                            if counthours[subj]>0:
                                if cal[week].loc[ind,col]=='':
                                    cal[week].loc[ind,col]=temp[subj][0]
                                    counthours[subj]=counthours[subj]-1 #emptying hours
                                    #print(counthours)
                    except KeyError:
                         if counthours[subj]>0:
                            if cal[week].loc[ind,col]=='':
                                cal[week].loc[ind,col]=temp[subj][0]
                                counthours[subj]=counthours[subj]-1 #emptying hours

    #'''
    print(counthours)
    
    
    #empties calendar from strings that are not of the subject, by creating 'subjonly', a list containing each cubject,
    #and erasing all the strings that are not in the list
    subjonly=[]
    for i in range(0,len(subjects)):
        subjonly.append(subjects[i][0])
        
    for week in range (0,len(cal)): #iterating over weeks
            for col in cal[week].columns: #iterating on days
                for ind in cal[week].index: #iterating on hours
                        if (cal[week].loc[ind,col] in subjonly)==False:
                            cal[week].loc[ind,col]=''
                    
    #reverses back the order of days of week to get monday first, tuesday second,...                
    if order=='reversed':
        for k in range(0,len(cal)):
            cal[k]=cal[k][cal[k].columns[::-1]]
    
    return cal[0]


#%%testing fill_calendar_for_students_hour

cal2_hour=fill_calendar_for_students_hour(clean_cal('template_calendar_hour.xlsx'),arg_ex,20,2)
cal2_hour.to_excel('cal2_hour.xlsx')



# %%

# %%
