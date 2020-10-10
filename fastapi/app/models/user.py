from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(100))
    hashed_password = Column(String(100), nullable=False)
    user_sod = relationship("UserSod", back_populates="user")
    sod = relationship("Sod", back_populates="user")