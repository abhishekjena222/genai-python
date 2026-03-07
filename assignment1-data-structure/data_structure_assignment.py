def hi():
    print("Hi")

# product collection -- list & tuple
def task1(): 
    print("\n --- task 1 : list & tuple ---")

    #1 list of products
    products = ["Laptop","mouse","keyboard","printer","phone","tablet"]

    #2 tuple for one product
    sample_product = ("Laptop", 80000, "Electronics")

    #3 print 2nd and last product
    print("2nd product:\t",products[1])
    print("Last product:\t",products[-1])

    #4 add two new product
    products.append("moniter")
    products.append("camera")
    print("products: ",products)

    #extra tuple to list, modify charhe, list to tuple
    tmp = list(sample_product)
    tmp[1] = 75000
    sample_product = tuple(tmp)

    print("updated sample_product: ",sample_product)




def main():
    task1()

if __name__ == "__main__":
    main()