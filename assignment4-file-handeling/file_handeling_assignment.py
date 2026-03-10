def assignment():
    print("File Handeling")   

dir = "assignment4-file-handeling/"
def task1():
    print("\n -- task 1 - Write sales record to a file -- ")
    sales = [1200, 450, 980, 1500, 3000]
    file = dir+'sales_data.txt'

    with open(file,'w') as f:
        f.write("\n".join(map(str, sales)))

    with open(file,'r') as f:
        content = f.read().splitlines()
        print(",".join(content))
        
def task2():
    print("\n -- task 2 - Read File in Different ways -- ")
    with open(dir+"sales_data.txt","r") as f:
        print("read : ",f.read())

        f.seek(0)
        content = f.readline()
        print("readline : ",content)

        f.seek(0)
        content = f.readlines()
        print("readlines : ",content)
        line_list = list(map(int, content ))
        print(line_list)

def task3():
    print("\n -- task 3 - Append new sales -- ")
    with open(dir+"sales_data.txt","a") as f:
        f.write("\n5000\n2500\n1700")

    with open(dir+"sales_data.txt","r") as f:
        print(f.read())
        f.seek(0)
        print("Total number of lines : ",len(f.readlines()))


def task4():
    print("\n -- task 4 - Geberat esummery report from file -- ")
    with open(dir+"sales_data.txt","r") as f:
        sale_list = list(map(int, f.readlines()))
        print(sale_list)
        print("Total sales : ",sum(sale_list))
        print("Highest sale : ",max(sale_list))
        print("Lowest sale: ",min(sale_list))
        print("Average sale : ",sum(sale_list)/len(sale_list))

        
def task5():
    print("\n -- task 5 - Create product info file -- ")
    with open(dir+"products.txt","w+") as f:
        f.write("ProductName | Price")
        for i in range(3):
            product_name = input(f"Enter {i+1} product name : ")
            price = input(f"Enter the price : ")
            f.write("\n"+product_name+" | "+price)
        
        f.seek(0)
        content = f.read()
        print("Text : ",content)
        
    
def task6():
    print(" -- task 6 - Read file safely -- ")
    file_name = input("Enter the file name : ")
    import os

    if os.path.exists(dir + file_name):
        with open(dir + file_name) as f:
            print(f.read())
    else:
        print("File not found. Please check the filename.")

def task7():
    print("\n -- task 7 - Mini Project : Export discount price -- ")
    prices = {
        "Mouse" : 500,
        "Keyboard" : 800,
        "Monitor" : 7000,
        "Pendrive" : 400,
        "Camera" : 5000
    }

    with open(dir+"discount_report.txt","w+") as file:
        discount =int(input("How much discount do you want : "))/100
        file.write("Product | Original price | Discount price")
        for product,price in prices.items():
            file.write(f"\n{product} | {price} | {price*(1-discount)}")
        file.seek(0)
        print(file.read())


def main():
    assignment()
    option = input("Witch task do you wanna run : ")
    if option == '1':
        task1()
    elif option == '2':
        task2()
    elif option == '3':
        task3()
    elif option == '4':
        task4()
    elif option == '6':
        task6()
    elif option == '5':
        task5()
    elif option == '7':
        task7()
    else:
        print("Invalid option")


if __name__ == "__main__" : main() 