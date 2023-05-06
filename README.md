# Application Summary
    This api application returns the client’s IP address and an indication of the last time a request was received from that client IP address.

## Tools used
    - This is a python django application.
    - It lives behind a nginx reverse proxy.
    - It uses mongodb as the main database.
    - It's built and hosted into docker containers.

## Prerequisites
    - The mongodb user needs to be created in the database before gaining access through the django app.
    - Make sure the host has mongo installed.
    - Alter the /mongo/init.js values to with the preffered credentials.
    - Add the same credentials to the .env file in the main directory.
    - When the apps are in running state, you can add the user to the mongo db using the command
        "mongo admin < mongo/init.js"

# Build and Run App on Windows

### Building the images using docker compose:
    docker compose build

### Running the images using docker compose:
    docker compose up -d


# Build and Run App on Linux/MacOS

### Building the images using docker compose:
    docker-compose build

### Running the images using docker compose:
    docker-compose up -d


## Endpoints
    You can send a GET request to the endpoint /api/myip/ to see the application summary in action.