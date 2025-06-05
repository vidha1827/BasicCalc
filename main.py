import pandas as pd

def calculator():
    while True:
        #ask user for operation
        operation = input("\nChoose operation (add / subtract / multiply / divide) or type 'exit' to quit: ").lower()

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue

        try:
            #get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        #perform calculation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = "Infinity (division by zero)" if num2 == 0 else num1 / num2

        #display using DataFrame
        df = pd.DataFrame({
            'Number 1': [num1],
            'Number 2': [num2],
            'Operation': [operation.capitalize()],
            'Result': [result]
        })

        print("\nCalculation Result:")
        print(df)

if __name__ == "__main__":
    calculator()
