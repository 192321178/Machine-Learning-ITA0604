import pandas as pd

df = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D'],
    'class': ['I', 'II', 'I', 'II'],
    'marks': [78, 85, 92, 66]
})
filtered = df[(df['marks'] > 70) & (df['class'] == 'I')]
sorted_df = df.sort_values(['class', 'marks'], ascending=[True, False])
print('Filtered:')
print(filtered.to_string(index=False))
print('Sorted:')
print(sorted_df.to_string(index=False))
