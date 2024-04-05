#4. Cree un programa que dada una lista de números imprima sólo los que son pares.
#Nota: utilice la sentencia continue donde haga falta
chain= [1, 7, 0, 2]
for num in chain:
    if((num % 2) == 0):
        print(num)
    else:
        continue