from utilidades_cifrado import Archivos
from utilidades_cifrado import Llaves
from utilidades_cifrado import Estadisticas
from pprint import pprint

texto = Archivos()
llavero = Llaves()

mensaje = texto.lineas("textos/permutaciones/test")
llaves = llavero.llaves(texto.lineas("textos/permutaciones/claves"))

#frecuencia = Estadisticas()
#tabla = frecuencia.analizarfrecuencia(mensaje)
#tabla = frecuencia.analizarpares(mensaje)

texto.sustituir(llaves, mensaje)