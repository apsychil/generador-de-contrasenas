#Por: Mateo Misas para el porfolio.
#Visita: https://mateomisas.simple.ink/

import secrets
import string

def generador_de_contrasena():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    alphabet = letters + digits + special_chars
    
    def obtener_longitud_contrasena():
        while True:
            try:
                longitud = int(input("Número de carácteres de la contraseña (máximo 40): "))
                if longitud > 40:
                    raise ValueError("Error: Recuerda que el máximo es 40.")
                elif longitud <= 0:
                    raise ValueError("Error: El número de caracteres no puede ser 0 o negativo.")
                break
            except ValueError as e:
                print(str(e))
        return longitud
    
    longitud = obtener_longitud_contrasena()
    
    pwd = ''
    for i in range(longitud):
        pwd += ''.join(secrets.choice(alphabet))
    
    print("La contraseña generada es:")
    print(pwd)
    
    with open("passwords.txt", "a") as f:
        f.write(pwd + "\n")
    print("Contraseña generada y guardada en passwords.txt")
    
if __name__ == '__main__':
    print("\nBienvenido al generador de contraseñas\n")
    print("Este programa va a brindarte una contraseña, según el número de carácteres que deseas que posea.")
    generador_de_contrasena()
