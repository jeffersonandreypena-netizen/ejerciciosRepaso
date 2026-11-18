# =====================================================================
#  16.1 EJERCICIOS USANDO SOLO FUNCIONES EN PYTHON
# ---------------------------------------------------------------------
#  Regla del taller: la lógica va dentro de funciones (parámetros,
#  return, llamadas entre funciones y recursión). NO se usan listas,
#  tuplas, sets ni diccionarios.
#
#  Cómo usar este archivo: ejecútalo y elige en el menú el número del
#  ejercicio que quieres probar.
# =====================================================================


# ---------------------------------------------------------------------
# 1. FACTORIAL DE UN NÚMERO
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Definir una función factorial(n) que reciba un entero positivo y
#   retorne su factorial. Toda la lógica debe estar dentro de la función.
#   Ejemplo -> Entrada: 5  |  Salida: 120
#
# EXPLICACIÓN:
# El factorial de n (n!) es n * (n-1) * (n-2) * ... * 1
# Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    resultado = 1                      # Empezamos en 1 porque es el neutro de la multiplicación
    for i in range(1, n + 1):          # i toma los valores 1, 2, 3, ..., n
        resultado = resultado * i      # Vamos acumulando la multiplicación
    return resultado                   # Devolvemos el resultado a quien llamó la función


# ---------------------------------------------------------------------
# 2. CALCULADORA CON FUNCIONES INDEPENDIENTES
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Crear funciones independientes: sumar(a, b), restar(a, b),
#   multiplicar(a, b) y dividir(a, b). Luego una función calculadora()
#   debe pedir los datos y llamar a la función adecuada.
#
# EXPLICACIÓN:
# Cada operación es una función pequeña que recibe a y b y retorna
# el resultado. Luego calculadora() pide los datos y llama a la correcta.
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    # No se puede dividir entre 0, así que lo validamos antes
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b


def calculadora():
    # float() permite ingresar números con decimales
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /): ")

    # Según el símbolo, llamamos a la función que corresponde
    if operacion == "+":
        resultado = sumar(a, b)
    elif operacion == "-":
        resultado = restar(a, b)
    elif operacion == "*":
        resultado = multiplicar(a, b)
    elif operacion == "/":
        resultado = dividir(a, b)
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)


# ---------------------------------------------------------------------
# 3. ¿EL NÚMERO ES PRIMO?
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Definir es_primo(n) que retorne True o False.
#   Debe verificar divisibilidad desde 2 hasta la raíz cuadrada de n.
#
# EXPLICACIÓN:
# Un primo solo es divisible entre 1 y él mismo.
# Basta con revisar divisores desde 2 hasta la raíz cuadrada de n.
# Truco: en vez de calcular la raíz, usamos la condición i * i <= n
# (es lo mismo que i <= raíz de n, pero sin importar librerías).
def es_primo(n):
    if n < 2:                 # 0, 1 y negativos NO son primos
        return False
    i = 2
    while i * i <= n:         # Revisamos hasta la raíz cuadrada de n
        if n % i == 0:        # Si el residuo es 0, i divide a n -> no es primo
            return False
        i += 1
    return True               # Si ningún número lo dividió, es primo


# ---------------------------------------------------------------------
# 4. CELSIUS A FAHRENHEIT
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Definir celsius_fahrenheit(c) aplicando la fórmula:
#   F = (C × 9/5) + 32
#
# EXPLICACIÓN:
# Fórmula: F = (C × 9/5) + 32
def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32


# ---------------------------------------------------------------------
# 5. MÁXIMO DE TRES NÚMEROS (sin listas ni max())
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Escribir maximo_de_tres(a, b, c) sin usar listas ni la función max().
#
# EXPLICACIÓN:
# Suponemos que el mayor es a, y lo vamos comparando con b y c.
def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


# ---------------------------------------------------------------------
# 6. CONTAR LOS DÍGITOS DE UN NÚMERO
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Crear la función contar_digitos(n) que retorne cuántos dígitos
#   tiene un número entero.
#
# EXPLICACIÓN:
# Idea: dividir entre 10 con // le "quita" el último dígito al número.
# Contamos cuántas veces podemos hacerlo hasta que llegue a 0.
# Ejemplo: 4567 -> 456 -> 45 -> 4 -> 0  (4 divisiones = 4 dígitos)
def contar_digitos(n):
    n = abs(n)                # abs() quita el signo negativo (-123 tiene 3 dígitos)
    if n == 0:                # Caso especial: el 0 tiene 1 dígito
        return 1
    contador = 0
    while n > 0:
        n = n // 10           # División entera: le quita el último dígito
        contador += 1
    return contador


# ---------------------------------------------------------------------
# 7. INVERTIR UNA CADENA CON RECURSIÓN (sin slicing)
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Escribir invertir(cadena) sin usar slicing ([::-1]) ni estructuras
#   avanzadas. Debe usar recursión.
#
# EXPLICACIÓN:
# Recursión = una función que se llama a sí misma.
# Siempre necesita:
#   - Un CASO BASE que detiene las llamadas.
#   - Un CASO RECURSIVO que se acerca al caso base.
#
# Aquí usamos un parámetro i (posición actual) que empieza en 0.
# Para "abc":
#   invertir("abc", 0) = invertir("abc", 1) + "a"
#   invertir("abc", 1) = invertir("abc", 2) + "b"
#   invertir("abc", 2) = invertir("abc", 3) + "c"
#   invertir("abc", 3) = ""            <- caso base
#   Resultado: "" + "c" + "b" + "a" = "cba"
def invertir(cadena, i=0):
    if i == len(cadena):                    # Caso base: ya pasamos el último carácter
        return ""
    return invertir(cadena, i + 1) + cadena[i]   # Primero lo que sigue, luego el actual


