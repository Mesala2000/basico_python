class Calculadora:
    def suma(self,a,b):
        return  a + b

    def resta(self,a,b):
        return a - b



sumaJose = Calculadora()
restaJose=Calculadora()
resultado = sumaJose.suma(a=4,b=9)
print("Resultado de la suma = ", resultado)
print ('El tipo de la suma es ',type(resultado) )
print('Resultado de la resta = ', restaJose.resta(a=4, b=9))


