import numpy as np
import pandas as pd

df = pd.DataFrame({
    'name': ['A', 'B', 'B', 'C', None],
    'marks': [78, np.nan, 85, 92, 66]
})
print('Missing values:')
print(df.isna().sum().to_string())

filled = df.fillna({'name': 'Unknown', 'marks': df['marks'].mean()})
print('After filling missing values:')
print(filled.to_string(index=False, formatters={'marks': lambda x: f'{x:.2f}'}))

# Add a duplicate after imputation so it does not change the imputation mean.
with_duplicate = pd.concat([filled, filled.iloc[[2]]], ignore_index=True)
clean = with_duplicate.drop_duplicates()
print('After removing duplicates:')
print(clean.to_string(index=False, formatters={'marks': lambda x: f'{x:.2f}'}))
