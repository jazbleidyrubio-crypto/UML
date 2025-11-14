class Revista:
    
    def __init__(self,titulo,categoria,precio):
        
        self.titulo = titulo
        self.categoria = categoria
        self.precio = precio
        
    def mostrar_informacion (self):
            return f"Titlo:{self.titulo}, Categoria:{self.categoria}, Precio:{self.precio}"