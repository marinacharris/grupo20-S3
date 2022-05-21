# Son estructuras de datos, y se utilizan para almacenar varios elementos,
# que pueden ser de distintos tipos de datos. 
# Son mutables y son indexadas

MarcasCarros = ['Audi','Chevrolet','Renault','Toyota']
datosPersonales = ['Carlos', 40, True]
print(MarcasCarros)
print(datosPersonales)

frutas = list(('manzana','pera','fresa'))
print(frutas)
frutas[2]='piña'
print(frutas)
frutas.append('coco')
frutas.append('patilla')
frutas.append((4,5,2,9,8))
print(frutas)

for i in frutas:
    print(i)
