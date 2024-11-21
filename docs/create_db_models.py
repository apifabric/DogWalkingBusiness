# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Owner(Base):
    """description: Represents the owner of pets in the dog walking business."""

    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String)
    email = Column(String)
    phone = Column(String)
    registration_date = Column(Date)
    total_fees_due = Column(Integer)  # derived attribute from sum rule


class Dog(Base):
    """description: Represents a dog that belongs to an owner."""

    __tablename__ = 'dog'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    birth_date = Column(Date)
    owner_id = Column(Integer, ForeignKey('owner.id'))


class Walker(Base):
    """description: Represents a dog walker employee."""

    __tablename__ = 'walker'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    hire_date = Column(Date)
    total_walks = Column(Integer) # derived attribute from count rule
    total_earnings = Column(Integer) # derived attribute from formula rule


class Walk(Base):
    """description: Represents an individual walk event."""

    __tablename__ = 'walk'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer)
    dog_id = Column(Integer, ForeignKey('dog.id'))
    walker_id = Column(Integer, ForeignKey('walker.id'))
    fee = Column(Integer)


class ClientPayment(Base):
    """description: Represents a payment made by a client."""

    __tablename__ = 'client_payment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'))


class WalkerPayment(Base):
    """description: Represents a payment made to a walker."""

    __tablename__ = 'walker_payment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    walker_id = Column(Integer, ForeignKey('walker.id'))


class Booking(Base):
    """description: Represents a pre-scheduled booking of a walk for a dog."""

    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_date = Column(Date, nullable=False)
    status = Column(String)
    dog_id = Column(Integer, ForeignKey('dog.id'))
    walker_id = Column(Integer, ForeignKey('walker.id'))


class DogHistory(Base):
    """description: Records historical walks and related details for dogs."""

    __tablename__ = 'dog_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dog_id = Column(Integer, ForeignKey('dog.id'))
    walk_id = Column(Integer, ForeignKey('walk.id'))


class MaintenanceLog(Base):
    """description: Logs maintenance activities related to dogs, such as grooming or health check-ups."""

    __tablename__ = 'maintenance_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    date = Column(Date)
    dog_id = Column(Integer, ForeignKey('dog.id'))


class Feedback(Base):
    """description: Stores feedback from clients regarding the walks."""

    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    comments = Column(String)
    rating = Column(Integer)
    date = Column(Date)
    dog_id = Column(Integer, ForeignKey('dog.id'))
    walker_id = Column(Integer, ForeignKey('walker.id'))


class Schedule(Base):
    """description: Represents a walker’s daily schedule."""

    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_of_week = Column(String)
    available_hours_start = Column(DateTime)
    available_hours_end = Column(DateTime)
    walker_id = Column(Integer, ForeignKey('walker.id'))


class Service(Base):
    """description: Represents additional services offered to clients, such as grooming or training."""

    __tablename__ = 'service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    dog_id = Column(Integer, ForeignKey('dog.id'))


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test data creation for each table:

# Owners
owner1 = Owner(id=1, name="John Doe", address="123 Maple Street", email="john@example.com", phone="555-1234", registration_date=date(2021, 1, 10), total_fees_due=100)
owner2 = Owner(id=2, name="Jane Smith", address="456 Oak Avenue", email="jane@example.com", phone="555-5678", registration_date=date(2021, 2, 15), total_fees_due=150)
owner3 = Owner(id=3, name="Emily Johnson", address="789 Pine Road", email="emily@example.com", phone="555-8765", registration_date=date(2021, 3, 20), total_fees_due=75)
owner4 = Owner(id=4, name="Henry Brown", address="321 Elm Street", email="henry@example.com", phone="555-6543", registration_date=date(2021, 4, 25), total_fees_due=200)

# Dogs

dog1 = Dog(id=1, name="Rex", breed="Labrador", birth_date=date(2019, 5, 1), owner_id=1)
dog2 = Dog(id=2, name="Fido", breed="Beagle", birth_date=date(2020, 6, 15), owner_id=2)
dog3 = Dog(id=3, name="Fluffy", breed="Poodle", birth_date=date(2018, 7, 20), owner_id=3)
dog4 = Dog(id=4, name="Bella", breed="Bulldog", birth_date=date(2019, 8, 25), owner_id=4)

# Walkers
walker1 = Walker(id=1, name="Alice Walker", email="alice@example.com", phone="555-1111", hire_date=date(2022, 1, 5), total_walks=0, total_earnings=0)
walker2 = Walker(id=2, name="Bob Trail", email="bob@example.com", phone="555-2222", hire_date=date(2022, 2, 10), total_walks=0, total_earnings=0)
walker3 = Walker(id=3, name="Charlie Way", email="charlie@example.com", phone="555-3333", hire_date=date(2022, 3, 15), total_walks=0, total_earnings=0)
walker4 = Walker(id=4, name="Diana Path", email="diana@example.com", phone="555-4444", hire_date=date(2022, 4, 20), total_walks=0, total_earnings=0)

