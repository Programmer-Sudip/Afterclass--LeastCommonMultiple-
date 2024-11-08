def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating LCM
result = lcm(num1, num2)

print(f"The Least Common Multiple of {num1} and {num2} is {result}")
