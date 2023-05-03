#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i in range(10, 0, -1):
        print(i)
        i -= 1

    print('Happy New Year!')


def square_integers(int_list):
    square_numbers = [num * num for num in int_list]
    return square_numbers


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
