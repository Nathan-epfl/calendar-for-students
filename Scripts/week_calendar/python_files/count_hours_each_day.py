#%%
'''
count_hours_each_day takes subjects, hours in total, coeff per day, 
and outputs dataframe with days as columns, subjects as rows,
each cell is the amount of hours of each subject that day,
and the final row of the dataframe is a copy of coef_per_day list.
'''




import pandas as pd


#'subjects_and_coeffs' is a list of 2-lists containing name of subject and coefficient of the subject 
#'hours_of work' is the amount of hours the students wants to work
#'coeff_per_day' is a 7-list with a coefficient for each day of the week, starting with Monday
def count_hours_each_day(subjects_and_coeffs = list, hours_in_total = int, coeff_per_day = [1]*7):

    #normalising the coefficients of 'subjects_and_coeffs'
    subjects_and_coeffs_copy=subjects_and_coeffs.copy()
    sum_of_sub_coeffs=0
    for num_of_sub in range(len(subjects_and_coeffs)):
        sum_of_sub_coeffs=sum_of_sub_coeffs + subjects_and_coeffs[num_of_sub][1]

    for num_of_sub in range(len(subjects_and_coeffs)):
        subjects_and_coeffs_copy[num_of_sub][1]=subjects_and_coeffs[num_of_sub][1]/sum_of_sub_coeffs
    
    #creating a list of subjects only, reused later
    subjects=[subjects_and_coeffs_copy[n][0] for n in range(len(subjects_and_coeffs_copy))]
    
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
    hours_per_subject=[
         subjects_and_coeffs_copy[n][1]*hours_in_total for n in range(len(subjects_and_coeffs_copy))
    ]
    hours_per_subject.append(0)
    
    
    #including it to the dataframe
    df_hours_each_day['total hours']=hours_per_subject
    
    #filling 'df_hours_each_day' with corresponding hours
    for day in df_hours_each_day.drop(labels='total hours', axis=1).columns: #iterating on days
        for sub in df_hours_each_day.drop(labels='coeff', axis=0).index: #iterating on subjects
            df_hours_each_day.loc[sub,day]=df_hours_each_day.loc[sub,'total hours']*\
                                            df_hours_each_day.loc['coeff',day]/\
                                            sum_of_coeffs

    return df_hours_each_day.drop(labels='total hours',axis=1)# axis 1 drops columns, 0 will drop rows that match index value in labels



#%% test
# out_count_hours_each_day=count_hours_each_day([['phys',2],['math',1]],30,[1,1,1,1,1,2,2])
# %%
# out_count_hours_each_day
# %%
