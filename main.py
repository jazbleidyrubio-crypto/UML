from usuario import Usuario
from producto import Producto
from editorial import Editorial
from libro import Libro
from revista import Revista
from novedades import Novedades
from segunda import Articulo_Segunda_Mano
from articulo_online import Articulo_Online
from indexador import indexador
from procesador import Procesador
from hilo import Hilo
from recolector import Recolector
from servidor import Servidor

object_usuario= Usuario("nayarith" ,"páez", "12324", "calle 16 # 7-58" ,"cr7","223444")
object_usuario.monstra_dato()
object_usuario.enviar_sugerencia()
object_usuario.leer()
object_usuario.comprar()

object_usuario.vender()

object_usuario.realizar_reclamacion()
reclamacion= object_usuario.realizar_reclamacion()


object_producto=Producto(precio="35.000",titulo="el dia feliz", autor="nayarith páez",editorial="colombiana",año_edicion="2009",preferencias="real madrid")
object_producto.vender()
object_producto.comprar()
object_producto.ver_catalogo()

object_servidor= Servidor()
mostrar=object_servidor.mostrar_pagina
print(mostrar)
sugerencias=object_servidor.enviar_sugerencias
print(sugerencias)
datos=object_servidor.enviar_datos_de_compra
print(datos)
venta=object_servidor.enviar_datos_de_venta
print(venta)


object_indexador= indexador()
indexar= object_indexador.actualizar_almacen()
enviar= object_indexador.enviar_resultado_busqueda()
print(indexar)
print(enviar)
print("---------------------------------------------------")
object_dato= Procesador()
object_dato.mandar_datos_de_venta()
object_dato.mandar_articulo_online()
print("---------------------------------------------------")
object_dato.enviar_sugerencia_administrador()
print("---------------------------------------------------")
object_dato.modificar_stock()
print("---------------------------------------------------")
object_dato.realizar_cobro()
print("---------------------------------------------------")
object_dato.realizar_pago()
print("---------------------------------------------------")
object_dato.actualizar_catalogo()
print("---------------------------------------------------")
object_dato.realizar_busqueda()
print("---------------------------------------------------")
object_hilo= Hilo()
object_hilo.buscar_novedades()


object_recolector= Recolector()
object_recolector.enviar_novedades()

object_editorial=Editorial(" nick","av 16ce","3233456788")
object_editorial.vender()

object_libro=Libro("gafitas leydi","nayarith","femenino","2000")
object_libro.mostrar_informacion()

object_revista= Revista("vendedora","alacran","2232323")
object_revista.mostrar_informacion()

object_articulo=Articulo_Segunda_Mano("supervivencia","obra literaria","libreria central","djkasdjkas","q34343")
object_articulo.mostrar_informacion()

object_novedad=Novedades("recursos","lanzamiento magico")
object_novedad.cambiar_clasificacion()
object_novedad.mostrar_informacion()

object_art_online=Articulo_Online("nuevas tendencias en literatura ","joel","2324234")
object_art_online.publicar()
object_art_online.mostrar_informacion()