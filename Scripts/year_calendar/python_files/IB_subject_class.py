#%% class IB subjects
import pandas as pd
class ib_subject():
    '''
    An ib_subject object represents all the important information about 
    an IB subject taken by the student (level, weighting, options, ...).
    it has different attributes:
        self.name is the name of the subject
        self.level is the level of the subject
        self.weight is the weighting of the subject (for revisions)
        self.exams is a dictionary containing names and dates of exams
        self.last_exam_date is the date of last exam
        self.syllabus is a pd.df of the syllabus
        self.choice_on_syllabus is a dictionary containgin all the different choices the student made
        self.options_chosen  is a list of options chosen
        self.hl_options_chosen is a list of hl_options chosen
    
    There is one function, "add_exam", which adds exams to the ib_subject object
    '''

    def __init__(self, name_of_sub,level_of_sub = ''):

        self.name = name_of_sub
        self.level = level_of_sub
        self.weight = 1
        self.exams = {}
        self.last_exam_date = pd.to_datetime('19 may 2023')
        self.syllabus = pd.DataFrame()
        self.choice_on_syllabus = {}
        self.options_chosen = []
        self.hl_options_chosen = []

    
    def add_exam(self,name_of_exam,date_of_exam):
        
        if self.exams == {}:
            self.last_exam_date = pd.to_datetime(date_of_exam)

        #adds the exam
        self.exams[name_of_exam]= pd.to_datetime(date_of_exam)

        #updates last exam date
        for some_exam_date in self.exams.values():
    
            if some_exam_date <= pd.to_datetime(date_of_exam):
                self.last_exam_date = pd.to_datetime(date_of_exam)

#%% to get the te docstring of the class:
ib_subject.__doc__


#%% listing every subject, and entering date of end of exams
list_of_all_subjects = ['maths AA_SL', 'maths AA_HL',
                        'maths AI_SL', 'maths AI_HL',
                        'physics SL','physics HL',
                        'chemistry SL','chemistry HL',
                        'biology SL','biology HL',
                        'language A SL', 'language A HL',
                        'geography SL', 'geography HL', 
                        'history SL','history HL',
                        'philosophy SL','philosophy HL',
                        'economics SL', 'economics HL',
                        'business management SL','business management HL']

import pandas as pd
date_of_end_of_exams = pd.to_datetime('19 may 2023')
# %% creating dictionnary of every subject
import re
subjects = {}
for subj in list_of_all_subjects:
    if re.findall('(.+)(?:\s)(?:AA_SL|AA_HL|AI_SL|AI_HL)',subj) == []:
        subjects[subj] = ib_subject(re.findall('(.+)(?:\s)(?:HL|SL)',subj)[0],re.findall('SL|HL',subj)[0])
    else:
        subjects[subj] = ib_subject(re.findall('(.+)(?:\s)(?:AA_SL|AA_HL|AI_SL|AI_HL)',subj)[0],re.findall('(?:[a-z\s]+)([A-Z_]+)',subj)[0])
    
    subjects[subj].syllabus = pd.read_excel('year_calendar\\secondary_files\\IB_syllabus.xlsx',sheet_name = 'IB_' + subjects[subj].name,index_col = [0,1])[['name_of_section','hours_' + subjects[subj].level]]

# %%



#1 is Interdisiplinary subjects
#2 is Sciences subjects
#3 is Studies in language and literature and Language acquisition
#4 is Mathematics
#5 is Individuals and Societies
#6 is The arts

###  ###################################################################  ###
###  ###################################################################  ###
###  ###################################################################  ###
###  ###################################################################  ###
###  ###################################################################  ###
###  ####################                               ################  ###
###  #################### LIST NOT FINISHED NOR UPDATED ################  ###
###  ####################I JUST CHANGED "2022" to "2023"################  ###
     ####################                               ################  ###
     ###################################################################  
###  ###################################################################  ###
###  ###################################################################  ###





             ##
             ##
             ##
             ##
             ##
             ##
             ##
             ##
             ##
             ##
             ##
             ##














###############
###############
             ##
             ##
             ##
