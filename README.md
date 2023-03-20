# restaurant-booking

Welcome to this app developed for Melp. In order to use this app yo must follow the next steps:

1. You must create a copy of the .env.example and rename it as .env. You must write the appropiate variable values for each one on this file
2.  Tou can work either locally (on your pc) or with docker
## Working locally
1. Create a Postgres database and install postgis extension.
2. Make sure you put the information for the database in the .env file.
3. Create a virtual environment:
    ´python -m venv venv´
4. Activate the virtual environment:
    ´source venv/Scripts/activate´
5. Install dependencies:
    ´pip install -r requirements.txt´
6. Run migrations (execute this command in the same folder of manage.py, as is /restaurant_booking):
    ´python manage.py migrate´
7. Run server (execute this command in the same folder of manage.py, as is /restaurant_booking):
    ´python manage.py runserver´
8. You are done, now you can make request to the following endpoints:
    * /restaurants
    * /restaurants/statistics

Please note that some commands may vary depending on your OS. Please refer to the Python official documentation.

## Working with Docker
1. Make sure you are on the root folder of the proyect and execute the following command:
    `docker-compose --env-file restaurant_booking/restaurant_booking/.env up -d`
2. You are done, now you can make request to the following endpoints:
    * /restaurants
    * /restaurants/statistics

### About endpoints
For mor information on the endpoints please refer to the collection to be able to consult examples on each one.