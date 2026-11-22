from pathlib import Path
import pandas as pd

Path('students.csv').write_text(
    'name,marks,class\nA,78,I\nB,45,II\n', encoding='utf-8'
)
df = pd.read_csv('students.csv')
print('Loaded data:')
print(df.to_string(index=False))

df['pass'] = df['marks'] >= 50
df.to_csv('students_processed.csv', index=False)
print('Processed data:')
print(df.to_string(index=False))
