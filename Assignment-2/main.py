from problems.fibonaaci import fibonaaci
from problems.prime_number import primeNumber
from problems.armstrong import armstrong


try:
    print("Choose 1 for Fibonaaci Number\nChoose 2 for Prime Number Number\nChoose 3 for Armstrong Number\nChoose any one :")
    i = int(input())
    while i not in range(1,4):
        print("You choose invalid option\n")
        print("Choose 1 for Fibonaaci Number\nChoose 2 for Prime Number Number\nChoose 3 for Armstrong Number\nChoose any one :")
        i = int(input())

    if i == 1:
        fibonaaciObj = fibonaaci()
        print(fibonaaciObj.run())
    elif i == 2:
        primeObj = primeNumber()
        print(primeObj.run())
    elif i == 3:
        armstrongObj = armstrong()
        print(armstrongObj.run())

except ValueError as e:
        print("Opps!!! You select a String!")
except Exception as e:
        print("Something went Wrong!")