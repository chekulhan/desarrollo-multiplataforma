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


# Actividades
from functools import reduce

numbers = [3, 7, 2, 9, 5]

# encontrar el número más grande usando reduce
"""
3 vs 7 → 7
7 vs 2 → 7
7 vs 9 → 9
9 vs 5 → 9
"""

cart = [
    {"name": "apple", "price": 2, "qty": 3},
    {"name": "banana", "price": 1, "qty": 5},
    {"name": "orange", "price": 3, "qty": 2}
]

# resultado esperado:
# apple: 2 * 3 = 6
# banana: 1 * 5 = 5
# orange: 3 * 2 = 6

# total = 17



# Respuestas
from functools import reduce

max_value = reduce(lambda acc, x: acc if acc > x else x, numbers)

print(max_value)

from functools import reduce

total = reduce(
    lambda acc, item: acc + (item["price"] * item["qty"]),
    cart,
    0
)

print(total)  # 17