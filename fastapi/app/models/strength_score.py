from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Boolean, Integer, Float, String, DateTime, Interval
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

from db.base_class import Base


class UserSod(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    sod_id = Column(Integer, ForeignKey('sod.id'))
    created = Column(DateTime)
    comment = Column(LONGTEXT)
    user = relationship("User", back_populates="user_sod")
    sod = relationship("Sod", back_populates="user_sod")


class SodScore(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_sod_id = Column(Integer, ForeignKey('usersod.id'))
    location = Column(Integer)
    weight = Column(Float)