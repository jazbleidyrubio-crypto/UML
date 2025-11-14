class Articulo_Segunda_Mano:
    
    def __init__(self,titulo,clasificacion,tema,vendedor,precio):
        
        self.titulo = titulo
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor
        self.precio = precio
        
    def mostrar_informacion (self):
            return (f"Titulo:{self.titulo}, Clasificacion:{self.clasificacion}, fTema:{self.tema}, Vendedor:{self.vendedor}, Precio:{self.precio}")