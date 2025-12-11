# 20.Realiza una función que reciba una palabra y desplace cada letra una cantidad n de posiciones.

def deplazar(palabra, n):
    nueva = ""
    for c in palabra:
        nueva += chr(((ord(c) - 97 + n) % 26)+97)
    return nueva

palabra = input("ingrese palabra: ")
n = int(input("ingrese n: "))

print("nueva palabra : ",deplazar(palabra,n))
        