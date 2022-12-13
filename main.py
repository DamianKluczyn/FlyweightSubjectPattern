from typing import Dict
from abc import ABC, abstractmethod

class IFlyweight(ABC):
    @abstractmethod
    def getState(self, unique_state) -> str:
        pass

class Flyweight(IFlyweight):
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state
        print("Flyweight innit")

    def getState(self, unique_state) -> str:
        return f"Shared state: {self._shared_state}, Unique state: {unique_state}"

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
            self._flyweights[key] = Flyweight(key)
        else:
            print("Using existing flyweight")

        return self._flyweights[key]


class Subject(ABC):
    @abstractmethod
    def getState(self) -> None:
        pass

class RealSubject(Subject):
    def __init__(self, first_name: Flyweight, last_name: str, latitude: float, longitude: float) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._latitude = latitude
        self._longitude = longitude
        print("RealSubject innit")

    def getState(self) -> str:
        return f"Shared state: {self._first_name}, Unique state: {self._last_name, self._latitude, self._longitude}"



class Proxy(Subject):
    def __init__(self, immigrant: list) -> None:
        self._first_name = immigrant[0].lower().capitalize()
        self._last_name = immigrant[1].lower().capitalize()
        self._latitude = immigrant[2]
        self._longitude = immigrant[3]
        self._real_subject = ""

    def addSubject(self, factory: FlyweightFactory) -> None:
        print("Proxy add subject")
        flyweight = factory.getFlyweight([self._first_name])
        flyweight.getState([self._last_name, self._latitude, self._longitude])
        self._real_subject = RealSubject(flyweight, self._last_name, self._latitude, self._longitude)
        SaveToFile(self);

    def getState(self) -> str:
        return self._real_subject.getState()

def ImmigrantInfo():
    first_name = input("Imie: ")
    last_name = input("Nazwisko: ")
    latitude = float(input("Szerokosc geograficzna: "))
    longitude = float(input("Wysokosc geograficzna: "))
    return [first_name, last_name, latitude, longitude]

def SaveToFile(data: Proxy):
    with open(".\\Dane.txt", "a") as f:
        f.write(data.getState() + "\n")



if __name__ == "__main__":
    factory = FlyweightFactory({})
    while True:
        proxy = Proxy(ImmigrantInfo())
        proxy.addSubject(factory)
