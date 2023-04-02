nmr1=2
nmr2=4
result= nmr1 + nmr2
result= str(result)
print( "el resultado de la suma es " + result)


#.FIND ES PARA BUSCAR EL NUMERO DE LA LETRA BUSCADA
message="Hola Ernesto"
search_substring= message.find("Ernesto")
print(search_substring)


message="Hola Ernesto"
extract_substring= message [1:8]
print(extract_substring)

#COMPARACION TRUE O FALSE

message_one = "Hola"
message_two = "Hoa"
print(message_one == message_two)

#PALABRAS RESERVADAS DE PYTHON ***PRINT***

prinT = 5
Print = 6
result = prinT + Print

print(result)

#OPERADORES ARITMETICOS 
#SUMA(+) RESTA(-) MULTIPLIACION(*) EXPONENTE(**) MODULO(%)
#DIVISION(/) DIVISION ENTERA(//)

print("SUMA:")

number_one= 5
number_two=8

result= number_one + number_two

print("El resultado de la suma es: " + str(result))

print("RESTA:")

number_one= 8
number_two=5

result= number_one - number_two

print("El resultado de la resta es: " + str(result))

print("MULTIPLICACION:")

number_one= 8
number_two=5

result= number_one * number_two

print("El resultado de la multiplicacion es: " + str(result))

print("EXPONENTE:")

number_one= 8
exponente=5

result= number_one ** exponente

print("El resultado de la exponente es: " + str(result))

print("MODULO O RESTO:")

number_one= 30
number_two=8

result= number_one % number_two

print("El resultado del modulo o resto es: " + str(result))

print("DIVISION:")

number_one= 8
number_two=4

result= number_one / number_two

print("El resultado de la division es: " + str(result))

print("DIVISION ENTERA:")

number_one= 8
number_two=4

result= number_one // number_two

print("El resultado de la division entera es: " + str(result))

# TIPOS DE COMENTARIOS
# ALMOHADILLA
" COMILLAS" "SOLO SE PUEDE COMENTAR UN UNA LINEA" 
"""COMENTARIO MULTILINEA
SE PUEDE 
COMENTAR
EN TODO
LAS LINEAS
SIN PROBLEMA
YA
"""

#TIPOS DE DATOS EN PYTHON

"""
ENTEROS Y LARGOS
FLOTANTES
NUMEROS COMPLEJOS
CADENAS
BOLEANOS
"""
#DESCRIPCION

"""
NUMEROS ENTEROS : "INT" NUMEROS NATURALES
NUMEROS DECIMALES: "FLOAT" DECIMALES
NUMEROS COMPLEJOS: "COMPLEX" 
CADENAS O STRINGS: TEXTO ENCERRADO ENTRE COMILLAS
BOOLEANOS: "BOOL" TIENE 2 VALORES TRUE O FALSE 
"""

#TIPO DE DATO ENTERO O LARGO

number= 15
print(number, type(number) ) #TYPE LE PUSE PARA SABER EL TIPO DE DATO

#TIPO DE DATO FLOTANTE

number_floaT= 15.5
print(number_floaT, type(number_floaT) ) #TYPE LE PUSE PARA SABER EL TIPO DE DATO

#TIPO DE DATO NUMERO COMPLEJO 
# ESTE TIPO DE DATO ES MAS
#PARA USO DE INGIENERIA O DESARROLLO E INVESTIGACION DE CIENCIAS

number_compleX= 5 + 6j
print(number_compleX, type(number_compleX)) #TYPE LE PUSE PARA SABER EL TIPO DE DATO

#tipo de dato string

name= "Mark"
print(name, type(name))

#TIPO DE DATO BOOLEANO

verdadero_falso= 3 == 3
print(verdadero_falso, type(verdadero_falso))







