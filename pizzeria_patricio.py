dinero = int(input("Ingrese su monto disponible:\n"))

DINERO_INICIAL = dinero 
total = 0
pedido = []

hawaiana = 150.56
pepperoni = 120.34
mexicana = 160.89
pizza_patricio = 170.55
pizza_amanda = 172.45

queso_extra = 25.00
champiñones = 30.50
pimiento = 20.50
churus = 20.50

print("---LA PIZZERÍA DE PATRICIO---")

while True:
    print(f"1. Hawaiana - {hawaiana}")
    print(f"2. Pepperoni - {pepperoni}")
    print(f"3. Mexicana - {mexicana}")
    print(f"4. Pizza Patricio - {pizza_patricio} ")
    print(f"5. Pizza Amanda - {pizza_amanda}")

    eleccion = int(input("Por favor, indique el número de la pizza de su preferencia:"))
    
    match eleccion:
        case 1:
            print(f"Ha elegido la pizza hawaiana\nTotal a pagar: {hawaiana}")
            dinero -= hawaiana
            print(f"Su monto disponible es: {round(dinero,2)}")
            total += hawaiana
            pedido.append(f"Hawaiana - {hawaiana}")
            break
        case 2:
            print(f"Ha elegido la pizza pepperoni\nTotal a pagar: {pepperoni}")
            dinero -= pepperoni
            print(f"Su monto disponible es: {round(dinero,2)}")
            total += pepperoni
            pedido.append(f"Pepperoni - {pepperoni}")
            break
        case 3:
            print(f"Ha elegido la pizza mexicana\nTotal a pagar: {mexicana}")
            dinero -= mexicana
            print(f"Su monto disponible es: {round(dinero,2)}")
            total += mexicana
            pedido.append(f"Mexicana - {mexicana}")
            break
        case 4:
            print(f"Ha elegido la pizza Patricio\nTotal a pagar: {pizza_patricio}")
            dinero -= pizza_patricio
            print(f"Su monto disponible es: {round(dinero,2)}")
            total += pizza_patricio
            pedido.append(f"Pizza Patricio - {pizza_patricio}")
            break
        case 5:
            print(f"Ha elegido la pizza Amanda\nTotal a pagar: {pizza_amanda}")
            dinero -= pizza_amanda
            print(f"Su monto disponible es: {round(dinero,2)}")
            total += pizza_amanda
            pedido.append(f"Pizza Amanda - {pizza_amanda}")
            break
        case _:
            print("Entrada invalida, introduzca un número de nuevo.")

while True:
    print(f"1. Extra queso - {queso_extra}")
    print(f"2. Champiñones - {champiñones}")
    print(f"3. Pimiento - {pimiento}") 
    print(f"4. Churus - {churus}")
    print("5. Sin extra.")
    
    eleccion = int(input("Añada ingredientes extra a su pizza si así lo desea."))
    
    match eleccion:
        case 1: 
            print(f"Ha añadido queso extra\nExtra a pagar: {queso_extra}")
            dinero -= queso_extra
            total += queso_extra
            print(f"Total a pagar: {total}")
            print(f"Su monto disponible es: {round(dinero,2)}")
            pedido.append(f"Queso extra - {queso_extra}")
        case 2: 
            print(f"Ha añadido champiñones\nExtra a pagar: {champiñones}")
            dinero -= champiñones
            total += champiñones
            print(f"Total a pagar: {total}")
            print(f"Su monto disponible es: {round(dinero,2)}")
            pedido.append(f"Extra champiñones - {champiñones}")
        case 3:
            print(f"Ha añadido pimiento extra\nExtra a pagar: {pimiento}")
            dinero -= pimiento
            total += pimiento
            print(f"Total a pagar: {total}")
            print(f"Su monto disponible es: {round(dinero,2)}")
            pedido.append(f"Extra pimiento - {pimiento}")
        case 4:
            print(f"Ha añadido churus\nExtra a pagar: {churus}")
            dinero -= churus
            total += churus
            print(f"Total a pagar: {total}")
            print(f"Su monto disponible es: {round(dinero,2)}")
            pedido.append(f"Extra churus - {churus}") 
        case 5:
            print("De acuerdo, no se añaden extras.")
            break
        case _:
            print("Opción invalida. Por favor, intentelo de nuevo.")
            
if total <= DINERO_INICIAL:
    print("\n---SU PEDIDO---")
    
    print(f"El total de su pedido es: {total}")
    print(f"Su cambio: {dinero}\n")
    
    for i in pedido:
        print(f"-{i}")
        
    print("\n¡Buen provecho!")
    
else:
    print("Lo sentimos, el total de su pedido es más que su monto disponible.")
        
                     
    
    