from utilidades_cifrado import Archivos
from utilidades_cifrado import GeneradorLlaves
from utilidades_cifrado import Estadisticas
from pprint import pprint

texto = Archivos()
generador = GeneradorLlaves()
print " "
print " "
mensaje = texto.lineas("textos/permutaciones/test")
LLAVE = ['I', 'B', 'C', 'D', 'U', 'F', 'G', 'H', 'Q', 'J', 'K', 'L', 'M', 'N', 'E', 'P', 'R', 'O', 'S', 'T', 'A', 'V', 'W', 'X', 'Y', 'Z']
generador.testclave(LLAVE, mensaje)