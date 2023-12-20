#%% function that redistributes hours to have a whole number and distributed according to the coefficients, and then rounds to the "time_unit" entered
import numpy as np
import secondary_functions_for_week_calendar_for_students as sec_fun
import pandas as pd
def redistribute_hours(df,time_unit):
    #df must be a dataframe coming from the function 'count_hours_each_day'
    total_hours=df.drop(index='coeff').values.sum()
    df_without_coeff=df.drop(labels='coeff', axis=0).copy()
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

# %%
