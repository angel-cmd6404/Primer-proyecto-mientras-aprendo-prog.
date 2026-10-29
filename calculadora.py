print("=== MI PRIMER CALCULADORA===")

numero1 = float(input("Escribe el primer numero: "))
operacion = input("Operación (+, -, *, /): ")
numero2 = float(input("Escribe el segundo numero: "))

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
     resultado = numero1 - numero2
elif operacion == "*":
      resultado = numero1 * numero2
elif operacion == "/":
     if numero2 != 0:
          resultado = numero1 / numero2
else:
      resultado = None
      print("Operacion invalida.")
if resultado is not None:
    print("Resultado:", resultado)