###############
###############
##             
##             
##             
###############
###############



#%% creating subjects['physics SL'] instance
subjects['physics SL'].weight = 150
subjects['physics SL'].add_exam('Paper 1','28 april 2023, 1pm')
subjects['physics SL'].add_exam('Paper 2','28 april 2023, 1pm')
subjects['physics SL'].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 1, 'practical_work' : ['IA']}
# print(subjects['physics SL'].syllabus)

#%% creating subjects['physics HL'] instance
subjects['physics HL'].weight = 240
subjects['physics HL'].add_exam('Paper 1','28 april 2023, 1pm')
subjects['physics HL'].add_exam('Paper 2','28 april 2023, 1pm')
subjects['physics HL'].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 1, 'practical_work' : ['IA']}




#######################################################################





#%% creating subjects['chemistry SL'] instance
subj = 'chemistry SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','18 may 2023, 8am')
subjects[subj].add_exam('Paper 2','18 may 2023, 8:45am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 1, 'practical_work' : ['IA']}



#%% creating subjects['chemistry HL'] instance
subj = 'chemistry HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','18 may 2023, 8am')
subjects[subj].add_exam('Paper 2','18 may 2023, 9am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 1, 'practical_work' : ['IA']}




#######################################################################





#%%creating subjects['biology SL'] instance
subj = 'biology SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','11 may 2023, 8am')
subjects[subj].add_exam('Paper 2','11 may 2023, 8:45am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 1, 'practical_work' : ['IA']}



#%% creating subjects['chemistry HL'] instance
subj = 'biology HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','11 may 2023, 8am')
subjects[subj].add_exam('Paper 2','11 may 2023, 9am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 1, 'practical_work' : ['IA']}









###############
###############
             ##
             ##
             ##
###############
###############
             ##
             ##
             ##
###############
###############



#%%creating subjects['biology SL'] instance
subj = 'language A SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','4 may 2023, 8am')
subjects[subj].add_exam('Paper 2','4 may 2023, 8:45am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 1, 'practical_work' : []}



#%% creating subjects['chemistry HL'] instance
subj = 'language A HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','4 may 2023, 8am')
subjects[subj].add_exam('Paper 2','4 may 2023, 9am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 1, 'practical_work' : []}











##           ##
##           ##
##           ##
##           ##
##           ##
###############
###############
             ##
             ##
             ##
             ##
             ##


#%% creating subjects['maths AA_SL'] instance
subj = 'maths AA_SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','6 may 2023, 1pm')
subjects[subj].add_exam('Paper 2','9 may 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 0, 'practical_work' : ['IA']}
# print(subjects['maths AA_SL'].syllabus)

#%% creating subjects['maths AA_HL'] instance
subj = 'maths AA_HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','6 may 2023, 1pm')
subjects[subj].add_exam('Paper 2','9 may 2023, 8am')
subjects[subj].add_exam('Paper 3','12 may 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 0, 'practical_work' : ['IA']}

#%% creating subjects['maths AI_SL'] instance
subj = 'maths AI_SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','6 may 2023, 1pm')
subjects[subj].add_exam('Paper 2','9 may 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 0, 'practical_work' : ['IA']}

#%% creating subjects['maths AI_HL'] instance
subj = 'maths AI_HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','6 may 2023, 1pm')
subjects[subj].add_exam('Paper 2','9 may 2023, 8am')
subjects[subj].add_exam('Paper 3','12 may 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 0, 'practical_work' : ['IA']}









###############
###############
##             
##             
##             
###############
###############
             ##
             ##
             ##
###############
###############

#%% 
subjects['geography SL'].weight = 150
subjects['geography SL'].add_exam('Paper 1','13 may 2023, 1pm')
subjects['geography SL'].add_exam('Paper 2','16 may 2023, 8am')
subjects['geography SL'].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 2, 'practical_work' : ['IA']}


#%% 
subjects['geography HL'].weight = 240
subjects['geography HL'].add_exam('Paper 1','13 may 2023, 1pm')
subjects['geography HL'].add_exam('Paper 2','16 may 2023, 8am')
subjects['geography HL'].add_exam('Paper 3','16 may 2023, 9am')
subjects['geography HL'].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 3, 'practical_work' : ['IA']}






