print ("Calculador de IMC")
print ( "Escriba du nombre ")

nombre_usuario = input ()

print ("escriba su peso")
peso_usuario = input ()
peso_usuario = float (peso_usuario)

print ( "escriba su altura ")

altura_usuario = input()
altura_usuario = float (altura_usuario)

imc = peso_usuario / (altura_usuario ** 2)

print (f"su IMC sr {nombre_usuario}  es : {imc}")

if imc < 18.5:
    print ("peso bajo")

elif 18.5 <= imc <24.9:
    print("peso normal")

elif 25 <= imc < 29.9:
    print ("sobrepeso ")

else:
    ("obesidad")