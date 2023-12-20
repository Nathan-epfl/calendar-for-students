#%% creating year calendar for students
from os import chdir, getcwd,path
import re
wd= path.dirname(__file__)
main_dir=re.findall('(.*)(?:\\\year_calendar)',wd)[0]
chdir( main_dir+'\\week_calendar')
from week_calendar_for_students_no_excel import week_calendar_for_students_no_excel





import datetime
import pandas as pd
start_time = datetime.datetime.now()

with pd.ExcelWriter("portfolio.xlsx") as writer:
    for i in range(4):
                week_calendar_for_students_no_excel(
                main_dir+'\\week_calendar\\excel_templates\\template_calendar.xlsx', #name of the xlsx ('.xlsx' included) file containing the student's schedule
                [['nuth nuuuuuuuth',2],['geography',3],['english',2],['IA',1]], # list of 2-lists containing name of subject and coefficient of the subject 
                25, #the (approximate) amount of hours the students wants to work
                [1,1,1,2,1,4,4], #7-list with a coefficient for each day of the week, starting with monday
                time_unit=0.5+i/52, #the interval of time in the calendar. It must correspond with the original calendar!
                order=[[2,3,1],[2,1,3]]
                ).to_excel(writer, sheet_name="week "+str(i))


end_time = datetime.datetime.now()
print(end_time - start_time)
chdir(wd)
from IB_subject_class import *
# print(chdir)

#%% testing stuff
physics_SL.exams
maths_AA_SL.syllabus

# %%