#######################################################################







#%% 
subjects['history SL'].weight = 150
subjects['history SL'].add_exam('Paper 1','4 may 2023, 1pm')
subjects['history SL'].add_exam('Paper 2','4 may 2023, 2pm')
subjects['history SL'].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 2, 'practical_work' : ['IA']}


#%% 
subjects['history HL'].weight = 240
subjects['history HL'].add_exam('Paper 1','4 may 2023, 1pm')
subjects['history HL'].add_exam('Paper 2','4 may 2023, 2pm')
subjects['history HL'].add_exam('Paper 3','5 may 2023, 8am')
subjects['history HL'].choice_on_syllabus = {'core' : 'all','HL' : 1, 'option' : 2, 'practical_work' : ['IA']}

# print(subjects['history HL'].syllabus)





#######################################################################






#%% 
subjects['philosophy SL'].weight = 150
subjects['philosophy SL'].add_exam('Paper 1','13 may 2023, 2pm')
subjects['philosophy SL'].add_exam('Paper 2','16 may 2023, 9am')
subjects['philosophy SL'].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 1, 'practical_work' : ['IA']}


#%% 
subjects['philosophy HL'].weight = 240
subjects['philosophy HL'].add_exam('Paper 1','13 may 2023, 2pm')
subjects['philosophy HL'].add_exam('Paper 2','16 may 2023, 9am')
subjects['philosophy HL'].add_exam('Paper 3','16 may 2023, 10am')
subjects['philosophy HL'].choice_on_syllabus = {'core' : 'all','HL' : 'all', 'option' : 2, 'practical_work' : ['IA']}



#######################################################################

#%% creating subjects['economics SL'] instance
subj = 'economics SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','9 may 2023, 1pm')
subjects[subj].add_exam('Paper 2','10 may 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 0, 'practical_work' : ['IA']}



#%% creating subjects['economics HL'] instance
subj = 'economics HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','9 may 2023, 1pm')
subjects[subj].add_exam('Paper 2','10 may 2023, 8am')
subjects[subj].add_exam('Paper 2','10 may 2023, 8:45am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 0, 'practical_work' : ['IA']}




######################################################################


#%% creating subjects['business_management SL'] instance
subj = 'business management SL'
subjects[subj].weight = 150
subjects[subj].add_exam('Paper 1','28 april 2023, 1pm')
subjects[subj].add_exam('Paper 2','29 april 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 0, 'practical_work' : ['IA']}



#%% creating subjects['economics HL'] instance
subj = 'business management HL'
subjects[subj].weight = 240
subjects[subj].add_exam('Paper 1','28 april 2023, 1pm')
subjects[subj].add_exam('Paper 2','29 april 2023, 8am')
subjects[subj].choice_on_syllabus = {'core' : 'all','HL' : 0, 'option' : 0, 'practical_work' : ['IA']}










###############
###############
##             
##             
##             
###############
###############
##           ##
##           ##
##           ##
###############
###############




#%%
# for subj in list_of_all_subjects:
#     print(subjects[subj].name,subjects[subj].level,subjects[subj].weight)
#     print(subjects[subj].syllabus)



#%%
subjects['maths AA_SL'].syllabus




#%%
subjects["philosophy HL"].syllabus















# %%
dict_of_choices_at_end_of_file_ib_subject = {
    'maths AA_SL': {},
    'physics HL': {'option' : ['Astrophysics']},
    'chemistry HL': {'option' : ['Energy']},
    'biology HL': {'option' : ['Human physiology']},
    'geography SL' : {'HL' : 0, 'option':['Extreme environments', 'Leisure, sport and tourism']},
    'history HL' : {'HL' : ['History of the Americas'],'option' : ['Society and economy (750–1400)','Causes and effects of wars (750–1500)','Dynasties and rulers (750–1500)']},
    'philosophy HL' : {'option' : ['Ethics','Philosophy of science']}
}
# %%

# %%
subjects['chemistry HL'].last_exam_date
# %%

# %%
