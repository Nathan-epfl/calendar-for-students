#%% 
##########community modules##########
import os
import pandas as pd
import numpy as np
############################



####local modules#######
# setting cwd as main folder
wd=os.getcwd()
if "\\week_calendar\\python_files" in wd:
    os.chdir(wd.replace('\\week_calendar\\python_files', ''))

import week_calendar.python_files.secondary_functions_for_week_calendar_for_students as sec_fun
########################



'''
function that rounds up the hours per day up to "time_unit" argument 
and redistributes the hours to fit best the expected hours per day and  expected hours per subject
'''


def redistribute_hours_with_objective_func(df = pd.core.frame.DataFrame, time_unit = float):
    #df must be a dataframe comming from the function 'count_hours_each_day'
    


    df_copy=df.copy()
    total_hours=df.drop(index='coeff').values.sum()
    df_copy['total_per_subject']=df_copy.apply(np.sum,axis=1)
    df_copy=df_copy.rename(index={'coeff':'expected_coeff'})
    
    df_without_coeff=df.drop(index='coeff').copy()

    ###########redistributing#########################################
    # moving the values of cells less than 0.75 (45 minutes) to another cell of same row that is also less than 0.75
    for sub in df_without_coeff.index: #iterating on subjects
        
        for day_to_empty in df_without_coeff.columns: #iterating on days to empty
            
            if (0 < df_without_coeff.loc[sub,day_to_empty] < 0.75):
                
                for day_to_fill in df_without_coeff.drop(columns=day_to_empty).columns:
                        
                        if (df_without_coeff.loc[sub,day_to_empty] <= df_without_coeff.loc[sub,day_to_fill] < 1):
                            
                            df_without_coeff.loc[sub,day_to_fill]+=df_without_coeff.loc[sub,day_to_empty]
                            df_without_coeff.loc[sub,day_to_empty]=0
                            
                            if (0 < df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_fill] < 0.75):
                                
                                df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_empty]+=\
                                df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_fill]

                                df_without_coeff.loc[sec_fun.next_row(sub,df_without_coeff),day_to_fill]=0
                            break
    ###########################################################################




    #############333333# updating df#################
    df_final = df_without_coeff.copy()
    df_final.loc['coeff'] = df_final.iloc[:,:].sum().T
    df_final.loc['coeff'] = df_final.loc['coeff'].apply(lambda x: x*np.sum(df.loc['coeff'])/total_hours)
    df_final.loc['expected_coeff'] = df.loc['coeff']
    #################################################



    ######## objective function definition####################
    #Objective function gives a weight of 1 to errors for a subject's hours, and weight 2 for a day's hours
    def objective_func(sub,day):

        # tuning parameters
        sub_weight = 1
        day_weight = 2

        diff_of_day_coeff_normalized = df_copy.loc['expected_coeff',day] - df_final.loc['coeff',day]

        diff_of_hour_subj_normalized = df_copy.loc[sub,'total_per_subject'] - df_final.loc[sub].values.sum()

        return  sub_weight * diff_of_day_coeff_normalized + day_weight * diff_of_hour_subj_normalized
    ##########################################################
    


    
    ################ rounding up or down depending on the objective function value #####################3
    for sub in df_final.drop(['coeff','expected_coeff']).index:

        for day in df_final.columns:

            if objective_func(sub,day) > 0: #if expected - given > 0, we round up

                df_final.loc[sub,day] = sec_fun.round_up_down(df_final.loc[sub,day],time_unit,'up')
                
            else: #if expected - given > 0, we round down

                df_final.loc[sub,day]=sec_fun.round_up_down(df_final.loc[sub,day],time_unit,'down')

            df_final.loc['coeff'] = df_final.drop(index=['coeff','expected_coeff']).iloc[:,:].sum().T
            df_final.loc['coeff'] = df_final.loc['coeff'].apply(lambda x: x * np.sum(df.loc['coeff']) / total_hours)
    ##########################################################



    ############# updating and cleaning df######################            
    df_final['total_per_subject'] = df_final.apply(np.sum,axis=1)
    df_final.loc['coeff','total_per_subject'] = df_final.drop(index=['coeff','expected_coeff'])['total_per_subject'].sum()
    df_final = round(df_final,2)
    df_final = df_final.drop('total_per_subject',axis=1)
    ######################################################



    return df_final
# %%
# out_redistribute_hours_with_objective_func = redistribute_hours_with_objective_func(out_count_hours_each_day,1)
# %%
# out_redistribute_hours_with_objective_func
# %%
