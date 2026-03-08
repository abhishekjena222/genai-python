def assignment():
    print("Control Flow Assignment")

# Discount Rules (if/elif/else)
def task1():
    print("\n -- task 1 : Discount Rules (if/elif/else) --")

    # 1 take order amount using input()
    # order_amount = int(input("enter the amount: "))

    # 3 input validation 
    try:
        order_amount = int(input("enter the amount: "))
        # order_amount = int(order_amount)
    except (ValueError,TypeError) as e:
        print("Invalid Input")
        return

    # 2 apply discount rule and print the amount
    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount =  0.07
    else:
        discount = 0

    sub_total = order_amount - (order_amount * discount)

    print("The discount amount is", sub_total)

    # extra add 5% after discount and print subtotal, tax, and final total
    tax = sub_total + (order_amount * 0.05)
    final_total = sub_total + tax

    print("Tax : ",tax)
    print("Final total : ",final_total)


# task 2 : Process Multiple order (for loop)
def task2():
    print("\n -- task 2 : Process Multiple order (for loop) --")

    # 1 order_amount, discount, final amount
    orders = [1200, 2500, 800, 1750, 3000]
    total_revenue = 0
    order_with_discount = 0

    for order_amount in orders:
        if order_amount >= 2000:
            discount = 0.15
        elif order_amount >= 1500:
            discount = 0.10
        elif order_amount >= 1000:
            discount =  0.07
        else:
            discount = 0

        if discount > 0:
            order_with_discount += 1

        final_amount = order_amount  * (1 - discount)
        total_revenue += final_amount

        print(f"Order : {order_amount} | Discount : {discount*100}% | Final : {final_amount}")


    # 2 total revenue after discount
    print("\nTotal revenue after discount: ",total_revenue)

    # extra numbers of order with discount > 0
    print("Total orders with discount is : ",order_with_discount)


# task 3 : User Menu (while loop  - break/continue)
def task3():
    print("\n -- task 3 : User Menu (while loop  - break/continue) --")

    # 1 while loop with option 1,2,q ; 1: add amount to a running list, 2: show amount and discount aount, q: quit
    # 2 continue the loop on invalid input, break or exit at q
    orders = []
    print("Menu: \nEnter 1 to add amount \nEnter 2 to show the table \nEnter q to exit")


    while True:
        option = input("enter your preference: ")
        if (option == 'q'):
            break
        elif (option == '1'):
            try:
                input_amount = int(input("Enter the amount: "))
            except ValueError:
                print("Invalid Input")
                continue

            orders.append(input_amount)
            print("Orders : ",orders)
        elif (option == '2'):
            for order_amount in orders:
                if order_amount >= 2000:
                    discount = 0.15
                elif order_amount >= 1500:
                    discount = 0.10
                elif order_amount >= 1000:
                    discount =  0.07
                else:
                    discount = 0
                print(f"Amount: {order_amount} | Total with discount : {order_amount * (1 - discount)}")
        else:
            print("Invalid preference")
            continue







def main():
    assignment()
    # task1()
    # task2()
    task3()


if __name__ == "__main__": main()