# Walks
walk1 = Walk(id=1, date_time=datetime(2022, 5, 10, 10, 0), duration_minutes=30, dog_id=1, walker_id=1, fee=25)
walk2 = Walk(id=2, date_time=datetime(2022, 6, 20, 9, 30), duration_minutes=45, dog_id=2, walker_id=2, fee=30)
walk3 = Walk(id=3, date_time=datetime(2022, 7, 15, 11, 0), duration_minutes=60, dog_id=3, walker_id=3, fee=40)
walk4 = Walk(id=4, date_time=datetime(2022, 8, 5, 8, 45), duration_minutes=30, dog_id=4, walker_id=4, fee=35)

# Client Payments
payment1 = ClientPayment(id=1, amount=100, date=date(2022, 9, 1), owner_id=1)
payment2 = ClientPayment(id=2, amount=150, date=date(2022, 10, 5), owner_id=2)
payment3 = ClientPayment(id=3, amount=75, date=date(2022, 11, 10), owner_id=3)
payment4 = ClientPayment(id=4, amount=200, date=date(2022, 12, 15), owner_id=4)

# Walker Payments
wpayment1 = WalkerPayment(id=1, amount=100, date=date(2022, 9, 25), walker_id=1)
wpayment2 = WalkerPayment(id=2, amount=150, date=date(2022, 10, 30), walker_id=2)
wpayment3 = WalkerPayment(id=3, amount=75, date=date(2022, 11, 25), walker_id=3)
wpayment4 = WalkerPayment(id=4, amount=200, date=date(2022, 12, 30), walker_id=4)

# Bookings
booking1 = Booking(id=1, walk_date=date(2022, 12, 1), status="Scheduled", dog_id=1, walker_id=1)
booking2 = Booking(id=2, walk_date=date(2022, 12, 2), status="Completed", dog_id=2, walker_id=2)
booking3 = Booking(id=3, walk_date=date(2022, 12, 3), status="Cancelled", dog_id=3, walker_id=3)
booking4 = Booking(id=4, walk_date=date(2022, 12, 4), status="Scheduled", dog_id=4, walker_id=4)

# Dog History
history1 = DogHistory(id=1, dog_id=1, walk_id=1)
history2 = DogHistory(id=2, dog_id=2, walk_id=2)
history3 = DogHistory(id=3, dog_id=3, walk_id=3)
history4 = DogHistory(id=4, dog_id=4, walk_id=4)

# Maintenance Logs
log1 = MaintenanceLog(id=1, description="Grooming Session", date=date(2022, 1, 15), dog_id=1)
log2 = MaintenanceLog(id=2, description="Veterinary Check-up", date=date(2022, 2, 20), dog_id=2)
log3 = MaintenanceLog(id=3, description="Vaccination Schedule", date=date(2022, 3, 25), dog_id=3)
log4 = MaintenanceLog(id=4, description="Dental Cleaning", date=date(2022, 4, 30), dog_id=4)

# Feedback
feedback1 = Feedback(id=1, comments="Great walk!", rating=5, date=date(2022, 1, 5), dog_id=1, walker_id=1)
feedback2 = Feedback(id=2, comments="Very good service", rating=4, date=date(2022, 2, 10), dog_id=2, walker_id=2)
feedback3 = Feedback(id=3, comments="Average experience", rating=3, date=date(2022, 3, 15), dog_id=3, walker_id=3)
feedback4 = Feedback(id=4, comments="Loved it!", rating=5, date=date(2022, 4, 20), dog_id=4, walker_id=4)

# Schedules
schedule1 = Schedule(id=1, day_of_week="Monday", available_hours_start=datetime(2022, 1, 3, 8, 0), available_hours_end=datetime(2022, 1, 3, 17, 0), walker_id=1)
schedule2 = Schedule(id=2, day_of_week="Tuesday", available_hours_start=datetime(2022, 1, 4, 9, 0), available_hours_end=datetime(2022, 1, 4, 18, 0), walker_id=2)
schedule3 = Schedule(id=3, day_of_week="Wednesday", available_hours_start=datetime(2022, 1, 5, 8, 0), available_hours_end=datetime(2022, 1, 5, 17, 0), walker_id=3)
schedule4 = Schedule(id=4, day_of_week="Thursday", available_hours_start=datetime(2022, 1, 6, 10, 0), available_hours_end=datetime(2022, 1, 6, 19, 0), walker_id=4)

# Services
service1 = Service(id=1, name="Grooming", price=50, dog_id=1)
service2 = Service(id=2, name="Training", price=75, dog_id=2)
service3 = Service(id=3, name="Vet Checkup", price=60, dog_id=3)
service4 = Service(id=4, name="Walking", price=40, dog_id=4)


session.add_all([owner1, owner2, owner3, owner4, dog1, dog2, dog3, dog4, walker1, walker2, walker3, walker4, walk1, walk2, walk3, walk4, payment1, payment2, payment3, payment4, wpayment1, wpayment2, wpayment3, wpayment4, booking1, booking2, booking3, booking4, history1, history2, history3, history4, log2, log3, log4, feedback1, feedback2, feedback3, feedback4, schedule1, schedule2, schedule3, schedule4, service1, service2, service3, service4])
session.commit()
