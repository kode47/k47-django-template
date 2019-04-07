**Name: Kudzai Nyandoro**  
**Email: kudzai@kode47.com**  
**Project: K47 Django Project**  

- This is a Django 2.2 project with simple static pages providing an easy
  starting point for a Django project. Feel free to use and change it any way
  you like. Below are some import notes that might help with the set up.
  
1. Clone the application 

```bash
$ git clone git@github.com:kode47/k47_template.git
```

```bash
$ mv k47_template animals_project
```

```bash
cd animals_project
```

- Change the project name to your own.  In this example I'm using 'animals_project'

```bash
cd mv template_project animals_project
```

- Open the manage.py file and update line #8

```python
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animals_project.settings')
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
web: gunicorn animals_project.wsgi
```


- Open and update line 2 & 14 of the wsgi.py file

```python
"""
WSGI config for animals_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animals_project.settings')

application = get_wsgi_application()

```

- Open and update lines 2, , 25, 49 and 67 in the animals_project/settings.py file.

```bash
Django settings for animals_project project. # line 2

ALLOWED_HOSTS = ['https://YourAppName.herokuapp.com'] # line 25

ROOT_URLCONF = 'animals_project.urls' # line 49

SGI_APPLICATION = 'animals_project.wsgi.application' # line 67
```

