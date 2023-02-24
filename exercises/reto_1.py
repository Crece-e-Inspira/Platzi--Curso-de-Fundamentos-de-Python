# Si un numero es par o impar

usr_num = float(input("Numero: "))
divisible = (usr_num + 2) / 2

print(divisible.is_integer())

if divisible.is_integer():
    print("El numero es PAR!")
else:
    print("El numero es IMPAR!")