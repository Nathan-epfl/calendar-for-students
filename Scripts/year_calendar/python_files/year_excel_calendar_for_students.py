#%%

def year_excel_calendar_for_students( calendar_from_student,
                                list_of_df_of_days_for_each_week,
                                list_of_start_and_end_date_each_week,
                                final_calendar_name,
                                order=[[1,2,3],[2,3,1]],
                                delete_original_calendar = False, 
                                run_macro = True,
                                time_unit = 0.5 #cannot be changed yet
                                ):
    '''
    Auxiliary function that creates the xlsm file with more or less the same inputs as "year_calendar_for_students"
    '''

    ############### Filter out the folowwing warning####################
    #  warn(msg)
    #C:\Users\******\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\openpyxl\worksheet\_reader.py:312: UserWarning: Unknown extension is not supported and will be removed
    import warnings
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    ########################################################   

    import pandas as pd
    import win32com.client
    import os



    #we import all functions that are used
    from week_calendar.python_files.secondary_functions_for_week_calendar_for_students import clean_cal
    from year_calendar.python_files.fill_week_of_year_calendar_for_students import put_hours_in_year_calendar, cal_with_subjects_only
    from week_calendar.python_files.set_priority import set_priority,order_hours_df


    

    
    writer = pd.ExcelWriter("examples_of_schedule\\" + final_calendar_name +'.xlsx', engine = 'xlsxwriter')
    workbook  = writer.book
    workbook.filename = str("examples_of_schedule\\" + final_calendar_name) +'.xlsm'

    workbook.add_vba_project('week_calendar\\secondary_files\\vbaProject.bin')

    for week_number in range(len(list_of_df_of_days_for_each_week)):
        # we create two templates of subjects and proportion
        original_cal_from_student_in_pandas = clean_cal(calendar_from_student)#converting calendar from student in pd

        reordered_cal_from_student_in_pandas = set_priority(original_cal_from_student_in_pandas,order)#reordering calendar to fit priority

        
        temp_hour_in_cal_and_remaing_hours = put_hours_in_year_calendar(list_of_df_of_days_for_each_week[week_number],reordered_cal_from_student_in_pandas.drop(['key_0'], axis = 1),time_unit)#2list with subjects integrated in the student's rearanged calendar and remaining hours
        temp_hour_in_cal = temp_hour_in_cal_and_remaing_hours[0]
        remaining_hours = temp_hour_in_cal_and_remaing_hours[1]
        temp_hour_in_cal.insert(0,'key_0',reordered_cal_from_student_in_pandas['key_0'])#inserting the column corresponding to weekdays

        hour_in_cal = order_hours_df(temp_hour_in_cal) #creating final df


        if delete_original_calendar == True:
            cal_with_subjects_only(hour_in_cal,original_cal_from_student_in_pandas).to_excel(writer, sheet_name = list_of_start_and_end_date_each_week[week_number]) #non subject cells from calendar removed
        else:
            hour_in_cal.to_excel(writer, sheet_name = list_of_start_and_end_date_each_week[week_number])


        worksheet = writer.sheets[list_of_start_and_end_date_each_week[week_number]]


        # Add a button tied to a macro in the VBA project.
        worksheet.insert_button('K15', {'macro':   'nice_everything',
                                    'caption': 'Make it nice!',
                                    'width':   120,
                                    'height':  70})
          

    writer.save()
    writer.close()
    os.remove(os.path.abspath("examples_of_schedule\\" + final_calendar_name) + '.xlsx')

        #doesn't work...
    if run_macro == True:
        for week_number in range(len(list_of_df_of_days_for_each_week)):
            xl = win32com.client.Dispatch("Excel.Application")
            worksheet = writer.sheets[list_of_start_and_end_date_each_week[week_number]]
            workbook.active = list_of_start_and_end_date_each_week[week_number]
            writer.save()
            xl.Workbooks.Open(os.path.abspath(workbook.filename))
            xl.Application.Run('\'' + workbook.filename + '\'' + '!Module2.nice_everything')
            xl.Workbooks.Close()


    # return remaining_hours

# %%
