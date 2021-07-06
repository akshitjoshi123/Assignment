from base import base

class primeNumber(base):  
    def run(self):
        if self.number > 1:
            for i in range(2, int(self.number/2)+1):
                if (self.number % i) == 0:
                    return "Not a prime number"
            else:
                return "prime number"
        else:
            return "Not a prime number"
