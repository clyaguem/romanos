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
diccionario_romano_a_entero = {"M": 1000,"D": 500,"C": 100,"L": 50,"X": 10,"V": 5,"I": 1}

diccionario_entero_a_romano = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM"
} #Creamos unos diccionarios para poder tener la equivalencia en números de los romanos

"""
Clase: molde o estructura de código donde dentro se pueden guardar varias funciones y variables
"""

regla_restas = {"I":("V", "X"), "X":("L", "C"), "C": ("D", "M")}

class RomanNumberError(Exception):
    pass

def romano_a_entero(romano:str)->int:
    list_romano = list(romano) #Transformamos el número romano de la variable en lista para poder recorrerlo y manipularlo después
    valor_entero = 0 #Guarda los resultados obtenidos con cada vuelta del for
    caracter_anterior = "" #Variable para comparar caracteres de la posición actual con la anterior
    contador_repeticiones = 0 #Contador para calcular la cantidad de repeticiones de carácteres
    caracter_ante_anterior = "" #

    for caracter in list_romano:
        if caracter == caracter_anterior:

            if caracter == "D" or caracter == "L" or caracter == "V": #Si el caracter actual es igual que el caracter anterior
                raise RomanNumberError("Los caracteres 'D' 'L' y 'V' no se pueden repetir") #Lanza el siguiente error

            contador_repeticiones += 1 #Suma uno al contador de repeticiones
            if contador_repeticiones > 2: #Si el acumulado del contador de repeticiones es mayor a 2
                raise RomanNumberError("No se puede repetir el valor mas de tres veces") #Lanza el siguiente error
       
        else:
            contador_repeticiones = 0 #Si el caracter actual es distinto al caracter anterior, pone el contador a 0

        if caracter_anterior and diccionario_romano_a_entero.get(caracter_anterior,0) < diccionario_romano_a_entero.get(caracter,0): #Si el caracter no es un str vacío y el caracter anterior es menor al caracter actual, entra a la regla de las restas

            if caracter_anterior in "VLD": #Si el caracter anterior está en "VLD", lanza error
                raise RomanNumberError("V, L y D nunca se pueden restar")

            if caracter not in regla_restas[caracter_anterior]: 
                raise RomanNumberError(f"{caracter_anterior} solo se puede restar de {regla_restas[caracter_anterior][0]} y {regla_restas[caracter_anterior][1]}")


            valor_entero -= diccionario_romano_a_entero.get(caracter_anterior,0)*2 # valor entero es igual a valor entero menos caracter anterior por 2(siempre entra entra el la variable al menos 2 veces)

            if (caracter_anterior == caracter_ante_anterior) and caracter_anterior in "IXC": 
                raise RomanNumberError("I,X,C ya no pueden restarse porque tienen dos repeticiones") 

        caracter_ante_anterior = caracter_anterior
        caracter_anterior = caracter #La variable caracter anterior se sobreescribe con el caracter actual
        valor_entero += diccionario_romano_a_entero.get(caracter,0) #A valor entero se le sumpa el valor del caracter actual

    return valor_entero

def entero_a_romano(numero:int)->str:
    if numero < 0 or numero > 3999: #Ponemos el límite estipulado, solo se puede llegar a 3999, si es mayor lanza error
        raise RomanNumberError("El limite esta entre mayor a 0 y 3999")
    
    if numero == 0: #Si el número es 0, devuelve cadena vacía
        return ""
    numero = "{:0>4d}".format(numero) #significa{:agregame 0 delante del (número), dicho (número) tiene que tener 4 de longitud y tiene que ser decimal entero}
    numero_list = list(numero) #Guardardamos en una lista la cadena resultante del paso anterior ["1","9","9","4"]
    valor_romano = "" #Guarda los resultados obtenidos con cada vuelta del while
    contador = 0
    valor_num = 1000

    while contador < len(numero_list): #Mientras contador sea menor que la longitud de la lista de números
        numero_list[contador] = int(numero_list[contador])*valor_num #El valor se convierte a integro y se multiplica por la variable "valor_num"(1000)
        valor_romano += diccionario_entero_a_romano.get(numero_list[contador],"") #Busca el valor en el diccionario unificado, si no encuentra el valor añade una cadena vacía
        contador += 1 #El contador se mueve una posición
        valor_num /= 10 #En cada vuelta, la variable valor_num se divide entre 10 pasando de millares a centenas, decenas...

    
    return valor_romano
