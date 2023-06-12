### Readme
 We have created Api for providing stock market information.

### Descriptions
- Signup API 
We are creating user provided by Django default user models and we are creating active user model. Active user model having 2 foreign key relation one of them uniqueuserkey model for save a unique identification and secound for Django default user model.

- Login API
We need 2 parameter user name and password for authentication and upon successfull verfication of the login the response get status code 200 

- Stock data API
For getting the stock information we need one perameter as symbols and user must be authentication & authorized for get the information. In resposne we get an array with sucess message status 200

- Throlling 
We will call this API while rendering on the stock information page using JavaScript we are calling this API in every 5 secound. If any case the request will be higher as we predict for that we implement throlling 

- Throlling Rule
As of now user can hit this API any number of times however only get result for up to 10 request/minutes (changeable). 


### Installation:

Steps for installation.
1-First clone the repository in your local system.
2-Install the projects requirement packages by running CMD (pip install -r requirements.txt ) before run this command python pip must be installed.
3-After that run the initial migrations for create default database table of django for that run the command python manage.py migrate.
4-After that run the django server using command python manage.py runserver.

Note: Default Port is 8000. if you want to change port please run command python manage.py runserver (Port number).

### Using:
We have created api for getting information about stock market of different-different stocks. we have also validate user authentication and authrized. we 
have implement throttling for stock information api, User can only request 10/minute/user and get the api data beyond that code will restrict the api request.
we have also create api logs in api.log which is stored in project directory.



### API endpoints
http://127.0.0.1:8000/api/register/
Required Input Parameter with POST method
username
password
email
first_name
last_name



http://127.0.0.1:8000/api/userlogin/
Required Input Parameter with POST method
username
password



http://127.0.0.1:8000/api/logout/
POST method

http://127.0.0.1:8000/api/stockData/
Required Input Parameter with POST method
symbol


