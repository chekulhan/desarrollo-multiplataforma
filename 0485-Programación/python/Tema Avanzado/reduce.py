# Deberias usar reduce cuando:
# - Quieres un valor al final
# - La operacion es cumulativo (sum, product, max, etc.)

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]

result = reduce(add, numbers)

print(result)


from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)  # 10



# reduce
reduce(lambda x, y: x + y, numbers)

# preferred
sum(numbers)
