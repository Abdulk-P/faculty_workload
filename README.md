HOW TO USE THIS PROJECT USING CLONE METHOD

first setup a Virtual Environment using this Command in the Terminal
    -->python -m venv .env

then activate the Virtual environment using this command 
    -->.env/scripts/activate
    
my project folder is facutly_workload
and App is workload 

then go to the faculty workload folder
    --> cd faculty-workload
install Django
--> pip install django
in the Django setting everything will be same if you clone this  project only you have to change the Database Configuration in the project folder -- > settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Or your database server
        'PORT': '3306',
    }
}

and run this command for initializing the Database
 --> python manage.py makemigrations
 and 
 -->python manage.py migrate

 then run ther server
 --> python manage.py runserver

 make sure you are in the faculty-workload folder where the project file, app, and  manage.py are located
