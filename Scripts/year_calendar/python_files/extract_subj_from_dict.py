# %%
from os import chdir,path
import re
file_directory= path.dirname(__file__)
wd = re.findall(".+Scripts",file_directory)[0]
chdir(wd)
# %%



from year_calendar.python_files.IB_subject_class import *


import copy
def extract_subj_from_dict(subjects_chosen = dict ,IA = False):
    '''
    Function that takes a dictionary {<name of subject> : {'HL' : [<options>],'option' : [<options>]}}
    and outputs a dictionnary {<name of subject> : <ib_subject type object >} containing only subjects selected by the student
    '''
    
    ############### Filter out the folowwing warning####################
    #  warn(msg)
    #C:\Users\******\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\openpyxl\worksheet\_reader.py:312: UserWarning: Unknown extension is not supported and will be removed
    import warnings
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    ########################################################   
    
    subjects_extracted = {key : copy.deepcopy(subjects[key]) for key in subjects_chosen.keys()} #extracting every subject of the student from "subjects" dictionnary, defined in IB_subject_class module

    
    for subj_name in subjects_chosen.keys(): #iterating on each subject
        
        ib_subject = subjects_extracted[subj_name] #giving a name for the extracted subject
        one_subj_extracted = pd.concat([ib_subject.syllabus.loc['core']], keys = ['core']) #creating a dataframe with core sections of subject ("concat" used to have the outer index)


        if ib_subject.level == 'HL' : #adding HL lessons to the subject's syllabus if the subject's level  is HL
            
            if ib_subject.choice_on_syllabus['HL'] == 'all':
                
                one_subj_extracted = pd.concat([
                    one_subj_extracted,
                    pd.concat([ib_subject.syllabus.loc['HL']],keys = ['HL'])
                ])
            
            else:
            
                ib_subject.hl_options_chosen = subjects_chosen[subj_name]['HL']
                one_subj_extracted = pd.concat([
                    one_subj_extracted,
                    pd.concat([
                        ib_subject.syllabus.loc['HL'][ib_subject.syllabus.loc['HL']['name_of_section'].isin(ib_subject.hl_options_chosen)]
                    ]
                    ,keys = ['HL'])
                ])

        if ib_subject.choice_on_syllabus['option'] != 0: #ading options to the subject's syllabus
            
            ib_subject.options_chosen = subjects_chosen[subj_name]['option']
            one_subj_extracted = pd.concat([
                one_subj_extracted,
                    pd.concat([ib_subject.syllabus.loc['option'][ib_subject.syllabus.loc['option']['name_of_section'].isin(ib_subject.options_chosen)]],keys = ['option'])
            ])
        
        if IA == True: #adding IA if the student wants to
        
            if ib_subject.choice_on_syllabus['practical_work'] != 0:
        
                practical_works_of_subj = ib_subject.choice_on_syllabus['practical_work']

                one_subj_extracted = pd.concat([
                    one_subj_extracted,
                        pd.concat([ib_subject.syllabus.loc['practical_work'][ib_subject.syllabus.loc['practical_work']['name_of_section'].isin(practical_works_of_subj)]],keys = ['practical_work'])
                ])
        

        subjects_extracted[subj_name].syllabus = one_subj_extracted



    return subjects_extracted

# %%tests
# out_extract_subj_from_dict = extract_subj_from_dict(dict_of_choices_at_end_of_file_ib_subject)
# %%
# out_extract_subj_from_dict["philosophy HL"].syllabus
# %%
