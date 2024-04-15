class Aplicacion:
    def saludar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Hola, {nombre}!")

    def contar_numeros(self):
        num = int(input("ingrese un numero: "))
        for i in range(1, num + 1):
            print(i)

    def calculadora_basica(self):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        operacion = input("Ingrese la operacion: ")

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: La división por cero no está permitida.")
                return
        else:
            print("Error: Operación desconocida.")
            return

        print(f"El resultado es {resultado}.")

# Crear una instancia de la clase Aplicacion y llamar a los métodos
app = Aplicacion()
app.saludar_usuario()
app.contar_numeros()
app.calculadora_basica()