#%% set working directory to "scripts"
from os import chdir,path
import re
file_directory = path.dirname(__file__)
wd = re.findall(".+Scripts",file_directory)[0]
chdir(wd)

#%% testing final function

'''
'calendar_from_student' is the name of the xlsx ('.xlsx' included) file containing the student's schedule
'subj_with_coeff is a list of 2-lists containing name of subject and coefficient of the subject 
'hours_of work' is the (approximate) amount of hours the students wants to work
'coeff_per_day' is a 7-list with a coefficient for each day of the week, starting with monday
'time_unit' is the interval of time in the calendar. It must correspond with 'calendar_from_student'!
if True is given at the end, then the final calendar will have deleted the 'calendar_from_student' part
'''

from week_calendar.python_files.week_calendar_for_students import week_calendar_for_students
final_df_pd = week_calendar_for_students(
    'week_calendar\\excel_templates\\template_calendar.xlsx', #name of the xlsx ('.xlsx' included) file containing the student's schedule
    [['Physics',2],['geography',3],['english',2],['IA',1]], # list of 2-lists containing name of subject and coefficient of the subject 
    25, #the (approximate) amount of hours the students wants to work
    'testing 25_07_22', #name of output file
    [1,1,1,2,6,4,4], #7-list with a coefficient for each day of the week, starting with monday
    time_unit = 0.5, #the interval of time in the calendar. It must correspond with the original calendar!
    order = [[3,2,1],[2,1,3]],
    delete_original_calendar = True, #False by default, if True is given at the end, then the final calendar will have deleted the 'calendar_from_student' part
    run_macro = False) #True by default. If "False" given, then the excel doesn't run the macro to make the calendar nice, and the user can apply small modifications

# %%
