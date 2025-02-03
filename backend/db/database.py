from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///./boozerats.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()






def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()