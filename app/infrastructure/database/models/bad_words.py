from sqlalchemy import Integer, Column

from infrastructure.database.base import Base


class BadWord(Base):
    __tablename__ = 'bad_words'
    __tableargs__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(Integer, nullable=False)
    used_count = Column(Integer, nullable=False, default=0)