# ---------------------------------------------------------------------
# 8. ¿LA CADENA ES PALÍNDROMA?
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Crear es_palindromo(cadena) comparando carácter por carácter.
#   Puede usar la función invertir.
#
# EXPLICACIÓN:
# Un palíndromo se lee igual al derecho y al revés (ej: "radar", "oso").
# Comparamos carácter por carácter: el primero con el último,
# el segundo con el penúltimo, etc.
def es_palindromo(cadena):
    # Pasamos a minúsculas y quitamos espacios para que
    # "Anita lava la tina" también cuente como palíndromo
    cadena = cadena.lower().replace(" ", "")
    n = len(cadena)
    for i in range(n // 2):                 # Solo hace falta revisar la mitad
        if cadena[i] != cadena[n - 1 - i]:  # n-1-i es la posición "espejo" de i
            return False                    # Si un par no coincide, no es palíndromo
    return True

    # Alternativa permitida por el enunciado usando la función del ejercicio 7:
    # return cadena == invertir(cadena)


# ---------------------------------------------------------------------
# 9. POTENCIA SIN USAR **
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Crear potencia(base, exponente) usando multiplicaciones repetidas
#   o recursión.
#
# EXPLICACIÓN:
# base^exponente = base * base * ... (exponente veces)
# Lo hacemos con recursión:
#   potencia(2, 3) = 2 * potencia(2, 2)
#                  = 2 * 2 * potencia(2, 1)
#                  = 2 * 2 * 2 * potencia(2, 0)
#                  = 2 * 2 * 2 * 1 = 8
def potencia(base, exponente):
    if exponente == 0:                        # Caso base: cualquier número a la 0 es 1
        return 1
    if exponente < 0:                         # Exponente negativo: 2^-3 = 1 / 2^3
        return 1 / potencia(base, -exponente)
    return base * potencia(base, exponente - 1)   # Caso recursivo


# ---------------------------------------------------------------------
# 10. MÍNIMO COMÚN MÚLTIPLO (mcm) USANDO EL MCD
# ---------------------------------------------------------------------
# ENUNCIADO:
#   Crear dos funciones:
#     1. mcd(a, b) usando el algoritmo de Euclides.
#     2. mcm(a, b) usando la fórmula: mcm(a, b) = |a * b| / mcd(a, b)
#
# EXPLICACIÓN:
# Algoritmo de Euclides para el MCD (máximo común divisor):
#   Mientras b no sea 0: reemplazamos (a, b) por (b, a % b).
#   Cuando b llega a 0, el MCD es a.
# Ejemplo: mcd(12, 18) -> (18, 12) -> (12, 6) -> (6, 0) -> MCD = 6
def mcd(a, b):
    while b != 0:
        residuo = a % b    # Guardamos el residuo en una variable temporal
        a = b
        b = residuo
    return abs(a)


# Fórmula: mcm(a, b) = |a * b| / mcd(a, b)
# Usamos // (división entera) para que el resultado sea un entero.
def mcm(a, b):
    return abs(a * b) // mcd(a, b)   # Esta función LLAMA a mcd()


# =====================================================================
#  MENÚ PRINCIPAL: permite probar cada ejercicio
# =====================================================================
def menu():
    opcion = ""
    while opcion != "0":
        print("\n===== EJERCICIOS CON FUNCIONES =====")
        print("1. Factorial")
        print("2. Calculadora")
        print("3. ¿Es primo?")
        print("4. Celsius a Fahrenheit")
        print("5. Máximo de tres números")
        print("6. Contar dígitos")
        print("7. Invertir cadena (recursión)")
        print("8. ¿Es palíndromo?")
        print("9. Potencia sin **")
        print("10. MCD y MCM")
        print("0. Salir")
        opcion = input("Elige un ejercicio: ")

        if opcion == "1":
            n = int(input("Número entero positivo: "))
            print(f"{n}! = {factorial(n)}")

        elif opcion == "2":
            calculadora()

        elif opcion == "3":
            n = int(input("Número: "))
            if es_primo(n):
                print(f"{n} es primo")
            else:
                print(f"{n} NO es primo")

        elif opcion == "4":
            c = float(input("Grados Celsius: "))
            print(f"{c} °C = {celsius_fahrenheit(c):.2f} °F")

        elif opcion == "5":
            a = float(input("Número a: "))
            b = float(input("Número b: "))
            c = float(input("Número c: "))
            print("El mayor es:", maximo_de_tres(a, b, c))

        elif opcion == "6":
            n = int(input("Número entero: "))
            print(f"{n} tiene {contar_digitos(n)} dígito(s)")

        elif opcion == "7":
            texto = input("Escribe una palabra o frase: ")
            print("Invertida:", invertir(texto))

        elif opcion == "8":
            texto = input("Escribe una palabra o frase: ")
            if es_palindromo(texto):
                print("Es palíndromo")
            else:
                print("NO es palíndromo")

        elif opcion == "9":
            base = float(input("Base: "))
            exponente = int(input("Exponente (entero): "))
            print(f"{base} ^ {exponente} = {potencia(base, exponente)}")

        elif opcion == "10":
            a = int(input("Número a: "))
            b = int(input("Número b: "))
            print(f"MCD({a}, {b}) = {mcd(a, b)}")
            print(f"MCM({a}, {b}) = {mcm(a, b)}")

        elif opcion == "0":
            print("¡Hasta luego!")

        else:
            print("Opción no válida")


# Esta línea hace que el menú solo se ejecute cuando corres ESTE archivo
# directamente (y no cuando lo importas desde otro archivo).
if __name__ == "__main__":
    menu()
