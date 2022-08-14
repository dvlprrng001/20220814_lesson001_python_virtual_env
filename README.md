# 20220814_lesson001_python_virtual_env
Lesson 001 How to setup Python Virtual environment Locally

#Steps
01 Create a fresh Branch

git checkout -b users/dvr/20220814_setup_venv

#Setup python Virtual env
python -m venv venv

#Activate python virtual env
.\venv\Scripts\Activate.ps1

#How to deactivate
.\venv\scripts\deactivate.bat 
or exit

#Commit and push branch changes
git add -A
git commit -am "Creating basic setup for a fresh project"
git push
