```
root/
│
├── backend/
│   ├── alembic/
│   │   └── versions/         # Database migration files
│   │   └── env.py
│   ├── venv/                 # Virtual environment for python dependency
│   ├── .gitignore
│   ├── alembic.ini           # alembic config, connected to sqlite:///models.db
│   ├── database.py           # To connect FastAPI app with the database (sqlite)
│   ├── main.py               # FastAPI app and API routers
│   ├── models.db             # sqlite3 database
│   ├── models.py             # For Alembic database migration and SQLAlchemy query
│   ├── README.md             # On running the FastAPI app, migration etc documentation
│   ├── schemas.py            # Pydantic schema
│   └── requirements.txt      # Dependencies (fastapi, uvicorn, sqlalchemy, alembic, psycopg2-binary)
├── README.md #   Project readme
```
