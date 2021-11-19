import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email=Column(String(250), unique=True, nullable=False)
    password=Column(String(250), unique=True, nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('character.id'))
    planets_id = Column(Integer, ForeignKey('planet.id'))
    starships_id = Column(Integer, ForeignKey('starship.id'))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    height=Column(Integer, nullable=True)
    mass=Column(Integer, nullable=True)
    hair_color=Column(String(120), nullable=True)
    skin_color=Column(String(120), nullable=True)
    eye_color=Column(String(120), nullable=True)
    birth_year=Column(Integer, nullable=True)
    gender=Column(String(250), nullable=True)
    name=Column(String(250), nullable=True)
    created=Column(String(250), nullable=True)
    edited= Column(String(250), nullable=True)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    url=Column(String(250), nullable=False)
    name=Column(String(250), nullable=False)
    diameter=Column(Integer, nullable=False)
    orbital_period=Column(Integer, nullable=False)
    gravity=Column(Integer, nullable=False)
    population=Column(Integer, nullable=False)
    terrain=Column(String(250), nullable=False)
    surface_water=Column(Integer, nullable=False)
    rotation_period=Column(Integer, nullable=False)
    climate=Column(String(250), nullable=False)
    create=Column(String(250), nullable=True)
    edited=Column(String(250), nullable=True)
    description=Column(String(250), nullable=False)


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    model=Column(String(250), nullable=True)
    consumables=Column(String(250), nullable=True)
    manufacturer=Column(String(250), nullable=True)
    crew=Column(Integer, nullable=True)
    passengers=Column(Integer, nullable=True)
    starship_class=Column(String(250), nullable=True)
    length=Column(Integer, nullable=True)
    cargo_capacity=Column(Integer, nullable=True)
    consumables=Column(String(250), nullable=True)
    created=Column(String(250), nullable=True)
    edited= Column(String(250), nullable=True)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e