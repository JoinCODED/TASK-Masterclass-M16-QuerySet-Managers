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

## Managers 101

### Singles

We will be creating a `singles` manager for songs.

1. Add a `managers.py` file inside of the `albums` app.
2. Create a `SingleManager` class that inherits from `models.Manager` inside of `albums/managers.py`.
3. Add a `get_queryset` method and annotate the return as `models.QuerySet[Any]`.
   - In the method filter for `is_single=True`

### Features

We will be creating a `features` manager for songs.

1. Create a `FeatureManager` class that inherits from `models.Manager` inside of `albums/managers.py`.
2. Add a `get_queryset` method and annotate the return as `models.QuerySet[Any]`.
   - In the method filter for songs that contain the word `feat` (case-insensitive).

### Combination

Go to `albums/models.py` and add 3 class variables to your `Song` model. One of them would be `objects = models.Manager()`, the second would be `singles = SingleManager()` (make sure to import it from `albums.managers`), and the last one would be `features = FeatureManager()`.

### Testing

Open up your python shell using `poetry run manage shell`, and import the `Song` model. Try out `Song.objects.count()`, then `Song.singles.count()`, and finally `Song.features.count()`. You should get different counts for each manager.
