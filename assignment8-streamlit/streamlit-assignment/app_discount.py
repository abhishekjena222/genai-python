import streamlit as st
def assignment():
    print("\n -- Task 2 - Discount Calculator -- ")



def main():
    # assignment()
    st.title("Discount Calculator")
    original_price = st.number_input("Enter the original price:", min_value=0.0, step=0.01)
    discount_percentage = st.slider("Select discount percentage:", min_value=0, max_value=50, value=10)
    calculate_discount = st.button("Calculate Discount")
    if calculate_discount:
        if original_price > 0 and discount_percentage >= 0:
            discount_amount = original_price * (discount_percentage / 100)
            discounted_price = original_price - discount_amount
            st.success(f"Discounted Price: ${discounted_price:.2f}")
        else:
            st.error("Please enter a valid original price and discount percentage.")
        st.table({
            "Original Price": [f"${original_price:.2f}"],
            "Discount Percentage": [f"{discount_percentage}%"],
            "Discount Amount": [f"${discount_amount:.2f}"],
            "Discounted Price": [f"${discounted_price:.2f}"]
        })



if __name__ == "__main__":
    main()