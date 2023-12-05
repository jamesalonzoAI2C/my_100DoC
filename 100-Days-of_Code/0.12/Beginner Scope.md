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
The variable declared above the code block is a *global* variable and the variable assigned inside the functions is a *local* variable.

Below is another example. 
```python
def drink_potion():
    potion_strength = 2
    print(potion_stregnth)

drink_potion()
```
The above will print the integter "2". However if we try and call the variable outide the drink_potion function, it will raise an error. It raises an error because the potion_strength variable is local to the fucntion. Meaning the variable is only accesible within the function.

```python
def drink_potion():
    potion_strength = 2
    print(potion_stregnth)

drink_potion()
print(potion_strength)
```
>    print(potion_stregnth)
NameError: name 'potion_stregnth' is not defined

The rule is global variables are accessible within functions. They must be declared before the function that is trying to access the variable. They are accessible regardless of how deep they get nested within a function. 

**The concept of *scope* also applies to fucntions. It is called *Namespace*. If function (b) is created within function a. You will not be able to call function b becuase it is local to function (a)**

## Modifying Global Scope

1. 
```python 
enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```
Must use the keyword "global" before calling the variable to modying global scope, locally. **Do not do it. Not recommended**
Instead, modying the function to ***return***. Look at the example below.

```python
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")
```
