text = "Ella sabe Python"
#imprime la ubicacion del texto
print(text[0])

#Imprimir el tultimo caracter
size = len(text)

# -1 por que el
print(text[size - 1])

#otra forma
print(text[-1])

#slicing, imprime solo ese rango de posicion
print(text[0:5])

#imprimir hasta el 10, se puede obviar el 0
print(text[:10])

#Imprimir hasta el final
print(text[5:])
print(text[:])
print(text[::-1])

#Saltos
print(text[10:16:1])
print(text[::2])