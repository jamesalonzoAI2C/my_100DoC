# Debugging

Grace Hopper found an actual moth in a relay she was using to run code. That was the first documented time someone "debugged".

## TTPs - Quickly Identify and Remove Bugs

### Describe the Problem

This is as simple as decribing what the error is or what the bug is doing that is preventing the code from running correctly.

```python
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")

my_function()
```

When the function is called, the function is not printing "You got it?"

- What is the for-loop doing?
    - i is for the integer. I is looping through every integer starting from 1 and ending at ~~20~~.
- When is the function meant to print "You got it"?
    - when i gets to 20, it is suppose to print.
- What are your assumptions about i?
    - When i gets to 20, it will equal 20. Therefore 20 == 20, thus printing.

*range()*
> If  I write range(4). The iteration will begin at 0 and end at 3. The last number is omitted. Therefore in our code block, the loop ends at 19 and never actually reaches 20.
>> the corrected code would be to change the range to 21 **or** i == 19.

### Reproduce the bug

When you encounter a bug once and not the next time, it becomes a really difficult bug to fix. Change the code just enough for when it is ran, the same error produces every time.

```python
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
```
*Describing the Problem*
When the code is ran, it will successfully run at time and then at other times with will give a list index out of range erorr. 

- How do you reproduce the bug?
    - for dice_num, change the value to "6" instead of randint. it will reproduce the erorr everytime.
    - changing the value to a number between 1 and 5, no error will produce. instead the function will run and generate the corresponding dice number. 

*randint()*
> randint() includes both endpoints unlike the range function. So randint(1, 6) will give 6 integers beginning form 1 and endng to include 6. Unlike range(1, 6) will only return 1 to 5.
>> To fix the code, simply shift the numbers down from 1,6 to 0,5. This will properly pull the corret index from the **list** of dice_imgs. Remeber lists are indexed and to properly pull items from a list we need to call their correct index. 

### Play Computer

Look at each line of code and follow the logic and check what it will evaluate to.

```python
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
```

- use pythontutor or thonny to really evaluate the code like a computer. Follow each single step logically. If the input is 1994, replace the first "year" with 1994 and evaluate if it will be true or false. So on and so forth. 

- line 2 checks if int(year) is less than 1994 and line 4 checks if int(year) is greater than 1994.
    - the code never directly checks the year 1994 only 1993 and below or 1995 or higher.
    - the code also never checks for years 1980 and under.

### Fix the Errors

This step is pretty obvious. When the editor or console is giving an error. Fix the error before moving on. It is important to run and check your code regularly to test for bugs and errors. 