
import os
import sys

# Hardcoded credentials (Security Hotspot)
USERNAME = "admin"
PASSWORD = "123456"

# Unused variables
x = 42
y = "unused"

# Use of eval (Security Vulnerability)
def insecure_eval():
    user_input = input("Enter a command: ")
    eval(user_input)

# Poor exception handling
def risky_division():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a / b)
    except:
        print("Something went wrong")

# Potential bug: IndexError
def out_of_bounds():
    items = [1, 2, 3]
    print(items[5])

# Function with too many return paths (Code Smell)
def complex_logic(n):
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    else:
        return "many"

# Unreachable code
def unreachable():
    return
    print("This will never be printed")

# SQL injection risk
def insecure_sql(user_id):
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    print("Executing query:", query)

# Main function to call all others
def main():
    insecure_eval()
    risky_division()
    out_of_bounds()
    complex_logic(3)
    unreachable()
    insecure_sql("1 OR 1=1")

if __name__ == "__main__":
    main()
