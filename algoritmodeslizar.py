class deslizamiento:
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    modulo = len(alfabeto)
    r = 19 #esta es la llave inversa con la que se encripto originalmente
    #la llave original es r = 7
    #en python se puede obtener esta llave mediante: r[-19+25] = index 6, (que es posicion 7)
    def SetR(self,valor):
        r = valor

    def deslizar(self, caracter):
        if(caracter in self.alfabeto):
            rd = self.alfabeto.index(caracter) + self.r
            if(rd==self.modulo):
                rd = 0
            elif(rd>self.modulo):
                rd = rd - self.modulo
            return self.alfabeto[rd]
        else:
            return ''.ljust(1)

    def deslizamiento_negativo(self, caracter):
        if(caracter in self.alfabeto):
            rd = self.alfabeto.index(caracter) - self.r
            return self.alfabeto[rd]
        else:
            return ''.ljust(1)

    def encriptarfrase(self, frase):
        newfrase = ""
        for index,caracter in enumerate(frase, start=0):
            newfrase+=self.deslizar(caracter)
        return newfrase

    def operacion_inversa(self, frase):
        newfrase = ""
        for index,caracter in enumerate(frase, start=0):
            newfrase+=self.deslizamiento_negativo(caracter)
        return newfrase


def prueba_algoritmo():
    algoritmo = deslizamiento()
    parrafo1 = "SH BUPCLYZPKHK HBAVUVTH KL NBHKHSHQHYH LZ BUH PUZAPABJPVU KL JBSABYH, JPLUJPH, LKBJHJPVU, HYAL F ALJUVSVNPH HS ZLYCPJPV KL SH OBTHUPKHK, XBL LKBJH HS THZ HSAV UPCLS F MVYTH PUALNYHTLUAL H SH WLYZVUH LU SV PUALSLJABHS, TVYHS, ZVJPHS F WYVMLZPVUHS, HZP JVTV LU SV MPZPJV."
    parrafo2 = "SH BHN OH ZPKV, LZ F ZLNBPYH ZPLUKV, MVYTHKVYH KL OVTIYLZ F TBQLYLZ KL IPLU, KL WYVMLZPVUHSLZ PUZWPYHKVZ LU HSAVZ CHSVYLZ, NLULYHKVYLZ KL IPLULZAHY F WYVNYLZV H SHZ JVTBUPKHKLZ H SHZ XBL ZPYCLU."

    muestra = parrafo1

    print("El alfabeto es modulo: " + str(algoritmo.modulo))
    print("R es: " + str(algoritmo.r))
    frase_encriptada = algoritmo.encriptarfrase(muestra)
    print("respuesta: " + frase_encriptada)
    frase_encriptada2 = algoritmo.encriptarfrase(frase_encriptada)
    print("respuesta: " + frase_encriptada2)