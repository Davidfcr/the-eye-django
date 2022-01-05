# the-eye-django
Python/Django the eye application

Conclusions

1. The Eye is used by multiple applications via calls to the endpoint of the application, per event.
2. The API rest endpoint should recibe an applicationId to identify the application and validate the event.
3. The API rest endpoint need authorization by user/password to identify the user and then save the sessionId, the Application sends the sessionId.
4. There is a need of validate the payloads, this can be achieve by using json schemas per category + name

