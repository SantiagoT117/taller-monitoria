import random

def hola():
    menu = 'Bienvenido a comprobación suma digitos'
    return menu

def aleatorio():
    global num_str
    num = random.randint(10000, 99999)
    print(f'Número aleatorio de 5 cifras: {num}')

    num_str = str(num)


def suma():
    suma_primeros_tres = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
    print(f'Suma primeros 3 números: {suma_primeros_tres}')
    suma_ultimos_dos = int(num_str[3]) + int(num_str[4])
    print(f'Suma ultimos 2 númros: {suma_ultimos_dos}')

    if suma_primeros_tres == suma_ultimos_dos:
        print("La suma de los primeros 3 dígitos es igual a la suma de los últimos 2 dígitos.")
        
    else:
        print("La suma de los primeros 3 dígitos no es igual a la suma de los últimos 2 dígitos.")


if __name__ == '__main__':
    print(hola())
    print()
    aleatorio()
    suma()
    
    #integrantes: Laura Sofia Rivera Arias 2380712 y Santiago Torres Rojas 2380301
    


