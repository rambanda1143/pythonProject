
from datetime import date
from typing import List

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class ImmutablePerson:
    def __init__(self, name: str, id: str, date_of_joining: date, addresses: List[Address]):
        self._name = name
        self._id = id
        self._date_of_joining = date_of_joining
        self._addresses = tuple(addresses)  # Make it immutable

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        return self._addresses

# Example Usage
addresses = [Address("123 Street", "CityA", "12345"), Address("456 Avenue", "CityB", "67890")]
person = ImmutablePerson("John Doe", "1234", date(2020, 1, 1), addresses)
print(person.name, person.id, person.date_of_joining, person.addresses)