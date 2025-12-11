import os
# enrique tarqui 
ARCHIVO = "sis211.txt"

def crearArchivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as file:
            pass
        print("Archivo creado.....")
    else:
        print("el archivo Existe .....")

def guardarRegistro():
    print("Ingrese los datos del estudiante : ")
    ru = input("RU: ")
    ci = input("CI: ")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    sexo = input("Sexo: ")
    nota = input("Nota: ")
    
    linea = f"{ru},{ci},{apellido},{nombre},{sexo},{nota}"
    
    with open(ARCHIVO, "a") as file:
        file.write(linea)
    
    print("Registrado correctamente ......")
    
def cargarDatos():
    estudiante = []
    if not os.path.exists(ARCHIVO):
        return estudiante
    
    with open(ARCHIVO, "r") as file:
        for linea in file:
            partes = linea.strip().split(",")
            if len(partes) == 6:
                estudiante.append(partes)
    return estudiante

def mostrar():
    estuantes = cargarDatos()
    print("\n LISTA DE ESTUDIANTES ")
    for e in estuantes:
        print(e)
    print()
    
def modificar():
    estudiantes = cargarDatos()
    ru = input("ingrese RU del estudiante a modificar: ")
    encontrado = False
    
    for i in range(len(estudiantes)):
        if estudiantes[i][0] == ru:
            print("Datos actuales del estudiante: ", estudiantes[i])
            estudiantes[i][2] = input("Ingrese nuevo apellido: ")
            estudiantes[i][3] = input("Ingrese nuevo Nombre: ")
            estudiantes[i][4] = input("Ingrese nuevo Sexo: ")
            estudiantes[i][5] = input("Ingrese nuevo Nota: ")
            
            encontrado = True
            break
        
    if encontrado:
        with open(ARCHIVO, "w") as archivo:
            for e in estudiantes:
                archivo.write(",".join(e)+ "\n")
        print("Resgistro modficado correctamente ")
            
    else:
        print("RU no encontardo...............")
            
    
def menu():
    while True:
        print("\n ============ MENU PRINCIPAL ===============")
        print("1. Crear archivo")
        print("2. Guardar archivo")
        print("3. Mostrar")
        print("4. Modificar")
        print("0. salir")
        
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1": crearArchivo()
        elif opcion == "2": guardarRegistro()
        elif opcion == "3": mostrar()
        elif opcion == "4": modificar()
        elif opcion == "0":
            print("Saliendo del programa....... ")
            break
        else:
            print("opcion no valida......")
    
menu()
    
        
        
    
        

        