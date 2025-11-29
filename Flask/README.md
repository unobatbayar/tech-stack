# Flask Examples

This directory contains various Flask web framework examples and projects.

## 📁 Projects

### `flask_sqlalchemy_postgres/`
Flask application with:
- SQLAlchemy ORM
- PostgreSQL database
- Alembic migrations
- Docker setup

### `froshims/`
Sample Flask application demonstrating:
- Form handling
- Database operations
- Template rendering

### `hello/`
Simple "Hello World" Flask application for beginners.

### `sql-sqlalchemy/`
Flask project demonstrating SQL and SQLAlchemy integration.

## 🚀 Quick Start

### Using Docker

```bash
docker compose up --build
```

### Manual Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
# Run migrations
flask db upgrade
# or
alembic upgrade head
```

4. Run the application:
```bash
flask run
# or
python app.py
```

The application will be available at `http://localhost:5000`

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Tutorial](https://flask.palletsprojects.com/tutorial/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

