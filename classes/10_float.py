import string

x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print(x == y)

''' format(), es equivalente a la función round(x, 2). Para elegir la cantidad de decimales que quiero
en este caso sera con string'''

y_str = format(y, ".2g")
print("Se convierte en 'str'", y_str)

print("*" * 25)
print(y, x)

tolerance = 0.00001
print(abs(x - y))
print(abs(x - y) < tolerance)