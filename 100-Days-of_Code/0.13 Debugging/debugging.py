## (1) Original is below

number = int(input()) # Which number do you want to check?

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
## Fixed code is below

# number = int(input()) # Which number do you want to check?

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

## (2) Original is below

# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

## Fixed code is below

# year = int(input()) # Which year do you want to check?

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

## (3) Original is below

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

## Fixed code is below

# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)