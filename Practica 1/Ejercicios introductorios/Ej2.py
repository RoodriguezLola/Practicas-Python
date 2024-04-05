#2. Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
#luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.
#ºF = (ºC · 1,8) + 32

temperature= float(input("Ingrese una temperatura en grados celsius: "))
degrees= 0
degrees= (temperature * 1.8) + 32
print(f'La temperatura que ingreso son: {degrees} grados Fahrenheit')