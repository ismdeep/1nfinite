from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,ForeignKey
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Image(Base):
    __tablename__ = 'Image'
    id = Column(INT, primary_key=True, autoincrement=True)
    url = Column(Text)

