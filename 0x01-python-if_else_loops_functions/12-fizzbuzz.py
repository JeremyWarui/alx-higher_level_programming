#!/usr/bin/python3
def fizzbuzz():
    for num in range(0, 101):
        if num != 100:
            if num % 5 == 0 and num % 3 == 0:
                string = "FizzBuzz"
            elif num % 3 == 0:
                string = "Fizz"
            elif num % 5 == 0:
                string = "Buzz"
            else:
                string = num
            print("{} ".format(string), end="")
        else:
            print("{}".format(string))
