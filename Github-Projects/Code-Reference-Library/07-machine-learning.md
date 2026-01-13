# Machine Learning Models


## Train/Test Split
```python
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

## Model Example
from sklearn.linear_model import LogisticRegression


model = LogisticRegression()
model.fit(X_train, y_train)