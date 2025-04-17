#### Activate virtual environment

source venv/bin/activate

#### Run FastAPI app

uvicorn main:app --reload

#### Migrations

- After you’ve made changes to your `models.py` (like adding a new table or column), run:

`alembic revision --autogenerate -m "add users table"`

- Apply the Migration (Upgrade the DB)
  To apply the migration to the actual database:

`alembic upgrade head`

- Rollback (Optional)
  If something goes wrong or you want to undo:

`alembic downgrade -1`

#### To do

pip freeze > requirements.txt
