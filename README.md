# the-eye-django
Python/Django the eye application

Conclusions

1. The Eye is used by multiple applications via request to the endpoint of the application, per event.
2. The API rest endpoint should recibe an applicationId to identify the application and validate the event.
3. The API rest endpoint need authorization, the Application sends the sessionId.
4. There is a need of validate the payloads, this can be achieve by using json schemas per category + name + application id

Running the project:

Run in the shell:
 1. docker-compose build
 2. docker-compose up

Using the application:

I add the SQLite db with an application record created with id: 100 also a session record 
created with value 'ttmmm9xl3uix8fs76kl19uhxhfnikhwm'


Example for a POST request:

curl --location --request POST 'http://127.0.0.1:8000/api/event/' \
--header 'ApplicationId: 100' \
--header 'Content-Type: application/json' \
--data-raw '{
  "session_id": "ttmmm9xl3uix8fs76kl19uhxhfnikhwm",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}'