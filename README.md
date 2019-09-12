**Name: Kudzai Nyandoro**  
**Email: kudzai@kode47.com**  
**Project: Kode47 Django Project**  

### Django Template Initial Set up

- This is a Django 2.2.5 project with simple static pages providing an easy starting point for a Django project. Feel free to use and change it any way you like. Below are some import notes that might help with the set up.

- These notes assume you're on a Unix based machine.  The first step is to set up  your environment variables.  Open your .bash_profile file if you are on a Mac or Linux and add the follow lines.
 
- Clone the application 

```bash
git clone git@github.com:kode47/k47-django-template.git
```
- Optional -- change the name of repository folder

```bash
$ mv kode47/k47-django-template animal_project
```
- Change directory into your new folder
 
```bash
cd animal_project
```

- Recommended option --create your virtaul enviroment.  There are many ways
  create a virtual environment so I'll leave that up to you.  

- Install all application requirements.

```bash
$ pip install -r requirements.txt
```

- Run migrations 

```bash
$  python manage.py make migrations
```

- Generate a new secret key and add it to the settings.py file or export to
   your .bash_profile.

```bash
$ python
>>> import secrets
>>> secrets.token_hex(24)
'4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b'
```
- Add the following to your .bash_profile

```bash
# .bash_profile

export SECRET_KEY="4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b"
export DEBUG_VALUE="True"
```

- Fire up the server

```bash
$ python manage.py runserver
```

- In your browser visit localhost:8000

### Add your application to version control

- Rename the current git origin

```bash
$ git remote rename origin upstream
```

**Push to Github**

- Visit https://github.com, log in or create and an account.  Next, create your
  remote repository.  If you're new to version control visit [my blog](https:/kode47.com) and view episodes 8 and 9 for more on version control and how to set up a remote repository on Github.

```bash
$ git remote add origin https://github.com/kode47/animal_project.git
$ git push -u origin master
```

**Or push to Gitlab**

-  If you're using Gitlab for version control your can create your remote
   repository as shown below without leaving your console.  I'm not sure how to
   do this on Github.  You can also visit [my blog](https://kode47.com) and
   watch episode 22 for more on Gitlab. Be sure to replace `kcny` with your username in the lines below. This is an optional way of creating your remote repository on GitLab.

- Send your application to version control on GitLab.
 
```bash
$ git push --set-upstream git@gitlab.com:kcny/animal_project.git master
```
- Add the origin

```bash
$ git remote add origin git@gitlab.com:kode47/animal_project.git
```

```bash
$ git add -A
$ git commit -m "Rename application ready to deploy."
$ git push 
```

- Create a Heroku app name

```bash
$ heroku create app_name
```
- Configure Django on Heroku

```bash
$ heroku config:set SECRET_KEY="4db736c4a169807620d3dcc0d2b5414dcd1bb5c5a100488b"
$ heroku config:set DEBUG_VALUE="False"
```
- Push to Heroku

```bash
$ git push heroku master
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
$ python manage.py createsuperuser # Follow the prompts
```
- Exit the Heroku shell

```bash
$ exit
```
- Open your application in the browser

```bash
$ heroku open
```




