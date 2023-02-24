if True:
    print("Se ejecuta sin hacer una comparativa")

if False:
    print("Nunca se ejecuta")

pet = input("Tu mascota favorita: ")
if pet == "perro":
    print("¡Bien, tu mascota es perro!")
elif pet == "gato":
    print("¡Bien, tu mascota es gato!")
elif pet == "pez":
    print("¡Bien, tu mascota es péz!")
else:
    print("¡Lo siento, tu mascota no es correcto!")

'''
stock = int(input("Ingrese el numero de stock: "))

if stock >= 100 and stock <= 1000:
    print("¡Bien, el stock es correcto!")
else:
    print("¡Lo siento, el stock no es correcto!")
'''