class Producto:
    
    def __init__(self,precio,titulo,autor,editorial,año_edicion,preferencias):
        
        self.precio = precio
        self.titulo =  titulo
        self.autor = autor
        self.editorial = editorial
        self.año_edicion = año_edicion
        self.preferencias = preferencias
        
    def vender (self):
            print(f"vendiendo producto:{self.titulo} con precio :{self.precio}") 
        
    def comprar (self):
            print (f"Comprando producto:{self.titulo} del autor: {self.autor}")
        
    def ver_catalogo(self):
            print(f"Catalogo:{self.titulo}") 