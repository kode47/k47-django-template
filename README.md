**Name: Kudzai Nyandoro**  
**Email: kudzai@kode47.com**  
**Project: Kode47 Django Project**  

- This is a Django 2.2 project with simple static pages providing an easy
  starting point for a Django project. Feel free to use and change it any way
  you like. Below are some import notes that might help with the set up.
  
1. Clone the application 

```bash
$ git clone git@github.com:kode47/k47_template.git
```

2. Change the name of repository folder

```bash
$ mv k47_template animal_project
```

3. Change directory into your new folder
 
```bash
cd animal_project
```

4. Change the project name to your own.  In this example I'm using 'animal_project'

```bash
cd mv template_project animal_project
```

5. Open the manage.py file and update line #8

```python
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_project.settings')
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
 
6. Open and update the Procfile

```bash
web: gunicorn animal_project.wsgi
```


7. Open and update line 2 & 14 of the wsgi.py file

```python
"""
WSGI config for animal_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_project.settings')

application = get_wsgi_application()

```

8. Open and update lines 2, , 25, 49 and 67 in the animal_project/settings.py file.

```bash
Django settings for animal_project project. # line 2

ALLOWED_HOSTS = ['https://YourAppName.herokuapp.com'] # line 25

ROOT_URLCONF = 'animal_project.urls' # line 49

SGI_APPLICATION = 'animal_project.wsgi.application' # line 67
```

