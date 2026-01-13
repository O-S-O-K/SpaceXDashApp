# Model Evaluation


## Accuracy & Confusion Matrix
```python
from sklearn.metrics import accuracy_score, confusion_matrix


accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)

## Classification Report
from sklearn.metrics import classification_report


print(classification_report(y_test, y_pred))