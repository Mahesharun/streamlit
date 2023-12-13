import streamlit as st

def find_largest_number(num1, num2, num3):
    numbers = [num1, num2, num3]
    largest_number = max(numbers)
    return largest_number

def main():
    st.title("Largest Number Finder")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest Number"):
        largest_number = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()

