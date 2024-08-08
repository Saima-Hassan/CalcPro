import streamlit as st

# Title
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Select operation
operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division: {result}")
        else:
            st.error("Error: Division by zero is not allowed")