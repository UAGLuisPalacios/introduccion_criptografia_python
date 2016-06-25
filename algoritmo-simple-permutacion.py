from utilidades_cifrado import Archivos
from utilidades_cifrado import GeneradorLlaves
from utilidades_cifrado import Cifrado
import hashlib


utilidadm = Cifrado()


archivo = Archivos()
print " "
print "Texto normal: "
lineas = archivo.lineas("textos/algoritmo-simple-permutacion/test")

for l in lineas:
    print l

textocifrado = utilidadm.cifrar_algoritmosimple_permutacion(lineas)

print "Texto cifrado: "
print " "
print textocifrado
print " "
print " "

print "MD5: "+ hashlib.md5(textocifrado).hexdigest()