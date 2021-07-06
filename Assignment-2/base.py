from abc import ABC, abstractmethod

class base(ABC):

    def __init__(self):
       self.number = int(input("Enter Number : "))

    @abstractmethod
    def run(self):
        pass
