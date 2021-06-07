# USER_API

This is the API that creates, updates, deletes Users

Steps to setup dev environment (using virtual environment):

1. Ensure Virtual environment and Python is installed on your system , check python version on runtime.txt file 

2 . Create Virtual environment and activate the virtual environment ,check this url for  how to setup virtual environment
     (https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
     
3. Install dependent packges by running this command 
 
   pip install -r requirements.txt

4.create a database in your locahost and update the database credentials inside settings.py file now 
  create Table in your database by using  below these  commands 
  
     python manage.py makemigrations
     python manage.py migrate
   

5. Now Your setup is Done you have to run your server   Start the server by running below commands

Python manage.py runserver

6. Testing API using postman

Note: - Import the userapi/userapi.postman_collection.json file inside your postman it will contain all the api url and request ,response with header
please use it  it will make your tast easy

7. Running the Unit Tests  Run the tests using the below command

python manage.py test




     


