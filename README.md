### Project 1
-----

Hello friends! Welcome to your first project! We've provided a bit of template code to get you started, and this file should walk you through the big ideas of what you'll need to do! We have split the below into 2 parts - what we did and what you will do. In the "what we did" section, you _do not_ and _should not_ re-execute those instructions. That is just to explain to you what we did, why we did it, and what its effect was. In the "what you will do" section, you _must_ and _should_ execute instructions, read them carefully, etc. The first section is just to let you know what went down. The second section is for you to do.

Enjoy!

-----

##### What we did
*Do not execute these instructions!* This part is just so you know how we set up this template code!

1. Virtualenv - this is a way to isolate different versions of Python and Python packages - we used a _virtual environment_ to keep our workspace nice and tidy. Django - this is our main server - it controls the flow of code from a request to the backend and back out to the user. We install it so that Python has access to the Django framework.
```
mkvirtualenv project1
pip3 install django
```

2. Initializing the overall project structure - this builds out the file structure for us. After we built it, we went into the directory.
```
django-admin startproject project1
cd project1
```

3. React! Now's time for us to install a tool to help us build out the directory structure for our React frontend.
```
npm install -s create-react-app
npx create-react-app project1-frontend
```

4. Whew! Now that that's all done, our directory structure is pretty much all set up, we just needed to add an app in Django, and then we'd be pretty much set! These _startapp_ commands are to further modularize and design our Django application.
```
cd project1
django-admin startapp api
django-admin startapp web
```

5. Now we need to grab all the glue that will hold our project together - for that, we're going to use Graphene (a way to interface with GraphQL) and Graphene-Django (a way to connect GraphQL and Django)
```
pip3 install graphene-django
```

6. We also did some configuration for you - we modified _settings.py_ so that all of our new fancy apps (_web_, _api_, _graphene\_django_) are included in _INSTALLED\_APPS_. And we allowed Django to broadcast on certain hosts. We also set up some simple models in _web.models.py_, created an example schema in _web.schema.py_ and built out example views in _web.views.py_

-----

##### What you need to do :)

We will updated this after the meeting today!