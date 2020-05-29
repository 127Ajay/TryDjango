pipenv install
##prerequisite

```
python
mongodb
pip install pipenv: if pipenv is not installed then run this command
```

##Steps:

<p>1.Create a Project Folder</p>
```
    mkdir try_django
```
<p>2.Go into project folder</p>
```
    cd try_django
```
<p>3.Using pip env install django and djongo</p>
```
    pipenv --python 3.7 install django==2.2 djongo==1.3.2
``` 
<p>4.Activate pipenv shell</p>
```
    pipenv shell
```
<p>5.Create a srv Folder</p>
```
    mkdir src
```
<p>5.Go into src folder</p>
```
    cd src
```
<p>7.Create startup project</p>
```
    django-admin startproject try_django .
```
<p>8.Into settings.py file of your project, add:</p>
```
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'Try_django',
        }
    }
```
<p>9.Run (ONLY the first time to create collections in mongoDB):</p>
```
    python manage.py makemigrations
    python manage.py migrate
```
<p>10.Create a superUser</p>
```
    python manage.py createsuperuser
```
<p>11.Runserver</p>
```
    python manage.py runserver
```
