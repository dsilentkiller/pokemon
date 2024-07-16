from sqlalchemy import Column, Integer, String
from config import Base


class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    image = Column(String)
