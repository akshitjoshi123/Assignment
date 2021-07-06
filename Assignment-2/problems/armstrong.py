from base import base

class sub_armstrong(base):
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