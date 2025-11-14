class Usuario:
    def __init__(self,nombre,apellido,n_cuenta,direccion,login,password):
        
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
        
    def enviar_sugerencia(self):
        print("sugerencia enviada")
        
    def leer (self):
        print("el usuario esta leyendo el contenido")
        
    def comprar (self):
        print("compra realizada con exito")
        
    def vender (self):
        print("se vendio correctamente")
        
    def realizar_reclamacion(self):
        print("revision enviada.pronto se inspeccionara ")
    def monstra_dato(self):
        print(f"(nombre: {self.nombre} {self.apellido}) - (cuenta: {self.n_cuenta}) - (direccion: {self.direccion}) - (datos del usuario: {self.login} {self.password}) ")