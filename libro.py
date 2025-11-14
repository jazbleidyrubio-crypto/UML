class Libro:
    
    def __init__(self,titulo,autor,genero,precio):
        
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        
    def mostrar_informacion(self):
           return f"Titulo:{self.titulo}, Autor:{self.autor}, Genero:{self.genero}, Precio:{self.precio}"