# Repaso práctico de Python - Parcial de Computación
# Ejecuta el archivo y elige en el menú el ejercicio que quieras probar.


# 1. Contador y acumulador con for
def ejercicio_1():
    pares = 0   # contador: suma 1 cada vez que el número es par
    suma = 0    # acumulador: va sumando todos los números
    for i in range(5):
        n = int(input("Número: "))
        suma += n            # suma = suma + n
        if n % 2 == 0:
            pares += 1       # pares = pares + 1
    print("Pares:", pares, "Suma:", suma)


# 2. Condicionales (if / elif / else)
def ejercicio_2():
    nota = float(input("Nota: "))
    if nota >= 4.5:
        print("Excelente")
    elif nota >= 3.0:
        print("Aprobó")
    else:
        print("Reprobó")


# 3. while con validación
def ejercicio_3():
    edad = int(input("Edad: "))
    while edad < 0 or edad > 120:
        print("Edad inválida")
        edad = int(input("Edad: "))
    print("Edad registrada:", edad)


# 4. while con break y continue
def ejercicio_4():
    suma = 0
    while True:
        n = int(input("Número (0 para salir): "))
        if n == 0:
            break        # sale del ciclo
        if n < 0:
            continue     # ignora el negativo y pasa a la siguiente vuelta
        suma += n
    print("Suma:", suma)


# 5. for con break (buscar en una lista)
def ejercicio_5():
    lista = [4, 8, 15, 16, 23]
    buscado = int(input("Buscar: "))
    encontrado = False
    for x in lista:
        if x == buscado:
            encontrado = True
            break
    if encontrado:
        print("Está")
    else:
        print("No está")


# 6. Función con return
def es_par(n):
    return n % 2 == 0


def ejercicio_6():
    n = int(input("Número: "))
    print("¿Es par?", es_par(n))


# 7. Diccionario: recorrer y sacar promedio
def ejercicio_7():
    notas = {"ana": 4.5, "luis": 3.2, "juan": 4.0}
    total = 0
    for nombre, nota in notas.items():
        print(nombre, "->", nota)
        total += nota
    print("Promedio:", round(total / len(notas), 2))


# 8. Matriz con for anidado: llenar y sumar
def ejercicio_8():
    m = []
    for i in range(2):
        fila = []
        for j in range(3):
            fila.append(int(input(f"m[{i}][{j}]: ")))
        m.append(fila)

    suma = 0
    for fila in m:
        for x in fila:
            suma += x
    print("Matriz:", m)
    print("Suma:", suma)


# Menú principal
ejercicios = {
    "1": ("Contador y acumulador con for", ejercicio_1),
    "2": ("Condicionales", ejercicio_2),
    "3": ("while con validación", ejercicio_3),
    "4": ("while con break y continue", ejercicio_4),
    "5": ("for con break", ejercicio_5),
    "6": ("Función es_par", ejercicio_6),
    "7": ("Diccionario y promedio", ejercicio_7),
    "8": ("Matriz con for anidado", ejercicio_8),
}

while True:
    print("\n=== REPASO PRÁCTICO ===")
    for clave, (nombre, _) in ejercicios.items():
        print(clave + ".", nombre)
    print("0. Salir")
    opcion = input("Elige un ejercicio: ")
    if opcion == "0":
        print("¡Éxitos en el parcial!")
        break
    if opcion in ejercicios:
        print("\n---", ejercicios[opcion][0], "---")
        ejercicios[opcion][1]()
    else:
        print("Opción inválida")
