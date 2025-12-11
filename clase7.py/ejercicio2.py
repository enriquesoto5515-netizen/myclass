class Circulo:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.radio = 0
        
    def leer(self):
        self.posx = int(input("Ingrese posicion X: "))
        self.posy = int(input("Ingrese posicion Y: "))
        self.radio = int(input("Ingrese la Radio : "))
        
    def mostrar(self):
        print("========== datos del circulo ===========")
        print(f"Posicion X: {self.posx}")
        print(f"Posicion Y: {self.posy}")
        print(f"Radio: {self.radio}")
        
    def area(self):
        area = 3.1416 * self.radio * self.radio
        print(f"El area es : {area}")
    
    def circunferencia(self):
        cir = 2 * 3.1416 * self.radio
        print(f"La circunferencia es: {cir}")
        
    def diametro(self):
        diametro = 2 * self.radio
        print(f"El diametro es: {diametro}")
    

circulo1 = Circulo()
circulo1.leer()
circulo1.mostrar()
circulo1.area()
circulo1.circunferencia()
circulo1.diametro()
    
    
circulo2 = Circulo()
circulo2.leer()
circulo2.mostrar()
circulo2.area()
circulo2.circunferencia()
circulo2.diametro()
    
    
    
    
    
    
    
    
    
    
    