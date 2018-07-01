# Report Api

### run the app by:
    * clone the repo
    * export database_uri=postgress://user:password@host/db
    * export FLASK_APP=api.py
    * run `pip install -r requirements.txt`
    * run the dev server with `flask run`

Swagger-UI is available at `http://localhost:5000/`

reports are available through the `/report/{id}` endpoint.

You can choose between format options json, xml, pdf by setting the `Accept` request header.
