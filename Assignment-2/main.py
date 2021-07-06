from problems.fibonaaci import sub_fibonaaci
from problems.prime_number import sub_prime_number
from problems.armstrong import sub_armstrong


try:
    print("Choose 1 for Fibonaaci Number\nChoose 2 for Prime Number Number\nChoose 3 for Armstrong Number\nChoose any one :")
    i = int(input())
    while i not in range(1,4):
        print("You choose invalid option\n")
        print("Choose 1 for Fibonaaci Number\nChoose 2 for Prime Number Number\nChoose 3 for Armstrong Number\nChoose any one :")
        i = int(input())

    if i == 1:
        fibonaaci_obj = sub_fibonaaci()
        print(fibonaaci_obj.run())
    elif i == 2:
        prime_obj = sub_prime_number()
        print(prime_obj.run())
    elif i == 3:
        armstrong_obj = sub_armstrong()
        print(armstrong_obj.run())

except ValueError as e:
        print("Opps!!! You select a String!")
except Exception as e:
        print("Something went Wrong!")