#Exception Handling
'''print("x")
try:
  print(x)
except:
  print("An exception occurred")'''
#Many Exceptions Name error
'''try:
    A=10
    B=0
    print(A/B)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")'''
#You can use the else keyword to define a block of
#code to be executed if no errors were raised
'''try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")'''
'''try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")'''
'''try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
#Raise an exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")'''
'''x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")'''
#User Input Validation – Handling Wrong Input
'''try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as e:
    print("Invalid input:", e)'''
#API Key Missing – Handling Missing Credentials
'''import os

try:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise EnvironmentError("API_KEY is missing in environment variables.")
    print("API Key Loaded Successfully")
except EnvironmentError as e:
    print("Error:", e)'''
'''class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Invalid payment amount.")
    print("Payment processed successfully.")

try:
    process_payment(100)  # Invalid amount
except PaymentFailedError as e:
    print("Transaction failed:", e)'''
# IoT Devices – Handling Sensor Data Errors
'''import random

try:
    temperature = random.choice([25, 20, None])  # Simulate sensor data
    if temperature is None:
        raise ValueError("Sensor failed to read temperature.")
    print("Temperature:", temperature, "°C")
except ValueError as e:
    print("Sensor Error:", e)
#Logging Errors in an Application
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)

try:
    value = 10 / 0
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)
    print("An error occurred. Check logs for details.")'''
#Financial Transactions – Handling Insufficient Balance
'''class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds!")
        self.balance -= amount
        print(f"Withdrawal successful! New balance: ${self.balance}")

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print("Transaction failed:", e)'''
#Handling Invalid Date Formats
from datetime import datetime

try:
    date_str = "2024-04-31"  # Invalid date
    valid_date = datetime.strptime(date_str, "%Y-%m-%d")
except ValueError as e:
    print("Invalid date format:", e)









        






  
