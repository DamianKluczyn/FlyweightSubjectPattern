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
    def __init__(self, first_name, last_name, latitude, longitude, flyweightFactory):
        self._first_name = first_name
        self._last_name = last_name
        self._latitude = latitude
        self._longitude = longitude
        self._unique_state = [self._last_name, self._latitude, self._longitude]
        self._non_unique_state = flyweightFactory.getFlyweight(self._first_name)

    def getSubjectInfo(self):
        return(self._first_name, self._last_name, self._latitude, self._longitude)

class Proxy(SubjectInterface):
    def __init__(self, first_name, last_name, latitude, longitude, flyweightFactory):
        self._realSubject = RealSubject(first_name.lower().capitalize().replace(' ',''), last_name.lower().capitalize().replace(' ',''), latitude, longitude, flyweightFactory)
    def getSubjectInfo(self):
        return self._realSubject.getSubjectInfo()

class Officer:
    def __init__(self):
        self._immigrant_first_name = ""
        self._immigrant_last_name = ""
        self._latitude = ""
        self._longitude = ""
    def setImmigrantData(self):
        self._immigrant_first_name = str(input("Imie: "))
        self._immigrant_last_name = str(input("Nazwisko: "))
        self._latitude = str(input("Szerokosc geograficzna: "))
        self._longitude = str(input("Wysokosc geograficzna: "))

    def getImmigrantData(self):
        return(self._immigrant_first_name, self._immigrant_last_name, self._latitude, self._longitude)

class Flyweight(IFlyweight):
    def __init__(self, state):
        self._non_unique_state = state

    def getState(self):
        return self._non_unique_state

class FlyweightFactory:
    _flyweights = {}

    def getFlyweight(self, non_unique_state):
        if self._flyweights.get(non_unique_state) is not None:
            print("Pobieram z cache")
            print("typo: ", self._flyweights.get(non_unique_state))
            return self._flyweights.get(non_unique_state)
        else:
            print("Przed dodaniem: ", self._flyweights)
            self._flyweights[non_unique_state] = Flyweight(non_unique_state)
            print("Po dodaniu: ", self._flyweights)
            print("Tworze nowego typa w cachu")


        return self._flyweights.get(non_unique_state)

    def getFlyweightFactory(self):
        return self._flyweights

class SaveData:
    def toFile(data):
        with open(".\\Immigrant_data.txt", "a") as f:
            f.writelines(str(data)+"\n")

if __name__ == '__main__':
    while(True):
        cache = FlyweightFactory()
        officer = Officer()
        officer.setImmigrantData()
        immigrant_data = Proxy(officer._immigrant_first_name, officer._immigrant_last_name, officer._latitude, officer._longitude, cache)
        SaveData.toFile(immigrant_data.getSubjectInfo())