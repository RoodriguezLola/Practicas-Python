#6. Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
#con los número pares y otras con los que son impares. Imprima las listas al terminar de
#procesarlas.
chain= [1, 7, 0, 2]
chain_peers= []
chain_odd= []
for num in chain:
    if((num % 2) == 0):
        chain_peers.append(num)
    else:
        chain_odd.append(num)

print("lista pares: ")
for num in chain_peers:    
    print(num)
print("lista impares")
for num in chain_odd:    
    print(num)