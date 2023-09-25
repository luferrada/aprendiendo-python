# 1. Saludo personalizado:
# Escribe tu nombre en una variable y luego imprime un saludo personalizado en
# la consola usando esa variable.
nombre = "Lucas"
print(f"Hola, {nombre}, te presento mi programa.")

print(f"Adios, {nombre}, gracias por leer.")


# 2. Edad futura:
# Escribe tu edad en una variable y luego imprime tu edad en 5 años más.
# Tambien en 8 y 13 años más.
edad = 27

print(f"voy a tener {edad + 5} años en 5 años mas")
print(f"voy a tener {edad + 8} años en 8 años mas")
print(f"voy a tener {edad + 13} años en 13 años mas")


# 3. Suma de 2 números:
# Ingresa 2 números en variables y luego imprime la suma de esos 2 números en
# la consola.
numero_1 = 999
numero_2 = 456
resultado_suma = numero_1 + numero_2
print(resultado_suma)

resultado_division = resultado_suma / 2
print(resultado_division)


# 4. Cálculo de area de un rectángulo:
# Ingresa la longitud y el ancho de un rectángulo en variables y luego imprime
# el área del rectángulo en la consola.
ancho = 4
longitud = 7
area_rectangulo = ancho * longitud
print(f"hay un rectangulo de {ancho} x {longitud}")
print(f"y su area es {area_rectangulo}")


# 5. Conversión de monedas:
# Ingresa una cantidad de dinero en pesos chilenos en una variable y luego
# imprime la conversión a dólares en la consola.
pesos_chilenos = input("ingresa el valor de pesos chilenos: ")
pesos_chilenos = int(pesos_chilenos)

print(f"el valor que se ha ingresado es de {pesos_chilenos}")
tasa_dolares = 0.0011
resultado = pesos_chilenos * tasa_dolares
print(resultado)


# 6. Números pares e impares:
# Ingresa un número en una variable y luego imprime si es par o impar en la
# consola.
numero = input("escribe un numero aqui: ")
numero = int(numero)
print(numero % 2 == 0)


# 7. Índice de masa corporal:
# Ingresa tu peso y tu altura en variables y luego imprime tu índice de masa
# corporal en la consola.

# 8. Propina de un restaurante:
# Ingresa el total de la cuenta de un restaurante en una variable y luego
# imprime el 10% de propina y el total de la cuenta con propina en la consola.