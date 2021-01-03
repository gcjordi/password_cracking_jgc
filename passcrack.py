import hashlib
import msvcrt
encontrado = 0
input_hash = input("Insertar el password hasheado: ")
pass_doc = input("Insertar el diccionario: ")
try:
    pass_file = open(pass_doc, "r")
except:
    print("Error:" + pass_doc + "no ha sido encontrado")
for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()
    if digest == input_hash:
        print("¡Password encontrado! \ El password es: " + palabra)
        encontrado = 1
        break
if not encontrado:
    print("Password no encontrado en el archivo " + pass_doc)
msvcrt.getch()