#!/usr/bin/python3

# Task 1: Calculator @codsoft
def calculator(num1,num2,ops):
  result = 0
  if ops == '+':
    result = num1 + num2
  elif ops == '-':
    result = num1 - num2
  elif ops == '*':
    result = num1 * num2
  elif ops == '/':
    result = num1 / num2
  else:
    result = "Give valid ops "
  return result