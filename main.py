"""
1. Crear una función que pase de entero >0 y <4000 a romano
2. Cualquier otra entrada de error
3. Límite 3999

Casos de prueba:
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError() el valor debe ser menor a 4000
c) "unacadena" -> RomanNumberError() debe ser un entero

M -> 1000 
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I -> 1
"""

"""
Creamos unos diccionarios para poder tener la equivalencia en números de los romanos
Lo dividimos en unidades, decenas, centenas y millares para poder abarcar todos los números que queremos
"""
diccionario = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

unidades = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
decenas = {10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC"}
centenas = {100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM"}
millares = {1000:"M",2000:"MM",3000:"MMM"}

"""
Crearemos un error
Clase: molde o estructura de código donde dentro se pueden guardar varias funciones y variables
"""
class RomanNumberError(Exception):
    pass

# a) 1994 -> MCMXCIV
def entero_a_romano(numero):
    numero = str(numero) #Transformamos en cadena el valor 1994 para poder descomponerlo
    numero_list = list(numero) #Guardardamos en una lista la cadena resultante del paso anterior ["1","9","9","4"]
    valor_romano = " " #Guarda los resultados de las condiciones
    for i in range(0,len(numero_list)): #Recorremos con el índice la variable "número" para poder saber si son millares, centenas, decenas o unidades
        if i == 0: #Si el indice está en la posición 0 debería ser millar
            numero_list[i] = int(numero_list[i]) * 1000 #Si se cumple la condición anterior, el valor de la posición 0 se transforma en integro y se multiplica por 1000
            valor_romano += millares.get(numero_list[i])
        if i == 1: #Si el indice está en la posición 1 debería ser millar
            numero_list[i] = int(numero_list[i]) * 100 #Si se cumple la condición anterior, el valor de la posición 1 se transforma en integro y se multiplica por 100
            valor_romano += centenas.get(numero_list[i])
        if i == 2: #Si el indice está en la posición 2 debería ser millar
            numero_list[i] = int(numero_list[i]) * 10 #Si se cumple la condición anterior, el valor de la posición 2 se transforma en integro y se multiplica por 10
            valor_romano += decenas.get(numero_list[i])
        if i == 3:
            numero_list[i] = int(numero_list[i])
            valor_romano += unidades.get(numero_list[i])
        
    print(valor_romano)


    
    
    
    
    return "MCMXCIV"

entero_a_romano(1994)

#1994
#["1","9","9","4"]
