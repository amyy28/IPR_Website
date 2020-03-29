# IPR_Website :computer: 

Made on Django framework and JavaScript, Bootstrap for the course Intellectual Property Rights, to enable students to upload  
their photos ,presentations and skit video content conducted as a part of classroom activity sessions. Each team also has a
unique auto-generated report which provides a glimpse of the activities conducted by that team.

## 🔧 Instructions to run
```
git clone https://github.com/amyy28/IPR_Website.git
```

### Now 'cd' into the cloned repository
Now again execute ```cd IPR_Website```

### Install all the requirements at once
```pip3 install -r requirements.txt```

### Create a superuser for login
#### Create your username and password of your choice
```python3 manage.py createsuperuser```

### Now you require to migrate all the database table schemas to the default sql database 
```python3 manage.py makemigrations```

### Now migrate it
```python3 manage.py migrate```

### Now run the server
```python3 manage.py runserver```

## Hit the below URL
```http://127.0.0.1:8000/```

Now go to login and enter the created username and password. Once logged in, create the team by filling in the required details and then skit and presentations data can easily be loaded using the forms in the UI. 
