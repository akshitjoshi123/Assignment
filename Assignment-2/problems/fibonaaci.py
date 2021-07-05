import sys
from abc import ABC, abstractmethod

class fibonaaci(ABC):
    @abstractmethod
    def run(self):
        pass


class sub_fibonaaci(fibonaaci):
    def __init__(self):
        self.number = int(input("Enter fibonaaci Number: "))

    def run(self):
        a = 0
        b = 1
        if self.number < 0:
            return "Incorrect input"
        elif self.number == 0:
            return a
        elif self.number == 1:
            return b
        else:
            for i in range(2,self.number+1):
                c = a + b
                a = b
                b = c
            return b

# obj1 = sub_fibonaaci()

# print(obj1.run())