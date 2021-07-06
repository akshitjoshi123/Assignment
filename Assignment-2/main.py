from problems.fibonaaci import sub_fibonaaci
from problems.prime_number import sub_prime_number
from problems.armstrong import sub_armstrong

print("Choose 1 for Fibonaaci Number\nChoose 2 for Prime Number Number\nChoose 3 for Armstrong Number\nChoose any one :")
i = int(input())
while i not in range(1,4):
    print("You choose invalid option\n")
    print("Choose 1 for Fibonaaci Number\nChoose 2 for Prime Number Number\nChoose 3 for Armstrong Number\nChoose any one :")
    i = int(input())

if i == 1:
    a = sub_fibonaaci()
    print(a.run())
elif i == 2:
    b = sub_prime_number()
    print(b.run())
elif i == 3:
    c = sub_armstrong()
    print(c.run())

