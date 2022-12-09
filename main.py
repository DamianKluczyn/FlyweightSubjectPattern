from abc import ABC, abstractmethod

class SubjectInterface(ABC):
    @abstractmethod
    def getSubjectInfo(self):
        pass

class IFlyweight(ABC):
    @abstractmethod
    def getState(self):
        pass

class RealSubject(SubjectInterface):
    def __init__(self, first_name, last_name, latitude, longitude):
        self._first_name = first_name.lower().capitalize()
        self._last_name = last_name.lower().capitalize()
        self._latitude = latitude
        self._longitude = longitude

    def getSubjectInfo(self):
        return(self._first_name, self._last_name, self._latitude, self._longitude)

class Proxy(SubjectInterface):
    def __init__(self, realSubject):
        self._realSubject = RealSubject(realSubject.getSubjectInfo())

class Officer:
    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._latitude = 0
        self._longitude = 0
    def setSubjectData(self):
        self._first_name = str(input("Imie: "))
        self._last_name = str(input("Nazwisko: "))
        self._latitude = float(input("Szerokosc geograficzna: "))
        self._longitude = float(input("Wysokosc geograficzna: "))

    def getSubjectData(self):
        return(self._first_name, self._last_name, self._latitude, self._longitude)

