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


# Categories -- (Sets)
def task2():
    print("\n --- task 2 : Sets ---")

    #1 set of categories
    categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Office"]
    categories_set = set(categories)

    #2 adding a new category to the set and duplicates are ignored
    categories_set.add("gaming")
    categories_set.add("gaming") # duplicate 

    #3 check category exists in the set
    if 'gaming' in categories_set:
        print("gaming category exist in the set")
    else:
        print("gaming category dosen't exist in the set")
    
    #extra total number of unique category in set
    print(" total unique categories: ",len(categories_set))  


# Product Pricing -- (Dictionaries)
def task3():
    print("\n --- task 3 : Dictionaries ---")

    #1 dictionary of product and price
    price_dict = {
        "Laptop":80000,
        "mouse":1200,
        "keyboard":8000,
        "printer":18000,
        "phone":30000,
        "tablet":24000
    }

    #2 add a product, 
    price_dict["camera"] = 22000
    price_dict["moniter"] = 10000

    #update the price of existing,
    price_dict["Laptop"] = 75000

    #remove a product by name
    product_to_remove = "camera"
    if product_to_remove in price_dict:
        del price_dict[product_to_remove]
        print(f"product {product_to_remove} removed from dictionary")
    else:
        print(f"product {product_to_remove} not found in dictionary")

    #3 print average price of all product
    avg_price = sum(price_dict.values()) / len(price_dict)
    print("the average price of products is :",avg_price)

    #extra product with max and min price
    max_prd = max(price_dict, key=price_dict.get)
    min_prd = min(price_dict, key=price_dict.get)

    print("Most expensive product : ",max_prd)
    print("Most expensive product : ",min_prd)





def main():
    # task1()
    # task2()
    task3()

if __name__ == "__main__":
    main()