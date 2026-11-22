import pandas as pd

df = pd.DataFrame({
    'class': ['I', 'II', 'I', 'II', 'I', 'II'],
    'marks': [78, 85, 92, 66, 74, 88]
})
summary = df.groupby('class')['marks'].agg(['mean', 'max', 'min'])
print(summary.to_string(float_format=lambda value: f'{value:.2f}'))
