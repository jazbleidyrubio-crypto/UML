class Articulo_Online:
    
    def __init__(self,titulo,autor,contenido):
        
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        
    def publicar (self):
            return f"El articulo '{self.titulo}' del autor {self.autor} ha sido publicado correctamente"
        
    def mostrar_informacion(self):
            return f"Titulo:{self.titulo}, Autor:{self.autor}, Contenido:{self.contenido}"