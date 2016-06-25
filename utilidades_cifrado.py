import itertools
import time


ALFABETO = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


class Cifrado:
	r = 7
	rn = 0
	newline = ""
	secondline =""
	#PERMUTACION = ['O','B','C','D','E','F','G','H','I','J','K','L','M','N','A','P','Q','R','S','T','U','V','W','X','Y','Z']
	PERMUTACION = list("AICFKGNLUHTXZSPDOJVYEMWQBR")
	tabla = dict(zip(ALFABETO,PERMUTACION))
	result = ""

	def algoritmo_simple_permutacion(self, caracter,rn):
		if caracter in ALFABETO:
			n_algoritmo = ALFABETO.index(caracter) + rn
			modulo_caracter_alfabeto_original = n_algoritmo%26
			self.rn = modulo_caracter_alfabeto_original
			if(self.PERMUTACION[modulo_caracter_alfabeto_original]!=ALFABETO[modulo_caracter_alfabeto_original]):
				self.rn = ALFABETO.index(self.PERMUTACION[modulo_caracter_alfabeto_original])
			#print caracter + ", el modulo del caracter cifrado es: " + str(self.rn)
			return modulo_caracter_alfabeto_original
		else:
			pass
		return

	def cifrar_algoritmosimple_permutacion(self, lineas):
		resultado = ""
		print " "
		print " "
		print " "
		self.rn = self.r

		self.newline=""
		self.newline+=str(self.rn)+","

		self.secondline+=ALFABETO[self.rn]

		self.result+=ALFABETO[self.rn]
		for linea in lineas:
			for caracter in linea:
				a = self.algoritmo_simple_permutacion(caracter,self.rn)
				if(a==0 or a):
					self.newline+=str(a)+","
					self.secondline+=self.PERMUTACION[a]
					self.result+=self.PERMUTACION[a]
				elif(caracter == '\n'):
					self.result+=caracter
			#print self.newline
			#print self.secondline
			self.newline=""
			self.secondline=""
		#print self.result
		return self.result

	#self.cifrar(lineas, "asp")


class Archivos:
	memoriatxt = []
	newline = ""

	alfabeto = {}

	def cargartexto(self, ruta_archivo):
		with open(ruta_archivo, 'r') as txt:
			texto = txt.read()
			return texto

	def lineas(self, ruta_archivo):
		with open(ruta_archivo, 'r') as txt:
			content = txt.readlines()
			#print " "
			for index,i in enumerate(content):
				content[index]= content[index].upper()
				#print content[index]
			#print " "
			return content

	def sustituir(self, llaves, lineas):
		CRIBA = "SISTEMASCREADOS"

		start = time.time()
		#print "TEXTO CODIFICADO: " + str(lineas)
		for index,LLAVE in llaves.items():
			self.newline=""
			tabla = dict(zip(ALFABETO,LLAVE))
			#print "PERMUTACION: " + str(tabla)
			#print LLAVE
			for linea in lineas:
				self.newline=""
				for caracter in linea:
					if caracter in LLAVE:
						value = tabla[""+caracter]
						self.newline+=value
					else:
						self.newline+=caracter
				#print self.newline
				resultado = self.newline.find(CRIBA)
				#if (resultado!=-1):
					#print "index: " + str(index) + ", " +  self.newline
			#print self.newline
		end = time.time()
		print(end - start)


class GeneradorLlaves:
	alfabetos = {}

	def sustituirlocal(self, LLAVE, lineas, index):
		CRIBA = "SISTEMASCREADOS"
		self.newline=""
		tabla = dict(zip(ALFABETO,LLAVE))
		#print "PERMUTACION: " + str(tabla)
		#print LLAVE
		for linea in lineas:
			self.newline=""
			for caracter in linea:
				if caracter in LLAVE:
					value = tabla[""+caracter]
					self.newline+=value
				else:
					self.newline+=caracter
			#print self.newline
			resultado = self.newline.find(CRIBA)
			if (resultado!=-1):
				print " "
				print " "
				print "LLAVE: " + str(LLAVE)
				print "index: " + str(index) + ", " +self.newline
				print " "
				print "TEXTO DESCIFRADO:"
				print " "
				for linea in lineas:
					self.newline=""
					for caracter in linea:
						if caracter in LLAVE:
							value = tabla[""+caracter]
							self.newline+=value
						else:
							self.newline+=caracter
					print self.newline
				return
		#print self.newline


	def simulacion(self, corte, lineas):
		start = time.time()
		abecedario_estatico = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[corte:])
		n=0
		for x in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[0:corte]):
			tupla_abecedario = x + abecedario_estatico
			#self.alfabetos.update({len(self.alfabetos):list(tupla_abecedario)})
			self.sustituirlocal(tupla_abecedario, lineas, n)
			n+=1
		#for key,values in self.alfabetos.iteritems():
			#print (key, values)
		#print(" ")
		#return self.alfabetos
		end = time.time()
		print " "
		print " "
		print "TIEMPO UTILIZADO: " + str(end - start)
		print " "
		print " "

	def permutacionAlfabeto(self, letras, mensaje):
		posiciones = []
		PERMUTACION = ALFABETO
		for caracter in letras:
			posiciones.append(ALFABETO.index(caracter))

		for y in itertools.permutations(letras):
			n=0
			for caracter in posiciones:
				#print y[n]
				PERMUTACION[caracter]= y[n]
				n+=1

			print PERMUTACION
			#hacer sustitucion
			#print PERMUTACION
			PERMUTACION = ALFABETO
			pass
		pass



class Estadisticas:

	def analizarfrecuencia(self, lineas):
		tabla = dict.fromkeys(ALFABETO, float(0))
		espacios = 0
		total = 0
		for linea in lineas:
			total+=len(linea)
			for caracter in linea:
				if caracter in ALFABETO:
					tabla[""+caracter]+=1
				else:
					espacios+=1
		for x in tabla:
			tabla[""+x] = float((tabla[""+x] / (total-espacios)) * 100)
		for key, value in sorted(tabla.iteritems(), key=lambda (k,v): (v,k), reverse=True):
			print "%s: %s" % (key, value)
		return tabla

	def analizarpares(self, lineas):
		pares = {}
		espacios = 0
		total = 0
		char1 = ""
		char2 = ""
		found = 0
		for linea in lineas:
			for caracter in linea:
				if caracter in ALFABETO:
					if char1 == "":
						char1=caracter
					else:
						char2 = char1
						char1=caracter
					if(found!=0):
						par = char2+char1
						if par in pares:
							pares[par]+=1
							total+=1
						elif not par in pares:
							pares.update({par:float(1)})
							total+=1
					else:
						found = 1
				else:
					espacios+=1
		print(" ")
		for key, value in sorted(pares.iteritems(), key=lambda (k,v): (v,k), reverse=True):
			print (key, value, "porcentaje: " + str((pares[""+key] / total) * 100) +" %")
		print(" ")