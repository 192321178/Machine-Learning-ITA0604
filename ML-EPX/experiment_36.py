import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E'],
    'marks': [78, 85, 92, 66, 74]
})
df['marks'].plot(kind='hist', title='Marks Distribution', bins=5)
plt.xlabel('Marks')
plt.tight_layout()
plt.savefig('marks_hist.png')
plt.close()

df.plot(x='name', y='marks', kind='bar', title='Marks by Student', legend=False)
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('marks_bar.png')
plt.close()
print('Plots saved: marks_hist.png, marks_bar.png')
