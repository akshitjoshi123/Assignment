from base import base

class sub_fibonaaci(base):

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
