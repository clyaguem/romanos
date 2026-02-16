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
"""
diccionario_entero_a_romano = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM"
}

"""
Crearemos un error
Clase: molde o estructura de código donde dentro se pueden guardar varias funciones y variables
"""
class RomanNumberError(Exception):
    pass

# a) 1994 -> MCMXCIV
def entero_a_romano(numero):
    numero = str(numero) #Transformamos en cadena el valor 1994 para poder descomponerlo
    if len(numero) == 3: #Si la longitud de número es igual a 3
        numero = "0" + numero #Añade un 0 delante del número
    elif len(numero) == 2: #Si la longitud de número es igual a 2
        numero = "00" + numero #Añade dos 0 delante del número
    elif len(numero) == 1: #Si la longitud de número es igual a 1
        numero = "000" + numero #Añade tres 0 delante del número

    numero_list = list(numero) #Guardardamos en una lista la cadena resultante del paso anterior ["1","9","9","4"]
    valor_romano = " " #Guarda los resultados obtenidos con cada vuelta del while
    contador = 0
    valor_num = 1000

    while contador < len(numero_list): #Mientras contador sea menor que la longitud de la lista de números
        numero_list[contador] = int(numero_list[contador])*valor_num #El valor se convierte a integro y se multiplica por la variable "valor_num"(1000)
        valor_romano += diccionario_entero_a_romano.get(numero_list[contador],"") #Busca el valor en el diccionario unificado, si no encuentra el valor añade una cadena vacía
        contador += 1 #El contador se mueve una posición
        valor_num /= 10 #En cada vuelta, la variable valor_num se divide entre 10 pasando de millares a centenas, decenas...

    
    return valor_romano

print(entero_a_romano(3))

#1994
#["1","9","9","4"]
