import sys
from abc import ABC, abstractmethod

class prime_number(ABC):
    @abstractmethod
    def run(self):
        pass


class sub_prime_number(prime_number):
    def __init__(self):
       self.number = int(input("Enter Prime Number : "))

    def run(self):
        if self.number > 1:
 
            for i in range(2, int(self.number/2)+1):
                if (self.number % i) == 0:
                    return "Not a prime number"
                    break
            else:
                return "prime number"

        else:
            return "Not a prime number"

# obj2  = sub_prime_number()
# print(obj2.run())