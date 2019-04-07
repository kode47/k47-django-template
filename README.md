**Name: Kudzai Nyandoro**  
**Email: kudzai@kode47.com**  
**Project: Kode47 Django Project**  

- This is a Django 2.2 project with simple static pages providing an easy  
  starting point for a Django project. Feel free to use and change it any way  
  you like. Below are some import notes that might help with the set up.

- These notes assume you're on a Unix based system.  The first step is to set
   up  your environment variables.  Open your .bash_profile file if you are on a
   Mac or Linux and add the follow lines.

- Clone the application 

```bash
$ git clone git@github.com:kode47/k47_template.git
```

- Change the name of repository folder

```bash
$ mv k47_template animal_project
```

- Change directory into your new folder
 
```bash
cd animal_project
```
-  Preprare for deployment

- Remove current Heroku settings, you might not need to do this.

```bash
$ git remote rm heroku
```

- Remove the current git origin

```bash
$ git remote rm origin
```

-  If you're using Gitlab for version control your can create your remote
  repository as shown below. Otherwise use the Graphical user interface of your
  favorite repository provider; e.g. Github, Bitbucket, etc.  Also see my past
  vidoes if you're not sure how to set up a remote repository [here](https://kode47.com)


- Send you application to version control on GitLab.
 
```bash
$ git push --set-upstream git@gitlab.com:kcny/animal_project.git master
```

- Add the origin

```bash
$ git remote add origin git@gitlab.com:kcny/animal_project.git
```

- Install all application requirements.

```bash
$ pip install -r requirements.txt
```

- Create a Heroku app name

```bash
$ heroku create app_name
```
- Generate a new secret key and add it to the settings.py file or export to
   your .bash_profile.

```bash
$ python
>>> import secrets
>>> secrets.token_hex(24)
'4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b'
```
  

```bash
# .bash_profile

export SECRET_KEY="4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b"
export DEBUG_VALUE="True"
```

- Change the project name to your own.  In this example I'm using 'animal_project'

```bash
cd mv template_project animal_project
```

- Open the manage.py file and update Line # 8

```python
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_project.settings') # Line 8
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```
 
- Open and update the Procfile

```bash
web: gunicorn animal_project.wsgi
```

- Open and update Line 2 & 14 of the wsgi.py file

```python
"""
WSGI config for animal_project project. # Line 2

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_project.settings') # Line 14

application = get_wsgi_application()

```

- Open and update lines 2, , 25, 49 and 67 in the animal_project/settings.py file.

```bash
Django settings for animal_project project. # Line 2

ALLOWED_HOSTS = ['https://YourAppName.herokuapp.com'] # Line 25

ROOT_URLCONF = 'animal_project.urls' # Line 49

SGI_APPLICATION = 'animal_project.wsgi.application' # Line 67
```


- Copy and replace line number 24 in your setting.py file with it.

```python
.
.
.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b' # Line 24
.
.
.
```


- Activate the virtual environment
 

- Push to Heroku
```bash
$ git push heroku master
```

- Configure Django on Heroku

```bash
$ heroku config:set SECRET_KEY="4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b"
$ heroku config:set DEBUG_VALUE="True"
```
 
- Inter into the Heroku shell

```bash
$ heroku run bash
```

- Make migrations
```bash
$ python manage.py makemigrations
```

- Run migrations

```bash
$ python  manage.py migrate
````

- Create a superuser. This is optional.

```bash
$ heroku manage.py createsupersuser # follow the prompts with user name and
password for your superuser.
```


- Exit the Heroku shell

```bash
$ exit
```

- Open your application in the browser

```bash
$ heroku open
```

- Set your debug value to false

```bash
heroku config:set DEBUG_VALUE="False"
```

- Open you Heroku app in the browser

```bash
$ heroku open
```


