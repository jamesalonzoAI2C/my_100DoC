# Debugging

Grace Hopper found an actual moth in a relay she was using to run code. That was the first documented time someone "debugged".

## TTPs - Quickly Identify and Remove Bugs

### Describe the Problem

- What is the for-loop doing?
> i is for the integer. I is looping through every integer starting from 1 and ending at 20.
- When is the function meant to print "You got it"?
>  when i gets to 20, it is suppose to print.
- What are your assumptions about i?
> When i gets to 20, it will equal 20. Therefore 20 == 20, thus printing.

```python
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")

my_function()
```
*** range *** 
> If write range(4). The iteration will begin at 0 and end at 3. The last number is omitted. Therefore in our code block, the loop ends at 19 and never actually reaches 20.
