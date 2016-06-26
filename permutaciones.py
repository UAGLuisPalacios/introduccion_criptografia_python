from utilidades_cifrado import Archivos
from utilidades_cifrado import GeneradorLlaves
from utilidades_cifrado import Estadisticas
from pprint import pprint

texto = Archivos()
generador = GeneradorLlaves()
print " "
print " "
mensaje = texto.lineas("textos/permutaciones/test")
#frecuencia = Estadisticas()
#tabla = frecuencia.analizarfrecuencia(mensaje)
#tabla = frecuencia.analizarpares(mensaje)

letras = tuple('ACDELORT')
#ACDELOR -> LLERO:
#LLAVE: ['D', 'B', 'R', 'A', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'C', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#index: 2050, ALABTCONIBOSPCOGCEMERLASDIGITELASANALLEROCETOCIONEBIONEL

#ACDELORS -> ALLERO
#LLAVE: ['D', 'B', 'R', 'A', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'C', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#index: 13714, ALABTSONIBOCPSOGSEMERLACDIGITELACANALLEROSETOSIONEBIONEL
#NUEVO
#ABECEDARIO = ['A','N','C','D','E','F','G','H','I','J','K','L','M','B','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#ABDELNOR
#ABCDELNORS
generador.permutacionAlfabeto(letras, mensaje)