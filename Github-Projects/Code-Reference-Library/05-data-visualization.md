# Data Visualization


## Matplotlib
```python
import matplotlib.pyplot as plt


plt.hist(df['column'])
plt.show()

## Seaborn
import seaborn as sns


sns.boxplot(x='col', y='target', data=df)