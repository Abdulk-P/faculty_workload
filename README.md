HOW TO USE THIS PROJECT USING CLONE METHOD

first setup a Virtual Environment using this Command in terminal
    -->python -m .venv env

then activate the Virtual envrionment using this command 
    -->.env/scripts/activate
    
my project folder is facutly_workload
and App is workload 

then go to facutly workload folder
    --> cd facutly-workload
install django
--> pip install django
in Django setting everything wiil be same if you clone this  project only you have to change the Database Configuration in in project folder -- > settings.py

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

 make sure you are in faculty-workload folder where project file , app and  manage.py is located
