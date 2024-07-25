import streamlit as st


def calculator(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 != 0:
            return number1 / number2
        st.error("Division by zero error")
        return "Division by zero error"
    
def main():
    st.title("Simple Calculator")

    number1 = st.number_input("Enter first number", format="%f")
    number2 = st.number_input("Enter second number", format="%f")
    operation = st.selectbox("Select Operation", ["+", "-", "*", "/"])

    result = calculator(number1=number1, number2=number2, operation=operation)
    st.write(f"Result: {result}")


if __name__ == "__main__":
    main()