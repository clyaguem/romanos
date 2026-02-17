
"""
diccionario = {"Jose":10,"María":20,"Pedro":15}
print("María: ",diccionario.get("María"))


for c,v in diccionario.items():
    print(c+"-"+str(v))

valor = "{:0>4d}".format(3) #significa{:agregame 0 delante del (3), el número (3) tiene que tener 4 de longitud y tiene que ser decimal entero}. Si el símbolo es este: < se agregan por detrás.
print(valor)
"""

try: #Sirve para controlar errores y hacer que nuestro sistema no falle
    division = 10/0
except Exception as e: #El Exception controla toda la clase de errores de python
        print("error: ",e) #Se puede poner el menaje que queramos

def myException():
      raise IndexError("Esta es mi excepción customizada") #Genero una excepción

myException()
diccionario = { "Jose":10,"Maria":20,"Pedro":15}
#print("Maria: ",diccionario.get(20,""))

valor= 'X'    

if valor in 'VLD':
    print("si se encuentra")