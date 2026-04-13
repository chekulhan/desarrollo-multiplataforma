# Demostracion de any y all
nums = [True, True, True]

x = all(nums)
print(x)

nums = [True, True, True]

x = any(nums)
print(x)


# Actividad
notas = [6, 7, 8, 5, 9]
# Mostrar un valor si todos han aprobado (True). Recordar que puedes usar list comprehension para sacar un array con [True, True, False, ...]


# Avanzado
passwords = ["abc123", "123456", "password", "securePass1"]
# Mostrar un valor True si todas las contraseñas contienen un digito (char.isdigit()). 