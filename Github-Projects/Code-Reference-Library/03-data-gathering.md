# Data Gathering


## Read CSV
```python
import pandas as pd


df = pd.read_csv('data/file.csv')

## Read Excel
df = pd.read_excel('data/file.xlsx')

## API Request
import requests


response = requests.get(url)
data = response.json()