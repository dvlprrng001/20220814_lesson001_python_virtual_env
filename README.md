# 20220814_lesson001_python_virtual_env
Lesson 001 How to setup Python Virtual environment Locally

# Steps
01 Create a fresh Branch

git checkout -b users/dvr/20220814_setup_venv

# Setup python Virtual env
python -m venv venv

# Activate python virtual env
.\venv\Scripts\Activate.ps1

# How to deactivate
.\venv\scripts\deactivate.bat 
or exit

#Commit and push branch changes
git add -A
git commit -am "Creating basic setup for a fresh project"
git push --set-upstream origin users/dvr/20220814_setup_venv

# Lesson 002

Activate Venv
.\venv\Scripts\Activate.ps1
Install Python Django and Selenium
Install Chrome Binary for Selenium
python -m pip install --upgrade pip
pip install django selenium chromedriver_binary


# Setup and start Django Project
.\venv\Scripts\Activate.ps1
# django-admin startproject NewProjectName FolderName
django-admin startproject superlists .

#django-admin startproject dvranga001

python manage.py runserver


echo "from selenium import webdriver " >> functional_tests.py
echo "import chromedriver_binary # Adds chrome driver binary to path" >> functional_tests.py

echo "driver4ChromeBrowser = webdriver.Chrome()  ">> functional_tests.py
echo "driver4ChromeBrowser.get(""http://localhost:8000"") ">> functional_tests.py
echo "assert ""Django"" in  driver4ChromeBrowser.title ">> functional_tests.py

python functional_tests.py