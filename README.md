
# Build CRUD API with Django REST framework

In this article, you'll learn how to build a CRUD API with Django and Django REST framework. The RESTful API will have endpoints for performing CRUD operations against an SQLite database.


## Screenshots

![App Screenshot](https://codevoweb.com/wp-content/uploads/2022/12/Build-CRUD-API-with-Django-REST-framework.webp)


## Topics Covered


* Run the Django CRUD API Locally
    
* Setup Django
   
* Create the Django Models
        
        * Database Model
        * Model Serializer

* Create the CRUD API Views in Django
        
        * GET and POST API Views
        * GET, PATCH, and DELETE API Views

* Add the CRUD Routes
        
        * Add the CRUD API URLs
        * Add the Base URL of the CRUD App to the Project
    
* Create the Migration File and Start the Server

* Test the Django CRUD API
        
        * Create Note
        * Update Note
        * Get All Notes
        * Delete Note

* Create Documentation for the CRUD API

## Step For Setup

1. git clone https://github.com/Vishnuk2259/django_app_function_view

2.  cd django_app_function_view

3. pip3 install -r requirements.txt

4 python3 manage.py makemigrations

5. python3 manage.py migrate

6. python3 manage.py runserver

7. Login to http://127.0.0.1:8000