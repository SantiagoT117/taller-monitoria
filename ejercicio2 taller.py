
def hello():
    menu = 'Bienvenido al cajero automatico'
    return menu

def cards_list():
    global tarjetas
    tarjetas = [{"numero": "1234567890", "clave": "1234", "saldo": 10000},
                {"numero": "0987654321", "clave": "4321", "saldo": 5000},
                {"numero": "5678901234", "clave": "5678", "saldo": 20000}]


def entrance():
    global numero_tarjeta
    numero_tarjeta = input("Por favor, ingrese el número de su tarjeta: ")


def valid_card():
    global tarjeta_valida, tarjeta_seleccionada
    tarjeta_valida = False
    for tarjeta in tarjetas:
        if tarjeta["numero"] == numero_tarjeta:
            tarjeta_valida = True
            tarjeta_seleccionada = tarjeta
            break


def process():
    if tarjeta_valida:
        clave = input("Por favor, ingrese su clave: ")

        if clave == tarjeta_seleccionada["clave"]:
            
            if tarjeta_seleccionada["saldo"] >= 10000:
                monto = int(input("Por favor, ingrese el monto a retirar: "))

                if monto <= tarjeta_seleccionada["saldo"]:
                    tarjeta_seleccionada["saldo"] -= monto

                    
                    print(f"Retire su dinero: ${monto}")
                else:
                    print("El monto a retirar es mayor que el saldo disponible en la tarjeta.")
            else:
                print("El saldo de la tarjeta es menor que $10,000.")
        else:
            print("La clave ingresada no coincide con la clave asociada a la tarjeta.")
    else:
        print("El número de tarjeta ingresado no se encuentra.")


if __name__ == '__main__':
    print(hello())
    cards_list()
    entrance()
    valid_card()
    process()
    
     #integrantes: Laura Sofia Rivera Arias 2380712 y Santiago Torres Rojas 2380301