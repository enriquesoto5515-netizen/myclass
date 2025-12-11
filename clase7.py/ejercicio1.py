class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = ""
        
    def leer(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = input("Ibgrese la edad: ")
         
    def mostrar(self):
        print("======= Mostrando Datos ===========")
        print(f"Nombre: {self.nombre}")
        print(f"Edad : {self.edad} ")
        
    def saludar(self):
        print("======= Saludando ===========")
        print(f"Buenos días, soy {self.nombre} y tengo {self.edad} años")
        
persona1 = Persona()
persona1.leer()
persona1.mostrar()
persona1.saludar()
