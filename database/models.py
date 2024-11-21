# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 21, 2024 20:53:38
# Database: sqlite:////tmp/tmp.zzGFkRt884-01JD87YV1D96ADA8EPPFE8HZ6X/DogWalkingBusiness/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Owner(SAFRSBaseX, Base):
    """
    description: Represents the owner of pets in the dog walking business.
    """
    __tablename__ = 'owner'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    email = Column(String)
    phone = Column(String)
    registration_date = Column(Date)
    total_fees_due = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    ClientPaymentList : Mapped[List["ClientPayment"]] = relationship(back_populates="owner")
    DogList : Mapped[List["Dog"]] = relationship(back_populates="owner")



class Walker(SAFRSBaseX, Base):
    """
    description: Represents a dog walker employee.
    """
    __tablename__ = 'walker'
    _s_collection_name = 'Walker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    hire_date = Column(Date)
    total_walks = Column(Integer)
    total_earnings = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="walker")
    WalkerPaymentList : Mapped[List["WalkerPayment"]] = relationship(back_populates="walker")
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="walker")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="walker")
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="walker")



class ClientPayment(SAFRSBaseX, Base):
    """
    description: Represents a payment made by a client.
    """
    __tablename__ = 'client_payment'
    _s_collection_name = 'ClientPayment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    owner_id = Column(ForeignKey('owner.id'))

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("ClientPaymentList"))

    # child relationships (access children)



class Dog(SAFRSBaseX, Base):
    """
    description: Represents a dog that belongs to an owner.
    """
    __tablename__ = 'dog'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    birth_date = Column(Date)
    owner_id = Column(ForeignKey('owner.id'))

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("DogList"))

    # child relationships (access children)
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="dog")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="dog")
    MaintenanceLogList : Mapped[List["MaintenanceLog"]] = relationship(back_populates="dog")
    ServiceList : Mapped[List["Service"]] = relationship(back_populates="dog")
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="dog")
    DogHistoryList : Mapped[List["DogHistory"]] = relationship(back_populates="dog")



class Schedule(SAFRSBaseX, Base):
    """
    description: Represents a walker’s daily schedule.
    """
    __tablename__ = 'schedule'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    day_of_week = Column(String)
    available_hours_start = Column(DateTime)
    available_hours_end = Column(DateTime)
    walker_id = Column(ForeignKey('walker.id'))

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class WalkerPayment(SAFRSBaseX, Base):
    """
    description: Represents a payment made to a walker.
    """
    __tablename__ = 'walker_payment'
    _s_collection_name = 'WalkerPayment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    walker_id = Column(ForeignKey('walker.id'))

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerPaymentList"))

    # child relationships (access children)



class Booking(SAFRSBaseX, Base):
    """
    description: Represents a pre-scheduled booking of a walk for a dog.
    """
    __tablename__ = 'booking'
    _s_collection_name = 'Booking'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_date = Column(Date, nullable=False)
    status = Column(String)
    dog_id = Column(ForeignKey('dog.id'))
    walker_id = Column(ForeignKey('walker.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("BookingList"))
    walker : Mapped["Walker"] = relationship(back_populates=("BookingList"))

    # child relationships (access children)



class Feedback(SAFRSBaseX, Base):
    """
    description: Stores feedback from clients regarding the walks.
    """
    __tablename__ = 'feedback'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    comments = Column(String)
    rating = Column(Integer)
    date = Column(Date)
    dog_id = Column(ForeignKey('dog.id'))
    walker_id = Column(ForeignKey('walker.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("FeedbackList"))
    walker : Mapped["Walker"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class MaintenanceLog(SAFRSBaseX, Base):
    """
    description: Logs maintenance activities related to dogs, such as grooming or health check-ups.
    """
    __tablename__ = 'maintenance_log'
    _s_collection_name = 'MaintenanceLog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    date = Column(Date)
    dog_id = Column(ForeignKey('dog.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("MaintenanceLogList"))

    # child relationships (access children)



class Service(SAFRSBaseX, Base):
    """
    description: Represents additional services offered to clients, such as grooming or training.
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    dog_id = Column(ForeignKey('dog.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("ServiceList"))

    # child relationships (access children)



class Walk(SAFRSBaseX, Base):
    """
    description: Represents an individual walk event.
    """
    __tablename__ = 'walk'
    _s_collection_name = 'Walk'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer)
    dog_id = Column(ForeignKey('dog.id'))
    walker_id = Column(ForeignKey('walker.id'))
    fee = Column(Integer)

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("WalkList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkList"))

    # child relationships (access children)
    DogHistoryList : Mapped[List["DogHistory"]] = relationship(back_populates="walk")



class DogHistory(SAFRSBaseX, Base):
    """
    description: Records historical walks and related details for dogs.
    """
    __tablename__ = 'dog_history'
    _s_collection_name = 'DogHistory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dog_id = Column(ForeignKey('dog.id'))
    walk_id = Column(ForeignKey('walk.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("DogHistoryList"))
    walk : Mapped["Walk"] = relationship(back_populates=("DogHistoryList"))

    # child relationships (access children)
