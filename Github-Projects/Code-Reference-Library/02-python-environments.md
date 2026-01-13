# Python Environments & Libraries


## Create Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate

## Install Libraries
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

## Save Environment
pip freeze > requirements.txt

## Recreate Environment
pip install -r requirements.txt