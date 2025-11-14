class Novedades:
    
    def __init__(self,tema,clasificacion):
        
        self.tema = tema
        self.clasificacion = clasificacion
        
    def cambiar_clasificacion(self):

            
            return f"Clasificacion cambiada a: {self.clasificacion}"
        
    def mostrar_informacion(self):
            return f"Tema:{self.tema}, Clasificacion:{self.clasificacion}"