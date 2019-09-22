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

*Setup* - run these commands after you have accepted the [assignment](https://classroom.github.com/a/3vMerwUf "Assignment Link"). (switch "USERNAME" for your username)
```
git clone https://github.com/Harvard-Crimson-Technology-Comp/f19-001-USERNAME.git
cd f19-001-USERNAME
git remote add src https://github.com/Harvard-Crimson-Technology-Comp/project1.git
git pull src master
```

1. Edit questions.txt and add your (brief) answers. No need to spend too much time on it, we just want your best first attempt.

2. Edit _api/models.py_ to contain the appropriate 4 classes. Remember that these represent the organization of your data. In particular, you need to have PurchaseModel, UserModel, PortfolioModel, and StockModel.
``` 
  PurchaseModel
    timestamp - the timestamp (date and time) that the transaction occurred (note that "purchases" are both buys and sells of stocks)
    user - a relation to the UserModel that created the transaction
    symbol - a string of the symbol that was traded
    price - a float representing the price of the stock in dollars that was traded
    quantity - an integer representing the number of stocks that were traded

  UserModel
    first_name - the first name of the user
    last_name - the last name of the user
    api_token - the string representing the user's API token (a unique token which the user can use to authenticate their usage of the API)
    password - the hashed representation of the user's password (the password they will provide to log in to the web interface)
    username - the username which the user will use to log in to the web interface, also how they will reference themselves in using the API
    portfolio - a reference to the PortfolioModel representing this user's portfolio

  PortfolioModel
    cash - a float representing the amount of cash which the user has in their portfolio

  StockModel
    portfolio - a reference to the PortfolioModel to which this stock belongs
    symbol - the symbol of the stock that was purchased
    quantity - an integer representing the amount of stock
```
3. Edit _api/schema.py_ to allow for the resolution of each of the models you just created (we need to be able to resolve via GraphQL each of the fields within the Django models)

4. Edit _schema.py_ (just the very top portion!) to register your new schema in the global schema.

5. Verify that you can still start the web server. You can load data into the webserver by creating MODELNAME.json containing the appropriate fields and JSON objects (see _users.json_ for an example) and then using the command ```python3 manage.py loaddata MODELNAME.json```. Once you have data, going to *http://127.0.0.1:8000/graphql* should let you query that data in the GraphQL console.

6. If you would like to get ahead, you can start building out the logic in _api/views.py_; however that is not required at this time, and we'll explain in more depth next week. 

7. Submit this portion of the assignment by executing the following commands:
```
git add .
git commit -m "submitting first half"
git push
```

8. Great job!
