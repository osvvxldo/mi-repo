import random
import string

def generador_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

print("Bienvenido al generador de contraseñas.")

longitud = int(input("De cuantos caracteres quiere su contraseña? "))

contraseña_segura = generador_contraseña(longitud)

print(f"Tu nueva contraseña segura es: {contraseña_segura}")