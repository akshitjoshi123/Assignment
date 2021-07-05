from problems.fibonaaci import sub_fibonaaci
from problems.prime_number import sub_prime_number
from problems.armstrong import sub_armstrong
from abc import ABC, abstractmethod

class base(ABC):
    @abstractmethod
    def run(self):
        pass


class sub_base(base):
    def __init__(self):
        print("Choose 1 for Fibonaaci Number")
        print("Choose 2 for Prime Number Number")
        print("Choose 3 for Armstrong Number")
        self.i = int(input("Choose any one :"))

    def run(self):
        if self.i == 1:
            a = sub_fibonaaci()
            return (a.run())
        elif self.i == 2:
            b = sub_prime_number()
            return (b.run())
        elif self.i == 3:
            c = sub_armstrong()
            return (c.run())
        else:
            return "You choose in valid option"
