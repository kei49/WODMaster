from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Boolean, Integer, Float, String, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

from db.base_class import Base


class Sod(Base):
    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(30))
    created = Column(DateTime)
    public = Column(Boolean)
    user = relationship("User", back_populates="sod")
    user_sod = relationship("UserSod", back_populates="sod")


class StrengthMaster(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))


class StrengthSet(Base):
    id = Column(Integer, primary_key=True, index=True)
    sod_id = Column(Integer, ForeignKey('sod.id'))
    strength_master_id = Column(Integer, ForeignKey('strengthmaster.id'))
    location = Column(Integer)
    time = Column(Float)
    reps = Column(Integer)