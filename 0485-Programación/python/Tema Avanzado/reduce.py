# Deberias usar reduce cuando:
# - Quieres un valor al final
# - La operacion es cumulativo (sum, product, max, etc.)

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]

result = reduce(add, numbers)

print(result)

"""
Step 1: x=1, y=2 → 3
Step 2: x=3, y=3 → 6
Step 3: x=6, y=4 → 10
"""



from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)  # 10



# reduce
reduce(lambda x, y: x + y, numbers)

# preferred
sum(numbers)
