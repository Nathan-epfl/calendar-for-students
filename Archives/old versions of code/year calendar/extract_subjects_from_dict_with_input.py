#%% extract subjects from subjects dictionnary in IB_subject_class.py
from IB_subject_class import *
import copy
def extrac_subj_from_dict_with_input():
    subjects_copy = copy.deepcopy(subjects)
    subjects_extracted = {}
    for number in ['first','second']:
        subj_name = input('choose a ' + number + ' subject')
        ib_subject = subjects_copy[subj_name]
        subjects_extracted[subj_name] = ib_subject
        
        if ib_subject.choice_on_syllabus['option'] != 0:
            options_of_subj = []


            for i in range(ib_subject.choice_on_syllabus['option']):
                options_of_subj.append(input('what\'s your option number ' + str(i + 1) + ' in ' + ib_subject.name + ' ?'))


            subjects_extracted[subj_name].syllabus = pd.concat(
                [ib_subject.syllabus.loc['core'],
                    ib_subject.syllabus.loc['option'][ib_subject.syllabus.loc['option']['name_of_section'].isin(options_of_subj)]]
            )
        
        
        else :
            subj_extracted = ib_subject.syllabus.loc['core']
        print(subj_extracted)
    return subjects_extracted

# %%
x = extrac_subj_from_dict_with_input()
# %%
x['maths AA_SL'].choice_on_syllabus

# %%
example_of_student_curriculum['physics SL'].exams
# %%
