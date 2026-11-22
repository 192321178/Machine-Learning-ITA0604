import pandas as pd

students = pd.DataFrame({'name': ['A', 'B', 'C'], 'marks': [80, 90, 70]})
new_student = pd.DataFrame({'name': ['D'], 'marks': [85]})
combined = pd.concat([students, new_student], ignore_index=True)
print('Concatenated:')
print(combined.to_string(index=False))

grades = pd.DataFrame({'name': ['A', 'B', 'C'], 'grade': ['A', 'A+', 'B']})
merged = pd.merge(students, grades, on='name', how='inner')
print('Merged:')
print(merged.to_string(index=False))
