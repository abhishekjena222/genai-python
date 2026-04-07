import streamlit as st

def assignment():
    print("\n -- Task 3 - Product Form -- ")

def main():
    # assignment()
    st.title("Product Form")
    products = ()
    # using slidebar to enter product name , cagegory (selectbox with 3-5 options), price
    product_name = st.text_input("Enter product name:")
    category = st.selectbox("Select product category:", ["Electronics", "Clothing", "Books", "Home & Kitchen", "Sports"])
    price = st.number_input("Enter product price:", min_value=0.0, step=0.01)
    submit = st.button("Submit")
    if submit:
        if product_name and price > 0:
            st.success(f"Product '{product_name}' in category '{category}' with price ${price:.2f} has been submitted successfully!")
            products += ({"Product Name": product_name, "Category": category, "Price": f"${price:.2f}"},)

        else:
            st.error("Please enter a valid product name and price.")
    
    st.subheader("Submitted Products")
    st.table(products)


if __name__ == "__main__":
    main()