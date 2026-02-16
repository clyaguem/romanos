diccionario = {"Jose":10,"María":20,"Pedro":15}
print("María: ",diccionario.get("María"))


for c,v in diccionario.items():
    print(c+"-"+str(v))

valor = "{:0>4d}".format(3) #significa{:agregame 0 delante del (3), el número (3) tiene que tener 4 de longitud y tiene que ser decimal entero}. Si el símbolo es este: < se agregan por detrás.
print(valor)