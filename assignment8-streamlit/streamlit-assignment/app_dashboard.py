import streamlit as st

def assignment():
    print("\n -- Task 4 - Sales Dashboard -- ")

def main():
    assignment()
    st.title("Simple Sales Dashboard")
    st.text("Use the sidebar to navigate between different sections of the dashboard.")
    months = ["January", "February", "March", "April", "May", "June"]
    sales = {"January": 1000, "February": 1500, "March": 1200, "April": 1800, "May": 2000, "June": 1700}
    # display selected month sales using st.matric() or st.write()
    selected_month = st.sidebar.selectbox("Select a month to view sales:", months)
    st.metric(label=f"Sales for {selected_month}", value=f"${sales[selected_month]:,}")
    # display a bar chart of sales data using st.bar_chart()
    st.subheader("Sales Data")
    st.bar_chart(list(sales.values()))



if __name__ == "__main__":
    main()