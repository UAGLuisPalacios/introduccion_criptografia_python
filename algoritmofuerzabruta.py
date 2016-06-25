import itertools
from utilidades_cifrado import Archivos, GeneradorLlaves
archivo = Archivos()
lineas = archivo.lineas('textos/act6-simulacion/test')

generador = GeneradorLlaves()

llaves = generador.simulacion(5, lineas)
#sustitucion = archivo.sustituir(llaves, lineas)