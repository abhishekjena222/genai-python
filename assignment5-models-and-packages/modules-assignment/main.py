def assignment():
    print("Modules and Packages")

import math_util
from math_util import square
def task1():
    print("\n -- task 1 - Create a simple module math_util.py -- ")
    print("Add : ",math_util.add(12, 4))
    print("Subtract : ",math_util.subtract(12, 4))
    print("Square : ",math_util.square(4))
    print("Import Square : ",square(4))


import string_utils
def task2():
    print("\n -- task 2 - Create another model string_util.py -- ")
    text = "hey, Im abhi"
    print("Capatelize : ",string_utils.capitalize_word(text))
    print("Reverse : ",string_utils.reverse_string(text))
    print("Count : ",string_utils.word_count(text))

def task3():
    print("\n -- task 3 - Create sample package shop_package -- ")
    print("discount.py \nbilling.py \n__init__.py")

import shop_package.discount as disc
import shop_package.billing as bill
def task4():
    print("\n -- task 4 - Import the package in main.py -- ")
    print("Apply discount : ",disc.apply_discount(1000,50))
    print("Flat discount : ",disc.flat_discount(1000))
    print("Calculate total : ",bill.calculate_total([100, 200, 300]))
    print("Apply tax : ",bill.apply_tax(1000))

def main():
    assignment()
    task1()
    task2()
    task3()
    task4()


if __name__ == "__main__" : main()