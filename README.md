# Description
 ## Project perspective
- If you are like me, You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it.

- Your Job is to create a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## User stories
One is able to: 

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.


## Setup/Installation
On your terminal, clone the project.
    
    $ git clone https://github.com/299hannah/Neighbourhood-App.git
    

Navigate into the cloned project.

    $ cd Neighbourhood-App

Create a `.env` file.

    $ touch .env

Inside `.env`, add the following and fill the empty fields with the appropriate values:

```python
SECRET_KEY=
DEBUG=True
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1
CLOUD_NAME= 
API_KEY=
API_SECRET=
```
The CLOUD_NAME, API_KEY, and the API_SECRET are from your account on [Cloudinary](https://cloudinary.com/).

Create the virtual environment and install the requirements from `requirements.txt`

    $ python3 -m venv env
    $ . env/bin/activate
    $ pip install -r requirements.txt


Perform a migration.

    $ python3 manage.py migrate


Start the server to run locally.

    $ python3 manage.py runserver

## API Endpoints
This site has 2 endpoints; 
    
- **Profiles:** [https://wwwrate.herokuapp.com/api/profiles/](https://Neighbourhood-App.herokuapp.com/api/profiles/)

    - Query the profiles stored in the database.
- **Projects:** [https://wwwrate.herokuapp.com/api/projects/](https://Neighbourhood-App.herokuapp.com/api/projects/)

    -  Query data about the projects stored in the database.

## Known Bugs
No known bugs.
## Technologies Used
- Django
- Python 3.8.5
- Bootstrap 4
- Postgresql
- Cloudinary
- Heroku
## Support and contact details
If you have any suggestions, you can reach me via [email](hannahwambui022@gmail.com).
### License
 [(https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright &copy; 2021 **[299hannah](www.github.com/299hannah)**