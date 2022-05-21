## Weather Portal

Using the weather application, you are able to check the current weather conditions in the cities of your choice, after user registration, the selected cities will be remembered. The user can reset and change the password. The app connects to the OpenWeather Api. The user has the option to delete the cities he has chosen.

## Table of Contents
* [Getting started](#getting-started)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Usage](#usage)
* [Project Status](#project-status)


### GETTING STARTED

1. Checking Python version.
    - To be able to use this script you'll need to have Python installed, you can check whether you have it installed or not by typing in terminal:  
`python3 --version`  
or:  
`python --version` 
    - This script was written using version 3.9.0 and it is advised to use the same version.
    - If you don't have Python installed you can go to [Python.org](https://www.python.org/downloads/) to download it.
    
 2. Creating Virtual Environment 
    - To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:  
    `python3 -m venv your-env`  
    - Once you’ve created a virtual environment, you may activate it.  
    `source your-env/bin/activate`
    
 3. Download
     - You need to clone repository to your local destination  
    `$ cd path/to/your/workspace`  
    `git clone https://github.com/zdpytpol45-project3/Weather_portal.git`
    
 4. Requirements
    - Once your virtual environment is activated and project is cloned you need to install requirements:  
    `$ pip install -r requirements.txt`  
    
 ### USAGE
 
 To use this application you need to type (if you're in your workspace directory): 
 
 - `python manage.py migrate`
 - `python manage.py createsuperuser`
 - `python manage.py runserver`  
    
 ### Features
   List the ready features here:
   - User registration/login
   - Change password
   - Reset password
   - Registrator new user
   - connect with OpenWeather Api
   - save city for logged users (without maximum)
   - for not logged user show maximum 1 city
   - make validator to check:
        - city exist 
        - city already is in list
   - delete button for user to delete city in saved user list
   
  
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p> 

### Project Status
Project is: _in progress_

### Screenshots
..
 
