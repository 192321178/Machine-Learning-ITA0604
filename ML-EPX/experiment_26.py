case_library = [
    {'symptoms': {'fever': True, 'cough': True,  'fatigue': False}, 'diagnosis': 'Flu'},
    {'symptoms': {'fever': False, 'cough': True, 'fatigue': True},  'diagnosis': 'Cold'},
    {'symptoms': {'fever': True,  'cough': False,'fatigue': True},  'diagnosis': 'Viral Infection'},
]

def similarity(new_case, old_case):
    return sum(new_case[key] == old_case.get(key) for key in new_case)

new_symptoms = {'fever': True, 'cough': True, 'fatigue': False}
best_case = max(case_library, key=lambda case: similarity(new_symptoms, case['symptoms']))
print('Retrieved diagnosis (Reuse):', best_case['diagnosis'])
case_library.append({'symptoms': new_symptoms, 'diagnosis': best_case['diagnosis']})
print('Case library size after Retain:', len(case_library))
