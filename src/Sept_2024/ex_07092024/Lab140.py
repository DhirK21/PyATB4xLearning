# Abstraction
# Abstraction - OOPs
# Hiding the details and showing --> what is required

from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Dhir(Father):
    def loan(self):
        print("Dhir --> Paid the loan")

dhir_1 = Dhir("1L")
dhir_1.loan()