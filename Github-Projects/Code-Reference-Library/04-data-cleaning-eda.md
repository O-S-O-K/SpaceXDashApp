# Data Cleaning & EDA


## Inspect Data
```python
df.head()
df.info()
df.describe()

## Missing Values
df.isnull().sum()
df.dropna()
df.fillna(0)

## Duplicates
df.drop_duplicates()