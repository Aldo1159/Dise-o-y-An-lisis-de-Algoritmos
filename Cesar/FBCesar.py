# Alfabeto que vamos a utilizar
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
# Abrimos el archivo donde esta el mensaje
archivo = open("mensajeCifrado.txt", "r", encoding="utf-8-sig")
mensaje = archivo.read()
archivo.close()
# Aqui vamos a ir probando las diferentes claves
for clave in range(27):
    resultado = ""
    for letra in mensaje:
        # Revisamos si el caracter es una letra del alfabeto
        if letra.lower() in alfabeto:
            # Buscamos en que posicion se encuentra
            posicion = alfabeto.index(letra.lower())
            # Le restamos la clave para descifrar
            nueva_posicion = (posicion - clave) % 27
            nueva_letra = alfabeto[nueva_posicion]
            # Si estaba en mayuscula la dejamos igual
            if letra.isupper():
                resultado = resultado + nueva_letra.upper()
            else:
                resultado = resultado + nueva_letra
        else:
            # Los espacios y signos se quedan como estan
            resultado = resultado + letra
    # Imprimimos cada intento para ver cual tiene sentido
    print("Clave:", clave)
    print(resultado)
    print("-------------------")
