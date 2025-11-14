class Editorial:
    
    def __init__(self,nombre,direccion,telefono):
        
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        
    def vender(self):
        print(f"EDITORIAL:{self.nombre}con direccion:{self.direccion}con numero de telefono{self.telefono}")