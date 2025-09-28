from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL

# Create engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

# Dependency for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
