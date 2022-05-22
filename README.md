<div align="center">
  <h1 align="center">Weather Portal</h1>
  <p align="center">
    Final project of SDA python course: ZDPYTpol45
    
  </p>
</div>


## About

Using the weather application, the user can check the current weather conditions in the cities of his choice, after user registration, the application allows you to view the weather from more than one city. The user can change and reset the password via the received link to the e-mail. The app connects to the OpenWeather Api. The user has the option of displaying the city of his choice, saving it to the favorites and deleting the cities he has chosen. The system notifies the user of unsafe conditions, including high and low temperatures.

## Table of Contents
* [Getting started](#getting-started)
* [Usage](#usage)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Status](#project-status)
* [Contributors ✨](#contributors-)
* [Screenshots](#screenshots)


## GETTING STARTED

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
    `cd path/to/your/workspace`  
    `git clone https://github.com/zdpytpol45-project3/Weather_portal.git`
    
 4. Requirements
    - Once your virtual environment is activated and project is cloned you need to install requirements:  
    `pip install -r requirements.txt`
    
 5. Make your secret key, API key in settings.py     
   ```js
   In settings.py set:
       SECRET_KEY = os.getenv('SECRET_KEY')
   
       DEBUG = os.getenv("DEBUG") == "True"
   
   In manage.py folder create .env file.
   
   Add to .env file variables used in settings.py config: 
       SECRET_KEY = example_name
       DEBUG = True
       API_KEY = example_name
   ```
    
 ## USAGE
 
 To use this application you need to type (if you're in your workspace directory): 
 
 - `python manage.py migrate`
 - `python manage.py createsuperuser`
 - `python manage.py runserver`  
    
 ## Features
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
   
  
## Technologies Used:
    - Python 3.9.0
    - Django 4.0.4
    - requests
    - bootstrap 5
    - Weather API - OpenWeatherMap


## Languages and Tools:
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p> 

## Project Status
Project is: _in progress_

## Contributors ✨
<table>
<tr>
<td align="center"><a href="https://github.com/robert-adamczyk"><img src="https://avatars2.githubusercontent.com/u/17708702?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Robert Adamczyk</b></sub></a><br /><title="Code">💻</a></td>

<td align="center"><a href="https://github.com/GJezierski"><img src="https://avatars2.githubusercontent.com/u/17708702?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Grzegorz Jezierski</b></sub></a><br /><title="Code">💻</a></td>
    
 <td align="center"><a href="https://github.com/jacek-gielnik"><img src="https://avatars2.githubusercontent.com/u/17708702?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jacek Gielnik</b></sub></a><br /><title="Code">💻</a></td>
 </tr>   
</table>    

## Screenshots
### Home Site
<a href="https://freeimage.host/i/XFXThl"><img src="https://iili.io/XFXThl.md.png" alt="XFXThl.md.png" ></a>
### Login
<a href="https://freeimage.host/i/XFXxpf"><img src="https://iili.io/XFXxpf.md.png" alt="XFXxpf.md.png" ></a>
### Allerts
<a href="https://freeimage.host/i/XFXII4"><img src="https://iili.io/XFXII4.md.png" alt="XFXII4.md.png" ></a>
### Select City
<a href="https://freeimage.host/i/XFXokG"><img src="https://iili.io/XFXokG.md.png" alt="XFXokG.md.png" ></a>
### Show/Save City
<a href="https://freeimage.host/i/XFXuQ2"><img src="https://iili.io/XFXuQ2.md.png" alt="XFXuQ2.md.png" ></a>
 
## License

MIT License.
