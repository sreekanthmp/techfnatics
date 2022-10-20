# Website CMS with custom admin panel(Django)
Replica of the techfnatic website home page with the custom admin panel.

## Main requirements

1)python 

2)Django

3)PostgreSQL

4)HTML

5)CSS


## Description

In this project custom admin panel is used for CRUD operations. Django default authentication system is used in custom admin panel
for login and logout. We can able to add, update and delete product cards, website's logo, images, text, social media links, address, and 
phone number of website(techfnatic.com) through admin panel.

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```






