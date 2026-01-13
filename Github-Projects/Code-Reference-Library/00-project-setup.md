# Project Setup (Folders & Files)


## Create a New Project Folder
```powershell
mkdir my-project
cd my-project
code .

## Create Common Project Structure
```powershell
mkdir data notebooks src tests
New-Item README.md requirements.txt .gitignore

## Rename/Delete Files or Folders
```powershell
Rename-Item old_name new_name
```powershell
Remove-Item file.txt
Remove-Item folder -Recurse

