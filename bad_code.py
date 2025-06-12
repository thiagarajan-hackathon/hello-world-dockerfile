# bad_code.py - intentionally poor code for SonarQube testing

def insecure_function():
    user_input = "2 + 2"
    result = eval(user_input)  # Use of eval is a security risk
    print("Result is:", result)

def unused_variables():
    x = 10  # Unused variable
    y = 20  # Unused variable
    print("This function has unused variables.")

def potential_bug():
    numbers = [1, 2, 3]
    print(numbers[5])  # IndexError: list index out of range

insecure_function()
unused_variables()
potential_bug()
