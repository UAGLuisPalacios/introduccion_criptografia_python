from utilidades_cifrado import Archivos
from utilidades_cifrado import GeneradorLlaves
from utilidades_cifrado import Estadisticas
from pprint import pprint

texto = Archivos()
generador = GeneradorLlaves()

mensaje = texto.lineas("textos/permutaciones/test")
print mensaje
#llaves = generador.sustituirlocal(texto.lineas(llave, mensaje,0)

#frecuencia = Estadisticas()
#tabla = frecuencia.analizarfrecuencia(mensaje)
#tabla = frecuencia.analizarpares(mensaje)

letras = tuple('AYZ')
generador.permutacionAlfabeto(letras, mensaje)