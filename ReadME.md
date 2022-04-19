# Timer API

## Tech Stack

- Django
- Django Rest Framework

## API endpoints

### Create

`POST /timers`

- Request

  ```
  {
      "webhook_url": "Webhook url to be called when the timer is complete",
      "duration": "Duration in milliseconds"
  }
  ```

- Response

  ```
    TimerId
  ```

  This Id will be used for future API calls including `Status`, `Pause`, and `Resume`.

### Status

`GET /timers/{timerId}`

- Response

  ```
    {
        "webhook_url": "Webhook url",
        "status": "Running/Paused/Finished",
        "remaining": "Time remaining in ms"
    }
  ```

### Pause

`PUT /timers/{timerId}/pause`

- Response

  ```
    {
        "webhook_url": "Webhook url",
        "status": "Running/Paused/Finished",
        "remaining": "Time remaining in ms"
    }
  ```

### Resume

`PUT /timers/{timerId}/resume`

- Response

  ```
    {
        "webhook_url": "Webhook url",
        "status": "Running/Paused/Finished",
        "remaining": "Time remaining in ms"
    }
  ```

## Run

Make sure that the docker is setup and running on your machine.

`docker-compose up -d --build`

Then you can access the api on `http://localhost:8000`.

## Admin

In case you want to use the Django admin panel, create a superuser using this command.

Get the docker container id from the Docker desktop.

`docker exec -it container_id python manage.py createsuperuser`

Eg: `docker exec -it timer_web_1 python manage.py createsuperuser`

Then open `http://localhost:8000/admin` and login with the superuser you've just created.
