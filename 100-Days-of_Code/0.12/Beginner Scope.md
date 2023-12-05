# **Beginner Scope**

## *Local  vs. Global Scope*

The below is an explanation into ***scope***. The first block (1) is the code entered and the second block (2) is the output.

1. ``` 
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

```

2. ```
enemies inside function: 2
enemies outside function: 1

```
