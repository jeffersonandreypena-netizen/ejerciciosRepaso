# Ejemplo de tipado fuerte en Python

x=10        #entero (int)
y="5"       #cadena (str)

#Esto generará un error
#print (x+y)

#Python no comvierte a cadena "5" en número automaticamente.

#Para convertir la cadena "5" en número, debes usar la función int(), esto es, hacerlo de forma explicita
print (x+int(y))