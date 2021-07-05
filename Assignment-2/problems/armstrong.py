import sys
from abc import ABC, abstractmethod

class armstrong(ABC):
    @abstractmethod
    def run(self):
        pass


class sub_armstrong(armstrong):
    def __init__(self):
       self.number = int(input("Enter Armdtrong Number : "))

    def run(self):
        sum = 0 
        n1 = self.number 
        while (n1 > 0): 
            dig = n1 % 10 
            sum += dig ** 3 
            n1 //= 10 
        if (self.number == sum): 
            return "Armstrong number"
        else: 
            return "Not an Armstrong number"


# obj3 = sub_armstrong()
# print(obj3.run())