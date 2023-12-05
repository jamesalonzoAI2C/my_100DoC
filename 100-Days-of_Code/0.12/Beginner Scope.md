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
