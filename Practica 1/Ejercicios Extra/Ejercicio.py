inventory= []
product= []
choose= int(input(f'Ingresar una opcion: ' + '\n' + '1) Agregar un producto '
              + '\n' + '2) Eliminar un producto ' + '\n' + '3) Mostrar el inventario ' 
              + '\n' + '4) Salir del programa ' + '\n'
              + 'Opcion: '))
print(' ')

while(choose != 4):
    match choose:
        case 1: 
            product= []
            name= input('Ingrese el nombre del producto: ')
            stock= int(input('Ingrese el stock del producto: '))
            product.append(name)
            product.append(stock)
            inventory.append([product])

        case 2:   
            name= input('Ingrese el nombre del producto a eliminar: ')
            cant= 0
            while(cant < len(inventory)):
                if(name in inventory[cant][0]):
                    inventory.remove(inventory[cant])
                else:
                  cant += 1

        case 3:
            cant= 0
            while(cant < len(inventory)):
                cant2= 0
                while(cant2 < 1):
                    print(f'producto: ' + str(inventory[cant][cant2]))
                    cant2 += 1
                cant += 1

    print(' ')
    choose= int(input(f'Ingresar una opcion: ' + '\n' + '1) Agregar un producto '
              + '\n' + '2) Eliminar un producto ' + '\n' + '3) Mostrar el inventario ' 
              + '\n' + '4) Salir del programa ' + '\n'
              + 'Opcion: '))
    print(' ')