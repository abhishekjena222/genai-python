class AgeError(Exception):
    pass

class NegativeError(Exception):
    pass

def assignment():
    print("Exception Handeling")

def task1():
    print("\n -- task 1 - Safe devision utility -- ")
    try:
        numerator = int(input("Enter numerator : "))
        denominator = int(input("Enter denominator : "))
        result = numerator/denominator
    except (ValueError, ZeroDivisionError) as e:
        print("Error: The number is invalid or devisible by zero")
    else:
        print("Result : ",result)
    finally:
        print("Operation complete")

def task2():
    print("\n -- task 2 - Bill calculator with error handeling -- ")
    prices = [120, 350, 'abc', 500, -200, 800]
    result = 0
    for price in prices:
        try:
            if not isinstance(price, (int,float)):
                raise TypeError("Not a number")
            if price < 0: 
                raise ValueError("Negative number")
        except (ValueError, TypeError) as e:
            print(f"Skipped : {price} : ",e)
        else:
            result += price
            print("Result : ",result)


def task3():
    print("\n -- task 3 - Custom exception age validation -- ")
    try:
        age = int(input("Enter your age : "))
        check_age(age)
    except (ValueError, AgeError) as e:
        print("Error: ",e)
    else:
        print("Age is valid")


def check_age(age):
    if age < 1 or age > 120:
        raise AgeError("Age must be between 1 and 120")

def task4():
    print("\n -- task 4 - File reader with exception handeling -- ")
    file_name = input("Enter file name : ")
    try:
        with open("assignment6-exception-handeling/"+file_name,"r") as file:
            content = file.readlines()
    except (FileNotFoundError, PermissionError) as e:
        print("Error: ",e)
    else:
        for line in content[::3]:
            print(line.strip())
    finally:
        print("File operation attempted.")


def task5():
    print("\n -- task 5 - Mini program : safe shopping cart -- ")
    cart =[]
    while True:
        price = input("Enter the price : ")
        if price == 'q':
            break
        try:
            price = float(price)
            if price < 0: raise NegativeError("Price can't be negetive")
        except (ValueError, NegativeError) as e:
            print("Error: ",e)
        else:
            cart.append(price)

    print("Items : ", cart)
    print("Tota items : ", len(cart))
    print("Total Bill : ", sum(cart))




def main():
    assignment()
    task1()
    task2()
    task3()
    task4()
    task5()

if __name__ == "__main__" : main()