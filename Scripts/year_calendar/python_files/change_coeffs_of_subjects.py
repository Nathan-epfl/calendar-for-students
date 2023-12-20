#%% change_coeffs_of_subjects

def change_coeffs_of_subjects(subjects = dict, coeff_per_subject = dict):
    '''
    function thak takes a dictionary of ib_subject objects and a dictionary of coeffs per subjects
    and outputs a dictionary of ib_subjects with coefficient changed
    '''
    import copy
    subjects_changed = copy.deepcopy(subjects)

    for subj in subjects.keys():
        subjects_changed[subj].syllabus['hours_'+ subjects[subj].level] = \
            subjects_changed[subj].syllabus['hours_' + subjects[subj].level].apply(
            lambda x : x * coeff_per_subject[subj]
               )
        subjects_changed[subj].weight = coeff_per_subject[subj]
    
    return subjects_changed


#%% test

# out_change_coeffs_of_subjects = change_coeffs_of_subjects(out_extract_subj_from_dict,
    {'maths AA_SL': 1,'physics HL': 4,'chemistry HL' : 1, 'biology HL' : 1, 'geography SL' : 1,'history HL' : 1,'philosophy HL' : 1 }
# )
# %%
# out_change_coeffs_of_subjects['physics HL'].weight


# %%
