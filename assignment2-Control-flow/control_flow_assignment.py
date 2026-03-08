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




def main():
    assignment()
    task1()


if __name__ == "__main__": main()