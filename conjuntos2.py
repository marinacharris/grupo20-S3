# operaciones ente los conjuntos
carbohidratosNat = {'papa', 'yuca', 'ñame'}
carbohidratosProc = {'Harina de trigo', 'Pasta'}
# operadores de los conjuntos
# | Unión
# & Interseccion
# - Diferencia
# ^ Diferencia simétrica
print(len(carbohidratosProc))

print(carbohidratosProc|carbohidratosNat)
print(carbohidratosProc&carbohidratosNat)
print(carbohidratosProc-carbohidratosNat)
print(carbohidratosProc^carbohidratosNat)

print(carbohidratosProc.union(carbohidratosNat)) # Esto es lo mismo que la linea 10

Lista = [2,4,5,3,7,9,3,4,5,2,2,8,8,8,5,4,1,2,4,0]
Conjunto1 = set(Lista)
print(Conjunto1)

