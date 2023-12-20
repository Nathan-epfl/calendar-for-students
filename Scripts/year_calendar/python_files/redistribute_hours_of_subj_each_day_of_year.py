#%%

import year_calendar.python_files.secondary_func_of_year_cal_for_students as sec_fun
import pandas as pd
import datetime
from year_calendar.python_files.IB_subject_class import *

def redistribute_hours_each_day_of_year(df_of_subj_and_hours_each_day = pd.core.frame.DataFrame, time_unit = float):
    '''
    Function that take a dataframe output from "transform_coeff_to_hours" function, 
    a time unit representing the rounding
    and outputs redistributed version of the dataframe, rounded up to "time_unit" variable
    '''

    original_df_copy = df_of_subj_and_hours_each_day.copy()
    original_df_copy_with_total_hours = original_df_copy.copy()
    original_df_copy_with_total_hours.loc['hours_per_day'] = original_df_copy_with_total_hours.sum(axis = 0)
    original_df_copy_with_total_hours['hours_per_subj'] = original_df_copy_with_total_hours.sum(axis = 1)
    # print(original_df_copy_with_total_hours)

    def objective_func(subj,day):
        expected_hours_per_subj = original_df_copy_with_total_hours.loc[subj,'hours_per_subj']
        computed_hours_per_subj = sum(original_df_copy.loc[subj])


        expected_hours_per_day = original_df_copy_with_total_hours.loc['hours_per_day',day]
        computed_hours_per_day = sum(original_df_copy[day])

        return(computed_hours_per_day - expected_hours_per_day) / len(original_df_copy.index) + 5 * (computed_hours_per_subj - expected_hours_per_subj) / len(original_df_copy.columns)


    # ##########################old method#######################
    # for subj in original_df_copy.index:
    #     for day in original_df_copy:
    #         if (0 < original_df_copy.loc[subj,day] < 1):
    #             if objective_func(subj,day) <= 0:
    #                 original_df_copy.loc[subj,day] = 1
    #             else:
    #                 original_df_copy.loc[subj,day] = 0
    #         else:
    #             if objective_func(subj,day) <= 0:
    #                 original_df_copy.loc[subj,day] = sec_fun.round_up_down(original_df_copy.loc[subj,day],time_unit,'up')
    #             else:
    #                 original_df_copy.loc[subj,day] = sec_fun.round_up_down(original_df_copy.loc[subj,day],time_unit,'down')
    # #################################################################

    ###############new method#####################################
    for day in original_df_copy.columns:
        list_of_sub_in_day_sorted_by_coeff = original_df_copy[day].sort_values().index
        for subj in list_of_sub_in_day_sorted_by_coeff:
            if datetime.timedelta(days = 1) <= subjects[subj].last_exam_date.date() - day.date() <= datetime.timedelta(days = 2):
                # print(day,subj)
                original_df_copy.loc[subj,day] = sec_fun.round_up_down(original_df_copy.loc[subj,day],time_unit,'up')
            elif (0 < original_df_copy.loc[subj,day] < 1):
                if objective_func(subj,day) <= 0:
                    original_df_copy.loc[subj,day] = 1
                else:
                    original_df_copy.loc[subj,day] = 0
            else:
                if objective_func(subj,day) <= 0:
                    original_df_copy.loc[subj,day] = sec_fun.round_up_down(original_df_copy.loc[subj,day],time_unit,'up')
                else:
                    original_df_copy.loc[subj,day] = sec_fun.round_up_down(original_df_copy.loc[subj,day],time_unit,'down')
    ###############################################################

    df_final = original_df_copy
    
    #########df not used, but here to check accuracy
    df_expected_vs_computed = df_final.copy()
    df_expected_vs_computed.loc['total_per_day_computed'] = df_expected_vs_computed.sum(axis = 0)
    df_expected_vs_computed['total_per_subj_computed'] = df_expected_vs_computed.sum(axis = 1)
    df_expected_vs_computed['total_per_subj_expected'] = original_df_copy_with_total_hours['hours_per_subj']
    ############

    return df_final


#%%
# out_redistribute_hours_each_day_of_year = redistribute_hours_each_day_of_year(out_transform_coeff_to_hours,0.5)

# %%
# out_redistribute_hours_each_day_of_year

