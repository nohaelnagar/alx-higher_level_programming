#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        mul3 = num % 3
        mul5 = num % 5
        if mul3 == 0:
            print("Fizz", end=" ")
        elif mul3 == 0 and mul5 == 0:
            print("FizzBuzz", end=" ")
        elif mul5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
