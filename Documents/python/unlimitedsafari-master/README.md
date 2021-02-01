# Unlimited Safari

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Are you a cheapskate just like me? Can you not afford to buy a monthly subscription of Orilley's Safaribooks? Well here's your chance to have unlimited free accounts.

Unlimited safari creates a trial account for Orilley Safari Books every 10 days (or at the trail expiration date), automatically, so you will never have to create them manually. 

### Stack Used
Below mentioned is the list of all technologies, frameworks, languages, DB's used for building this application.

* [Python] - Python 3.8.0
* [Django] - Django 3.0 though it would run the same with 2.2 or whatever the earlier LTS version is.
* [Django Rest Framework] - To serve the data in JSON format.
* [jQuery] - For a much more user friendly DOM manipulation API.
* [PostgreSQL] - Holds the data for user, trial safari accounts, etc.


### Installation
Follow along to know how to setup the project.

```sh
# clone the repository
$ git clone https://github.com/iamllama/unlimitedsafari.git
# cd into the new cloned directory and install the requirements
$ pip install -r requirements.txt
# create a database called unlimitedsafari
$ postgres -U postgres
postgres > create database unlimitedsafari;
# run the server
$ ./manage.py runserver 
```

Lisence Type - [Apache License 2.0]


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Apache License 2.0]: <https://github.com/google/ExoPlayer/blob/release-v2/LICENSE>
   [jQuery]: <https://jquery.com/>
   [Python]: <https://www.python.org/>
   [Django]: <https://www.djangoproject.com/>
   [Django Rest Framework]: <https://www.django-rest-framework.org/>
   [Javascript]: <https://javascript.info/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [Apache2]: <https://httpd.apache.org/>
   [MySQL]: <https://www.mysql.com/>
   [Composer]: <https://getcomposer.org/>
