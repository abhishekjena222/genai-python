import streamlit as st

def assignment():
    print("\n -- Task 1 - Basic Stream App --")


def main():    
    # assignment()
    st.title("Welcome to Streamlit!")
    name = st.text_input("Enter your name:")
    greet_me = st.button("Greet Me")
    if greet_me and name:
        st.write(f"Hello, {name}! Welcome to Streamlit!")



if __name__ == "__main__": main()