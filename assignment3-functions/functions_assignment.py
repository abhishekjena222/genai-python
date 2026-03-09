def assignment():
    print("Functions Assignment")

def task1():
    print("\n -- task 1 - Basic Function Price after discount --")
    discount_price = apply_discount(1000, 70)
    print("The discount price: ",discount_price)
    print(apply_discount(500))


def apply_discount(price, discount_percent = 5):
    if discount_percent > 60:
        discount_percent = 60
    discount = discount_percent/100
    return price * (1 - discount)


def task2():
    print("\n -- task 2 - Recursion function factorial unit -- ")
    n = 5
    print(f"Factorial of {n} is : ",factorial(n))

def factorial(n):
    if (n < 0):
        print("Negative number not allowed")
        return None

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def task3():
    print("\n -- task 3 - Lambda Function Gst Calculator -- ")
    
    gst = lambda price : price * (1 + 0.18)
    discount_amount = lambda price,discount : price * (1 - discount/100)
    price = 100
    print(gst(price))
    print(discount_amount(gst(price), 40))


def task4():
    print("\n -- task 4 - Using map(): apply gst in price list -- ")
    prices = [100, 250, 400, 1200, 50]
    prices_with_gst = list(map(lambda price : price * (1 + 0.18), prices))
    print("Prices : ",prices)
    print("Gst proce : ",prices_with_gst)


def task5():
    print("\n -- task 5 - filter() Filter expensive products -- ")
    prices = [100, 250, 400, 1200, 500, 2000, 850]
    expensive_product = list(filter(lambda price : price > 500, prices))
    cheap_product = list(filter(lambda price : price <= 500, prices))

    print("Expensive products : ",expensive_product)
    print("Cheap products : ",cheap_product)


def task6():
    print("\n -- task 6 - Combined Utility function -- ")
    prices = [100, 500, 900, 50, 750]
    discounted_prices,filtered_prices = process_prices(prices)
    print("Process : ",prices)
    print("Discount : ",discounted_prices)
    print("Filtered : ",filtered_prices)

def process_prices(prices):
    discounted_prices = list(map(lambda price : price * (1 - 0.1), prices))
    filtered_prices = list(filter(lambda price : price > 300, discounted_prices))

    return discounted_prices,filtered_prices


def task7():
    print("\n -- task 7 - Mini problem Menu using function -- ")
    prices_list = []

    print("1 - add price \n2 - avg of price \n3 - highest of numbers \nq - to Quit")
    while True:
        print("List : ",prices_list)
        option = input("Enter the preference : ")
        if option == '1':
            try:
                number = int(input("Enter the number : "))
            except ValueError:
                print("Invalid Integer")
                continue
            prices_list = add_price(prices_list,number)
            print("Price addend : ",prices_list)
        elif option == '2':
            avg_price = get_average_price(prices_list)
            print("The average of the list : ",avg_price)
        elif option == '3':
            high_price = get_max_price(prices_list)
            print("Highest numver in the List : ",high_price)
        elif option == 'q':
            return
        else:
            print("Invalid Option")
            continue

def add_price(prices_list,price):
    prices_list.append(price)
    return prices_list

def get_average_price(prices_list):
    if not prices_list:
        return 0
    return sum(prices_list)/len(prices_list)

def get_max_price(prices_list):
    if not prices_list:
        return 0
    return max(prices_list)
    

def main():
    assignment()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()

if __name__ == "__main__": main()