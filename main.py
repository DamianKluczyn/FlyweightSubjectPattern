import json
from typing import Dict
from abc import ABC, abstractmethod

class IFlyweight(ABC):
    @abstractmethod
    def getState(self):
        pass

class Flyweight(IFlyweight):
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def getState(self) -> str:
        return self._shared_state

class FlyweightFactory:

    _flyweights: Dict[str, Flyweight] = {}
    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.getKey(state)] = Flyweight(state)

    def getKey(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def getFlyweight(self, shared_state: Dict) -> Flyweight:
        key = self.getKey(shared_state)
        if not self._flyweights.get(key):
            print("Creating new flyweight")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("Using existing flyweight")

        return self._flyweights[key]

def add_immigrant_to_database(factory: FlyweightFactory, first_name: str, last_name: str, latitude: str, longitude: str) -> None:
    real_subject = RealSubject()
    flyweight = factory.get_flyweight([first_name])
    flyweight.operaion([last_name, latitude, longitude])


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def __init__(self) -> None:
        self._first_name = ""
        self._last_name = ""
        self._latitude = ""
        self._longitude = ""

    def setData(self, proxy):

    def getNonUniqueState(self) -> str:
        return self._first_name
    def getUniqueState(self) -> str:
        return [self._last_name, self._latitude, self._latitude]

class Proxy(Subject):
    def __init__(self, first_name: str,last_name: str, latitude: str, longitude: str) -> None:
        self._first_name = first_name.lower().capitalize()
        self._last_name = last_name.lower().capitalize()
        self._latitude = latitude
        self._longitude = longitude
        self._real_subject = RealSubject()

    def checkData(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()


def client_code(subject: Subject) -> None:
    subject.request()

if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    client_code(proxy)