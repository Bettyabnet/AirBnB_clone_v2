#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel,  Base):
    """ State class """
    name = ""

    if storage_type != 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]
