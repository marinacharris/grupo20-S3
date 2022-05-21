# Los conjuntos son colecciones de datos en las cuales se alamacenan varios 
# elementos
# No están ordenados, son inmutables y no permiten valores duplicados
conjunto = {'Cali', 'Barranquilla', 'Bucaramanga'}
print(type(conjunto))
print(conjunto)
conjunto2 = {2,4,5,3,3,3,7,7,9}
print(conjunto2)
# conjunto3 = {3, 5.0, True, 'Carlos', [1,2,3]} un conjunto no puede contener una lista
conjunto3 = {3, 5.0, True, 'Carlos'}
conjunto4 = set((3, 7, (9,8,7))) #Nótese el doble paréntesis, es obligatorio
print(conjunto3)
print(conjunto4)
conjunto3.add('Pedro')
conjunto3.remove(5.0)
print(conjunto3)


