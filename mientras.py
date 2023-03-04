controladora = 100

print('***Empanadas el machetico***')
print('***______________________***')
print('1. Agregar sabor de empanada')
print('2. Mostrar sabor de empanada')
print('3. Cambiar sabor de empanadas')
print('0. SALIR')

# pass -> sirve para omitir procesos y dejar pasar con el next

while controladora != 0 :
    empanada=None
    controladora = int(input("Digita una opcion: "))
    if controladora == 1:
        empanada =input("Digita el sabor: ")
    elif controladora == 2:
        print(f"El sabor es {empanada}")
    elif controladora == 3:
        empanada = input("Cual es el sabor: ")
    elif controladora == 0:
        print("vuelve pronto")
    else:
        print('Opcion invalida')