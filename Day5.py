#Python Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#Creating and calling a Function
'''def my_function():
  print("Hello from a function")

my_function()'''
'''def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")'''
'''def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")'''
'''def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")'''
'''def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")'''
#Default Parameter Value
'''def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")'''
#Passing a List as an Argument
'''def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)'''
#Return Values
'''def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))'''
#The pass Statement
'''def myfunction():
  pass'''
#To specify that a function can have
#only positional arguments, add , / after the arguments
'''def my_function(x, /):
  print(x)

my_function(3)'''
#Recursion
'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)'''
#Function to Find the Factorial of a Number
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")'''
#Function to Return Fibonacci Series (Using Recursion)
'''def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = fibonacci(n - 1)
    fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

print(fibonacci(10))  # First 10 Fibonacci numbers'''
#Function to Find the GCD (Greatest Common Divisor)
'''import math

def gcd(a, b):
    return math.gcd(a, b)  # Using built-in method

print(gcd(48, 18))'''
#Function to Count Vowels in a String
'''def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

print(count_vowels("Hello World"))'''
#Function to Check if a String is a Palindrome
'''def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("Hello"))  # False'''
#Function to Find the Sum of Digits of a Number (Using Recursion)
'''def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # 10 (1+2+3+4)
#Function to Find the Maximum Number in a List
def find_max(lst):
    return max(lst)

numbers = [3, 5, 7, 2, 8, 10]
print(find_max(numbers)) ''' 
#Function to Reverse a List
'''def reverse_list(lst):
    return lst[::-1]

numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))'''
#Function to Remove Duplicates from a List
'''def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))
#Function to Merge Two Sorted Lists
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

a = [1, 3, 5]
b = [2, 4, 6]
print(merge_sorted_lists(a, b))
#Function to Check if a Number is an Armstrong Number
def is_armstrong(n):
    digits = list(map(int, str(n)))
    return sum(d ** len(digits) for d in digits) == n

print(is_armstrong(153))  
print(is_armstrong(123))'''
#calculator
# Function for addition








'''def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Function for modulus
def modulus(a, b):
    return a % b

# Function for exponentiation
def exponent(a, b):
    return a ** b

# Function for floor division
def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b

# Main function to take user input and perform operations
def calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")

    choice = input("Enter choice (1-7): ")

    if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Invalid choice!")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Performing the operation based on user choice
    if choice == "1":
        print(f"Result: {a} + {b} = {add(a, b)}")
    elif choice == "2":
        print(f"Result: {a} - {b} = {subtract(a, b)}")
    elif choice == "3":
        print(f"Result: {a} * {b} = {multiply(a, b)}")
    elif choice == "4":
        print(f"Result: {a} / {b} = {divide(a, b)}")
    elif choice == "5":
        print(f"Result: {a} % {b} = {modulus(a, b)}")
    elif choice == "6":
        print(f"Result: {a} ** {b} = {exponent(a, b)}")
    elif choice == "7":
        print(f"Result: {a} // {b} = {floor_division(a, b)}")

# Call the calculator function
calculator()'''
#Calculator with User-defined Functions










'''def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error! Division by zero." if b == 0 else a / b

def calculator():
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Enter choice (1-4): ")
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice!")
        return
    a, b = map(float, input("Enter two numbers: ").split())
    ops = {"1": add, "2": subtract, "3": multiply, "4": divide}
    print("Result:", ops[choice](a, b))

calculator()'''
#Temperature Converter (Celsius to Fahrenheit & Vice Versa)


















'''def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def temperature_converter():
    print("1. Celsius to Fahrenheit  2. Fahrenheit to Celsius")
    choice = input("Enter choice (1-2): ")
    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temp)}°F")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"Temperature in Celsius: {fahrenheit_to_celsius(temp)}°C")
    else:
        print("Invalid choice!")

temperature_converter()'''
#Simple Interest and Compound Interest Calculator















'''def simple_interest(p, r, t):
    return (p * r * t) / 100

def compound_interest(p, r, t):
    return p * (1 + r/100) ** t - p

def interest_calculator():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time (years): "))

    print(f"Simple Interest: {simple_interest(p, r, t)}")
    print(f"Compound Interest: {compound_interest(p, r, t)}")

interest_calculator()'''
#BMI (Body Mass Index) Calculator












'''def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_checker():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

bmi_checker()'''
#Find LCM and GCD of Two Numbers













'''import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = map(int, input("Enter two numbers: ").split())
print(f"GCD: {gcd(a, b)}")
print(f"LCM: {lcm(a, b)}")'''
#Count the Frequency of Words in a Sentence











from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    return Counter(words)

sentence = input("Enter a sentence: ")
print(word_frequency(sentence))
#Matrix Multiplication using Functions












'''def matrix_multiplication(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        return "Matrix multiplication is not possible"

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

result = matrix_multiplication(A, B)
for row in result:
    print(row)'''
#Python Lambda
'''x = lambda a : a + 10
print(x(5))'''
'''x = lambda a, b : a * b
print(x(5, 6))'''
'''x = lambda a, b, c : a + b + c
print(x(5, 6, 2))'''
#The power of lambda is better shown when
#you use them as an anonymous function inside another function
'''def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))'''
'''def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))'''

'''def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))'''

































