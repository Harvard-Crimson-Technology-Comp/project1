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

5. Verify that you can still start the web server. You can load data into the webserver by creating MODELNAME.json containing the appropriate fields and JSON objects (see _users.json_ for an example) and then using the command ```python3 manage.py loaddate MODELNAME.json```. Once you have data, going to *http://127.0.0.1:8000/graphql* should let you query that data in the GraphQL console.

6. If you would like to get ahead, you can start building out the logic in _api/views.py_; however that is not required at this time, and we'll explain in more depth next week. 

7. Submit this portion of the assignment by executing the following commands:
```
git add .
git commit -m "submitting first half"
git push
```

8. Great job!

-----

##### 09/28 Update - Part 2!
1. Welcome to the next portion of building our own web app! In order to pull instructions go ahead and run:
```
git pull src master
```
You will certainly get a slew of merge conflicts, and you're welcome to keep the incoming changes (our solutions) or reject them (use your own solutions). We do assume that your code works at least to the spec we provide - which means that all fields are named correctly and are of the correct type, but you are welcome to include additional information (we simply won't check the additional information!).

2. In this part we want to add some functionality now that our database is set up and ready to go. This means that our backend API will need to become functional. There are a few steps to this process, but the high level overview is that incoming requests to our API will be parsed in _api/views.py_ and the database will be interacted with via code. You may also want to look at _project1/urls.py_ in order to get requests to go where they're supposed to go. We don't particularly care how exactly you implement everything, so long as the sample requests and interface that we require are functional. (If that makes no sense, then see below for a concrete version of that)

3. Buy - this view should accept HTTP POST requests containing an API token (named "api_token"), a stock symbol (named "symbol"), and a quantity (named "quantity"). Any other method of request should be rejected via HttpResponseNotAllowed (Django has a built in implementation of this behavior). You will want to check that the API token belongs to a user (and which user). You will be responsible for validating the symbol (verify that it exists on the NYSE - potentially look at a public API for this information - you may find the requests library very useful). You will also be responsible for verifying that the user can in fact make this purchase (do they have sufficient funds?). And finally you will need to adjust the user's portfolio, add a PurchaseModel entry, and add a StockModel entry. Upon failure, this view must return a JSON response containing at least the field "error" with an appropriate error message. Upon success, this view must return a JSON response containing at least the fields "symbol", "quantity", "timestamp" where timestamp is the time that was recorded in the PurchaseModel entry.

4. Sell - this view should also only accept HTTP POST requests containing an API token (named "api_token"), a stock symbol (named "symbol"), and a quantity (named "quantity"). Any other method of request should be rejected via HttpResponseNotAllowed. Similarly to the buy view, sell will require you to verify that the user exists, that the symbol is within their portfolio, and that they have sufficient stock to sell that quantity. You will need to add an entry to PurchaseModel (do not remove old entries! simply add a new one recording the sale - there are several ways to indicate that it was a sale as opposed to a buy), modify the user's Portfolio, and modify the user's Stocks. Similarly to with buy, upon failure, this view must return a JSON response containing at least the field "error" with an appropriate error message. Upon success, this view must return a JSON response containing at least the fields "symbol", "quantity", "timestamp" where timestamp is the time that was recorded in the PurchaseModel entry.

5. Register - this is the last complex view you will need! This is also the trickiest one - this view must accept only HTTP POST requests containing a first name ("first_name"), last name ("last_name"), username ("username"), and password ("password"). You will need to add the appropriate user model (verifying of course that someone with the same username does not exist already!), store their hashed password in this new model, and generate a unique API token for this user. Upon failure, this view must also return a JSON response containing at least the field "error" with an appropriate error message. Upon success, this view must return a JSON response containing at least the fields "username" and "api_token" with the appropriate contents. 

6. And finally list - this is a view which must only accept HTTP GET requests which contain a single field, the user's API token ("api_token"). This only needs to verify that the API token corresponds to a user. Upon failure, this view must do as the previous 3 views do. Upon success, this view must return a JSON response containing at least the fields "stocks" (a list of JSON objects of the form ```{"symbol": "SYM", "quantity": #, "price": "12.34"}```), "cash", and "timestamp" (the time that the response was returned). 

7. And that's it! You should have a functional API that allows for the creation of users, the purchase and sale of stocks, and the viewing of said stocks. For fun and profit! Submit with:
```
git add .
git commit -m "submitting second half"
git push
```