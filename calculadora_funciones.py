print("---CALCULADORA MEJORADA---")

#Se definen las funciones
def suma(numero1,numero2):
    return numero1 + numero2

def resta(numero1,numero2):
    return numero1 - numero2

def multiplicación(numero1,numero2):
    return numero1 * numero2

def división(numero1,numero2):
    return numero1 / numero2

def modulo(numero1,numero2):
    return numero1 % numero2

def exponente(numero1,numero2):
    return numero1 ** numero2

while True:
    #Se le pide al usuario que elija una opción y se evalúa
    print("Por favor, elija una opción:")
    print("1- Suma.")
    print("2- Resta.")
    print("3- Multiplicación.")
    print("4- División.")
    print("5- Módulo.")
    print("6- Exponente.")
    print("7- Salir.")
    
    #Se le pide al usuario un número de opción
    eleccion = int(input("Teclee un número y pulse ENTER: "))
    
    match eleccion:
        case 1:
            print("Ha elegido suma.")
        case 2:
            print("Ha elegido resta.")
        case 3:
            print("Ha elegido multiplicación.")
        case 4:
            print("Ha elegido división.")
        case 5:
            print("Ha elegido módulo.")
        case 6:
            print("Ha elegido exponente.")
        case 7:
            print("Saliendo de la calculadora.")
            break
        case _:
            print("Error. Por favor, inténtelo de nuevo.")
    
    #Se le piden los números al usuario.
    numero_1 = float(input("Especifique el primer operando:\n"))
    numero_2 = float(input("Especifique el segundo operando:\n"))
    
    match eleccion:
        case 1: 
            resultado = round(suma(numero_1, numero_2), 2)
            print(f"El resultado de sumar {numero_1} más {numero_2} es: {resultado}.")
        case 2:
            resultado = round(resta(numero_1, numero_2), 2)
            print(f"El resultado de restar {numero_1} menos {numero_2} es: {resultado}.")
        case 3:
            resultado = round(multiplicación(numero_1, numero_2), 2)
            print(f"El resultado de multiplicar {numero_1} por {numero_2} es: {resultado}.")
        case 4:
            resultado = round(división(numero_1, numero_2), 2)
            print(f"El resultado de dividir {numero_1} entre {numero_2} es: {resultado}.")
        case 5:
            resultado = round(modulo(numero_1, numero_2), 2)
            print(f"El resto de la división de {numero_1} entre {numero_2} es: {resultado}.")
        case 6:
            resultado = round(exponente(numero_1, numero_2), 2)
            print(f"{numero_1} elevado a {numero_2} es: {resultado}.")
                    
                