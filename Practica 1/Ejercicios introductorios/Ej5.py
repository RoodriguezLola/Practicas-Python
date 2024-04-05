#5. Implementa un programa que solicite al usuario que ingrese una lista de números.
#Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
#Nota: utilice la sentencia break cuando haga falta.

numbers=input("Ingrese una lista de numeros (separados por espacios): ")
chain= numbers.split()
chain= [int(num) for num in chain]

for num in chain:
    if(num < 0):
        break
    else:    
        print(num)