# flaskAuthTracker
Simple Flask-based API which allows tracking registered/anonymous users.
Incorporates OpenAPI specification.

# Tech stack
- Python
- Flask 2.2.0
- Marshmallow
- PostgreSQL
- Docker

# Local setup steps
1. `git clone` this reposity into the desired directory in your local machine.
2. Navidate to the directory where you cloned this repo into.
3. Create `db.env` and copy-paste the contents of `db.env.example` there.
4. Create `.env` and copy-paste the contents of `.env.example` there.
5. Build the project with `docker-compose build`.
6. Run the project with `docker-compose up`.
7. Apply the database migrations with `docker-compose exec api flask db migrate`.
8. Open your browser and navigate to `http://127.0.0.1:5000/api/docs/` to see the OpenAPI specification for this application.
