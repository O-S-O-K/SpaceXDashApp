# Feature Engineering


## Encoding
```python
pd.get_dummies(df, drop_first=True)

## Scaling
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)