# FastAPI Examples

This directory contains various FastAPI project examples and templates.

## 📁 Projects

### `fastapi-template/`
Production-ready FastAPI template with:
- PostgreSQL database
- Prisma ORM
- Docker Compose setup
- Database migrations

### `books-microservice/`
A minimal backend microservice to manage books (title, author) with:
- FastAPI framework
- SQLModel (Pydantic + SQLAlchemy)
- PostgreSQL database
- Alembic migrations

### `prisma_project/`
FastAPI project using Prisma as the ORM for database management.

### `metrics/backend/`
Backend service for tracking and managing metrics.

### `tutorial/`
Basic FastAPI tutorial project with database integration.

## 🚀 Quick Start

### Using Docker Compose

Most projects include a `docker-compose.yml` file:

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

3. Set up environment variables:
```bash
cp .env.sample .env
# Edit .env with your configuration
```

4. Run database migrations (if applicable):
```bash
alembic upgrade head
# or
prisma db push
```

5. Start the server:
```bash
uvicorn main:app --reload
```

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Prisma with Python](https://www.prisma.io/docs/concepts/overview/prisma-in-your-stack/python)

