from abc import ABC, abstractmethod

class PyATB(ABC):

    @abstractmethod
    def payFees(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Dhir(PyATB):
    def payFees(self):
        print("Dhir --> Paid")


Dhir1 = Dhir()
Dhir1.enrolled()