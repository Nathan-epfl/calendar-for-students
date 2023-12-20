#%% setting priority of filling of a dataframe
import pandas as pd
def set_priority(schedule = pd.core.frame.DataFrame , order=[[1,2,3],[2,1,3]]):


    '''
    takes a student's schedule in pandas and swaps hours to set priority on a given part of the day
    
    morning is till morn_end:00
    afternoon is till 18:30
    evening is till 23:30 pm

    order is set using the following table ([[week day priority],[weekend priority]])
    1____<=>____morning_______
    2____<=>____afternoon_____
    3____<=>____evening_______

    by default we have [[1,2,3],[2,1,3]],
    i.e. the student works morning first, afternoon second and evening third in week days, 
    and afternoon-morning-evening in weekends
    '''

    morn_end = 13 
    aft_end = 18.5

    #we first deal with the case where nothing is changed
    if order == [[1,2,3],[1,2,3]]:
        schedule.insert(0, 'key_0', schedule.index) #we add an extra column that's a copy of the index, because it is used in next functions
        return schedule
    


    ##############splitting dfs##################
    sched_copy = schedule.copy() #creating a copy of schedule
    sched_weekdays = sched_copy[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']] #extracting weekdays
    sched_weekend = sched_copy[['Saturday', 'Sunday']] #extracting weekend

    sched_weekdays_morn = sched_weekdays[sched_weekdays.index <= morn_end] #extracting weekdays mornings
    sched_weekdays_aft = sched_weekdays[(morn_end < sched_weekdays.index) &\
                                                 (sched_weekdays.index <= aft_end)] #extracting weekdays afternoons
    sched_weekdays_eve = sched_weekdays[aft_end < sched_weekdays.index] #extracting weekdays evenings

    sched_weekdays_splitted_list = [sched_weekdays_morn, sched_weekdays_aft, sched_weekdays_eve] #creating a list containing each weekdays subdf from morining to evening


    sched_weekend_morn = sched_weekend[sched_weekend.index<=morn_end] #extracting weekend mornings
    sched_weekend_aft = sched_weekend[(morn_end < sched_weekend.index) &\
                                                     (sched_weekend.index <= aft_end)] #extracting weekend adternoons
    sched_weekend_eve = sched_weekend[aft_end < sched_weekend.index] #extracting weekend evenings
    
    sched_weekend_splitted_list = [sched_weekend_morn, sched_weekend_aft, sched_weekend_eve] #creating a list containing each weekend subdf from morining to evening
    #############################################################################

    
    #creating weekdays df with order put according to priority (the -1 is due to 1,2,3 priority order)
    sched_rearranged_weekdays = pd.concat([
                                sched_weekdays_splitted_list[int(order[0][0]-1)],\
                                sched_weekdays_splitted_list[int(order[0][1]-1)],\
                                sched_weekdays_splitted_list[int(order[0][2]-1)]
                                ])

    
    
    #creating weekdend df with order put according to priority (the -1 is due to 1,2,3 priority order)
    sched_rearranged_weekend = pd.concat([
                                sched_weekend_splitted_list[int(order[1][0]-1)],\
                                sched_weekend_splitted_list[int(order[1][1]-1)],\
                                sched_weekend_splitted_list[int(order[1][2]-1)]
                                ])
    
    
    #merging weekdays and weekend
    sched_rearranged = pd.merge(
        sched_rearranged_weekdays,
        sched_rearranged_weekend,
        left_index=True,
        right_on = sched_rearranged_weekdays.index
    )

    return sched_rearranged

#%%
def order_hours_df(filled_pd_not_in_order):
    order_weekdays=filled_pd_not_in_order[['key_0','Monday','Tuesday','Wednesday','Thursday','Friday']].set_index('key_0') #reseting weekdays to put hours chronologically
    order_weekdays.index.name=None

    order_weekend=filled_pd_not_in_order[['Saturday','Sunday']] #reseting weekend to put hours chronologically
    order_weekdays.index.name=None

    ordered_df=order_weekdays.join(order_weekend).sort_index()
    return ordered_df


# %%
# out_set_priority = set_priority(out_clean_cal)
# %%
