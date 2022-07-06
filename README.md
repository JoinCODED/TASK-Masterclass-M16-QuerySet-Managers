# QuerySet Managers

Let's manage our query sets

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M16-QuerySets).
2. Make sure to have `python 3.9.13` installed (use `pyenv install 3.9.13` to ensure it is installed).
3. Install the project dependencies using `poetry install`.
4. Run the migrations using `poetry run manage migrate`.
5. Create a database using `psql`:
   - `psql -d postgres`
   - `CREATE DATABASE music_task;`
6. Create a `.env` file inside the project.
   - Add `DEBUG=False`
   - Add `DATABASE_URL=postgres://username:password@localhost:5432/music_task`
7. Open the database using `poetry run manage dbshell`.
8. Load the mock data using `\i ./fixtures/main.sql`.
   - Note: you might some errors, ignore them.
