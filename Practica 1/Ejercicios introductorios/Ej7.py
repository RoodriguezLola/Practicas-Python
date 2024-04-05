#7. Escribe un programa que tome una lista de números enteros como entrada del usuario.
#Luego, convierte cada número en la lista a string y únelos en una sola cadena,
#separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
#de 3 de la cadena fina

numbers=input("Ingrese una lista de numeros (separados por espacios): ").split()
numbers= [int(num) for num in numbers]
chain= ''
for num in numbers:
    if(num % 3 == 0):
        continue
    else:
        chain+= str(num)
chain= ' - '.join(chain)
print(chain)