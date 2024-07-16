from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# genral form
# DATABASE_URL = "postgresql://postgresql:postgres@localhost:5432/python_db"
# engine = create_engine(DATABASE_URL)
# sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base = declarative_base()

DATABASE_URL = "postgresql://postgres:root@localhost:5432/pokemon"
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
