# **Beginner Scope**

## *Local  vs. Global Scope*

The below is an explanation into ***scope***. Block (1) is the code entered and the block (2) is the output.

1. 
```python 
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

```
2. 
```python
enemies inside function: 2
enemies outside function: 1

```
The variable declared above the code block is a *global* variable and the variable assigned inside the functions is a *local*variable.

Another example is in block (3). 
```python
def drink_potion():
    potion_strength = 2
    print(potion_stregnth)

drink_potion()
```
The above will print the integter "2". However if we try and call the variable outide the drink_potion function, it will raise an error. It raises an error because the potion_strength variable is local to the fucntion.

3. 
```python
def drink_potion():
    potion_strength = 2
    print(potion_stregnth)

drink_potion()
print(potion_strength)
```
>    print(potion_stregnth)
NameError: name 'potion_stregnth' is not defined