# =====================================================================
#  15.1 EJERCICIOS INTERMEDIOS EN PYTHON — COLECCIONES
# ---------------------------------------------------------------------
#  1. Listas y matrices   (1.1 a 1.5)
#  2. Tuplas              (2.1 a 2.5)
#  3. Sets                (3.1 a 3.5)
#  4. Diccionarios        (4.1 a 4.5)
#
#  Cómo usar este archivo: ejecútalo y escribe en el menú el número
#  del ejercicio, por ejemplo 1.3 o 4.2
# =====================================================================

opcion = ""

while opcion != "0":
    print("\n========== EJERCICIOS DE COLECCIONES ==========")
    print("LISTAS Y MATRICES")
    print("  1.1 Números mayores que el promedio")
    print("  1.2 Producto escalar de dos listas")
    print("  1.3 Matriz identidad")
    print("  1.4 Suma de dos matrices")
    print("  1.5 Transposición de una matriz")
    print("TUPLAS")
    print("  2.1 Lista a tupla sin duplicados")
    print("  2.2 Coordenadas dentro de un rango")
    print("  2.3 Empaquetar y desempaquetar")
    print("  2.4 Comparación de tuplas")
    print("  2.5 Suma y promedio con tuplas")
    print("SETS")
    print("  3.1 Unión y diferencia")
    print("  3.2 Palabras únicas de una frase")
    print("  3.3 Pares comunes (intersección)")
    print("  3.4 Diferencia simétrica")
    print("  3.5 Subconjunto y superconjunto")
    print("DICCIONARIOS")
    print("  4.1 Agenda telefónica")
    print("  4.2 Contador de palabras")
    print("  4.3 Promedio de calificaciones")
    print("  4.4 Diccionario invertido")
    print("  4.5 Fusionar diccionarios")
    print("0. Salir")
    opcion = input("Elige un ejercicio: ")

    # =================================================================
    # 1. LISTAS Y MATRICES
    # =================================================================

    # -----------------------------------------------------------------
    # 1.1 NÚMEROS MAYORES QUE EL PROMEDIO
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar al usuario una lista de números y mostrar cuáles son mayores
    #   que el promedio de la lista.
    #   Entrada: 10 5 8 3 9
    #   Salida:  Promedio: 7.0 / Mayores que el promedio: [8, 9, 10]
    if opcion == "1.1":
        texto = input("Ingresa números separados por espacio: ")   # ej: 10 5 8 3 9
        # split() corta el texto por los espacios -> ['10', '5', '8', '3', '9']
        # La comprensión convierte cada pedazo a número
        numeros = [int(x) for x in texto.split()]

        promedio = sum(numeros) / len(numeros)   # sum() suma todo, len() cuenta elementos
        # Filtramos solo los mayores al promedio y los ordenamos con sorted()
        mayores = sorted([n for n in numeros if n > promedio])

        print("Promedio:", promedio)
        print("Mayores que el promedio:", mayores)

    # -----------------------------------------------------------------
    # 1.2 PRODUCTO ESCALAR DE DOS LISTAS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Dadas dos listas del mismo tamaño con números, calcular su producto escalar
    #   (multiplicar los elementos de la misma posición y sumar los resultados).
    #   Entrada: Lista A: 1 2 3 / Lista B: 4 5 6
    #   Salida:  Producto escalar = 32
    #
    # EXPLICACIÓN:
    # A·B = A[0]*B[0] + A[1]*B[1] + ...
    # Ejemplo: [1,2,3]·[4,5,6] = 1*4 + 2*5 + 3*6 = 32
    elif opcion == "1.2":
        A = [float(x) for x in input("Lista A (separada por espacios): ").split()]
        B = [float(x) for x in input("Lista B (separada por espacios): ").split()]

        if len(A) != len(B):
            print("Error: las listas deben tener el mismo tamaño.")
        else:
            producto = 0
            for i in range(len(A)):
                producto += A[i] * B[i]     # Multiplicamos los de la misma posición y sumamos
            print(f"Producto escalar = {producto:g}")

    # -----------------------------------------------------------------
    # 1.3 MATRIZ IDENTIDAD
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar un número n y construir una matriz identidad de tamaño n×n
    #   (1s en la diagonal principal y 0s en las demás posiciones).
    #   Entrada: n = 3
    #   Salida:  [1, 0, 0] / [0, 1, 0] / [0, 0, 1]
    #
    # EXPLICACIÓN:
    # 1 en la diagonal (cuando fila == columna) y 0 en lo demás
    elif opcion == "1.3":
        n = int(input("n = "))
        identidad = []
        for i in range(n):
            fila = []
            for j in range(n):
                if i == j:
                    fila.append(1)     # Diagonal principal
                else:
                    fila.append(0)
            identidad.append(fila)

        for fila in identidad:         # Imprime cada fila en una línea
            print(fila)

        # Versión corta con comprensión de listas (hace lo mismo):
        # identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # -----------------------------------------------------------------
    # 1.4 SUMA DE DOS MATRICES
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Dadas dos matrices del mismo tamaño, calcular su suma elemento a elemento
    #   (cada posición (i, j) se suma entre las dos matrices).
    #   Entrada: A = [[1, 2], [3, 4]]  B = [[5, 6], [7, 8]]
    #   Salida:  [[6, 8], [10, 12]]
    elif opcion == "1.4":
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))

        # Leer A (mismo método del README de matrices)
        print("Matriz A:")
        A = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(int(input(f"A[{i},{j}]: ")))
            A.append(fila)

        # Leer B
        print("Matriz B:")
        B = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(int(input(f"B[{i},{j}]: ")))
            B.append(fila)

        # Sumar posición por posición: C[i][j] = A[i][j] + B[i][j]
        C = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(A[i][j] + B[i][j])
            C.append(fila)

        print("A + B =", C)

    # -----------------------------------------------------------------
    # 1.5 TRANSPOSICIÓN DE UNA MATRIZ
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Generar la matriz transpuesta de una matriz ingresada por el usuario
    #   (se intercambian filas por columnas: A[i][j] -> A[j][i]).
    #   Entrada: [[1, 2, 3], [4, 5, 6]]
    #   Salida:  [[1, 4], [2, 5], [3, 6]]
    #
    # EXPLICACIÓN:
    # A[i][j] pasa a la posición T[j][i]
    elif opcion == "1.5":
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))

        A = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(int(input(f"Elemento [{i},{j}]: ")))
            A.append(fila)

        # Cada columna j de A se convierte en la fila j de T
        T = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(A[i][j])
            T.append(nueva_fila)

        print("Original:   ", A)
        print("Transpuesta:", T)

    # =================================================================
    # 2. TUPLAS (ordenadas e inmutables)
    # =================================================================

    # -----------------------------------------------------------------
    # 2.1 LISTA A TUPLA SIN DUPLICADOS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar una lista de elementos y convertirla en una tupla sin
    #   elementos repetidos (convertir a set elimina duplicados; luego a tupla).
    #   Entrada: ['rojo', 'azul', 'rojo', 'verde']
    #   Salida:  ('rojo', 'azul', 'verde')
    #
    # EXPLICACIÓN:
    # La explicación del taller dice: lista -> set -> tupla.
    # Problema: el set NO guarda el orden, así que el resultado podría salir
    # desordenado. Para respetar el orden de la salida esperada, recorremos
    # la lista y usamos un set solo para recordar lo que ya vimos.
    elif opcion == "2.1":
        texto = input("Elementos separados por coma (ej: rojo,azul,rojo,verde): ")
        # strip() quita espacios sobrantes de cada elemento
        lista = [x.strip() for x in texto.split(",")]

        vistos = set()        # Elementos que ya agregamos
        sin_repetir = []      # Lista auxiliar en orden
        for elemento in lista:
            if elemento not in vistos:      # Si no lo hemos visto, lo agregamos
                vistos.add(elemento)
                sin_repetir.append(elemento)

        resultado = tuple(sin_repetir)      # tuple() convierte la lista en tupla
        print(resultado)

        # Versión directa del enunciado (puede cambiar el orden):
        # resultado = tuple(set(lista))

    # -----------------------------------------------------------------
    # 2.2 COORDENADAS DENTRO DE UN RANGO
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Dadas coordenadas (x, y) en una tupla, verificar si están dentro de
    #   un rango dado (si x e y están entre los límites).
    #   Entrada: Coordenada: (4, 6) / Rango: 0 a 10
    #   Salida:  Dentro del rango
    elif opcion == "2.2":
        x = float(input("Coordenada x: "))
        y = float(input("Coordenada y: "))
        coordenada = (x, y)                       # Empaquetamos en una tupla

        minimo = float(input("Límite inferior del rango: "))
        maximo = float(input("Límite superior del rango: "))

        # Python permite comparaciones encadenadas: a <= x <= b
        if minimo <= coordenada[0] <= maximo and minimo <= coordenada[1] <= maximo:
            print("Dentro del rango")
        else:
            print("Fuera del rango")

    # -----------------------------------------------------------------
    # 2.3 EMPAQUETAR Y DESEMPAQUETAR DATOS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Dado un conjunto de datos (nombre, edad, país) empaquetados en una
    #   tupla, mostrar cada uno (desempaquetar asignando la tupla a variables).
    #   Entrada: ('Ana', 23, 'Colombia')
    #   Salida:  Nombre: Ana / Edad: 23 / País: Colombia
    elif opcion == "2.3":
        # EMPAQUETAR: juntar varios valores en una sola tupla
        datos = (input("Nombre: "), int(input("Edad: ")), input("País: "))
        print("Tupla empaquetada:", datos)

        # DESEMPAQUETAR: repartir la tupla en variables
        # (debe haber tantas variables como elementos tenga la tupla)
        nombre, edad, pais = datos

        print("Nombre:", nombre)
        print("Edad:", edad)
        print("País:", pais)

    # -----------------------------------------------------------------
    # 2.4 COMPARACIÓN DE TUPLAS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Ingresar dos tuplas numéricas y determinar cuál es mayor
    #   (Python compara tuplas elemento a elemento de forma lexicográfica).
    #   Entrada: (3, 4, 5) y (3, 4, 2)
    #   Salida:  La primera tupla es mayor.
    #
    # EXPLICACIÓN:
    # Python compara de forma LEXICOGRÁFICA (como en el diccionario):
    # primero el elemento 0; si son iguales, pasa al 1; y así sucesivamente.
    # (3, 4, 5) vs (3, 4, 2): 3 == 3, 4 == 4, 5 > 2 -> la primera es mayor
    elif opcion == "2.4":
        t1 = tuple(int(x) for x in input("Primera tupla (números separados por espacio): ").split())
        t2 = tuple(int(x) for x in input("Segunda tupla (números separados por espacio): ").split())
        print("Tupla 1:", t1)
        print("Tupla 2:", t2)

        if t1 > t2:
            print("La primera tupla es mayor.")
        elif t1 < t2:
            print("La segunda tupla es mayor.")
        else:
            print("Las tuplas son iguales.")

    # -----------------------------------------------------------------
    # 2.5 SUMA Y PROMEDIO CON TUPLAS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar una tupla de números y calcular la suma y el promedio
    #   (usar sum() y len() directamente sobre la tupla).
    #   Entrada: (10, 20, 30, 40)
    #   Salida:  Suma = 100 / Promedio = 25.0
    elif opcion == "2.5":
        numeros = tuple(float(x) for x in input("Números separados por espacio: ").split())
        suma = sum(numeros)                 # sum() y len() funcionan igual en tuplas
        promedio = suma / len(numeros)
        print(f"Suma = {suma:g}")
        print("Promedio =", promedio)

    # =================================================================
    # 3. SETS (no ordenados, sin duplicados)
    # =================================================================

    # -----------------------------------------------------------------
    # 3.1 UNIÓN Y DIFERENCIA
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Ingresar dos conjuntos y mostrar su unión y diferencia
    #   (usar los operadores | para unión y - para diferencia).
    #   Entrada: A = {1, 2, 3}  B = {3, 4, 5}
    #   Salida:  Unión: {1, 2, 3, 4, 5} / Diferencia: {1, 2}
    elif opcion == "3.1":
        # set(...) convierte lo ingresado en conjunto
        A = set(int(x) for x in input("Conjunto A (números separados por espacio): ").split())
        B = set(int(x) for x in input("Conjunto B (números separados por espacio): ").split())

        print("Unión:", A | B)          # |  = todos los elementos de A y de B
        print("Diferencia:", A - B)     # -  = los que están en A pero NO en B
        # Equivalentes con métodos: A.union(B) y A.difference(B)

    # -----------------------------------------------------------------
    # 3.2 PALABRAS ÚNICAS DE UNA FRASE
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar una frase y mostrar las palabras únicas
    #   (separar la frase con split() y convertirla en set).
    #   Entrada: "hola mundo hola python"
    #   Salida:  {'hola', 'mundo', 'python'}
    elif opcion == "3.2":
        frase = input("Escribe una frase: ")
        palabras = frase.split()        # Lista de palabras (con repetidas)
        unicas = set(palabras)          # El set elimina las repetidas
        print(unicas)

    # -----------------------------------------------------------------
    # 3.3 PARES COMUNES (INTERSECCIÓN)
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Dadas dos listas de números, mostrar los pares comunes en ambas
    #   (convertir a sets y usar & para la intersección).
    #   Entrada: A = [2, 4, 6, 8]  B = [4, 5, 6, 9]
    #   Salida:  {4, 6}
    elif opcion == "3.3":
        A = [int(x) for x in input("Lista A: ").split()]
        B = [int(x) for x in input("Lista B: ").split()]

        comunes = set(A) & set(B)                       # & = intersección (los que están en ambas)
        pares_comunes = {n for n in comunes if n % 2 == 0}   # Comprensión de set: solo los pares
        print(pares_comunes)

    # -----------------------------------------------------------------
    # 3.4 DIFERENCIA SIMÉTRICA
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Mostrar los elementos que están en uno de los conjuntos pero no en
    #   ambos (usar ^ o symmetric_difference()).
    #   Entrada: {1, 2, 3} y {3, 4, 5}
    #   Salida:  {1, 2, 4, 5}
    #
    # EXPLICACIÓN:
    # Elementos que están en A o en B, pero NO en ambos a la vez
    elif opcion == "3.4":
        A = set(int(x) for x in input("Conjunto A: ").split())
        B = set(int(x) for x in input("Conjunto B: ").split())
        print(A ^ B)                    # Igual a A.symmetric_difference(B)

    # -----------------------------------------------------------------
    # 3.5 SUBCONJUNTO Y SUPERCONJUNTO
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Determinar si un conjunto A está contenido en otro conjunto B y
    #   viceversa (usar issubset() e issuperset()).
    #   Entrada: A = {1, 2}  B = {1, 2, 3, 4}
    #   Salida:  A es subconjunto de B / B es superconjunto de A
    #
    # EXPLICACIÓN:
    # A es subconjunto de B si TODOS los elementos de A están en B.
    # B es superconjunto de A si B contiene a todos los de A.
    elif opcion == "3.5":
        A = set(int(x) for x in input("Conjunto A: ").split())
        B = set(int(x) for x in input("Conjunto B: ").split())

        # Revisamos A respecto a B
        if A.issubset(B):
            print("A es subconjunto de B")
        else:
            print("A NO es subconjunto de B")
        if B.issuperset(A):
            print("B es superconjunto de A")
        else:
            print("B NO es superconjunto de A")

        # Y viceversa (B respecto a A)
        if B.issubset(A):
            print("B es subconjunto de A")
        if A.issuperset(B):
            print("A es superconjunto de B")

    # =================================================================
    # 4. DICCIONARIOS (pares clave: valor)
    # =================================================================

    # -----------------------------------------------------------------
    # 4.1 AGENDA TELEFÓNICA
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar nombres y teléfonos y almacenarlos en un diccionario hasta
    #   que el usuario escriba "fin" (nombre = clave, teléfono = valor).
    #   Entrada: Juan - 123 / Ana - 456 / fin
    #   Salida:  {'Juan': '123', 'Ana': '456'}
    elif opcion == "4.1":
        agenda = {}                         # Diccionario vacío
        while True:                         # Ciclo "infinito" que cortamos con break
            nombre = input("Nombre (o 'fin' para terminar): ")
            if nombre.lower() == "fin":
                break                       # Sale del ciclo
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono       # Clave = nombre, valor = teléfono
        print(agenda)

    # -----------------------------------------------------------------
    # 4.2 CONTADOR DE PALABRAS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Solicitar una frase y contar cuántas veces aparece cada palabra
    #   (claves = palabras, valores = frecuencias).
    #   Entrada: "hola mundo hola"
    #   Salida:  {'hola': 2, 'mundo': 1}
    elif opcion == "4.2":
        frase = input("Escribe una frase: ")
        contador = {}
        for palabra in frase.split():
            # get(palabra, 0) devuelve el conteo actual, o 0 si es la primera vez
            contador[palabra] = contador.get(palabra, 0) + 1
        print(contador)

    # -----------------------------------------------------------------
    # 4.3 PROMEDIO DE CALIFICACIONES
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Ingresar nombres de estudiantes y sus notas, y calcular el promedio
    #   general (guardar nombre->nota y usar sum() y len() sobre dict.values()).
    #   Entrada: Ana: 4.0 / Luis: 3.5 / Sofía: 4.5
    #   Salida:  Promedio general: 4.0
    elif opcion == "4.3":
        notas = {}
        while True:
            nombre = input("Nombre del estudiante (o 'fin'): ")
            if nombre.lower() == "fin":
                break
            notas[nombre] = float(input(f"Nota de {nombre}: "))

        if len(notas) == 0:
            print("No se ingresaron estudiantes.")
        else:
            # values() devuelve solo las notas, sin los nombres
            promedio = sum(notas.values()) / len(notas)
            print(notas)
            print(f"Promedio general: {promedio:.1f}")

    # -----------------------------------------------------------------
    # 4.4 DICCIONARIO INVERTIDO
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Invertir un diccionario de clave->valor a valor->clave
    #   (usar comprensión de diccionarios {v: k for k, v in dic.items()}).
    #   Entrada: {'a': 1, 'b': 2, 'c': 3}
    #   Salida:  {1: 'a', 2: 'b', 3: 'c'}
    #
    # EXPLICACIÓN:
    # Pasar de clave -> valor a valor -> clave
    elif opcion == "4.4":
        dic = {'a': 1, 'b': 2, 'c': 3}         # Diccionario de ejemplo del enunciado
        # items() da los pares (clave, valor); los volteamos en la comprensión
        invertido = {v: k for k, v in dic.items()}
        print("Original: ", dic)
        print("Invertido:", invertido)
        # Ojo: si dos claves tienen el mismo valor, en el invertido
        # solo quedará una (las claves no se pueden repetir).

    # -----------------------------------------------------------------
    # 4.5 FUSIONAR DICCIONARIOS
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Combinar dos diccionarios en uno solo. Si hay claves repetidas, el
    #   segundo debe sobrescribir al primero (usar update() o | en Python 3.9+).
    #   Entrada: A = {'x': 1, 'y': 2}  B = {'y': 10, 'z': 3}
    #   Salida:  {'x': 1, 'y': 10, 'z': 3}
    elif opcion == "4.5":
        A = {'x': 1, 'y': 2}                   # Diccionarios de ejemplo del enunciado
        B = {'y': 10, 'z': 3}

        # Forma 1: copy() + update(). Copiamos A para no modificar el original;
        # update() agrega lo de B y SOBRESCRIBE las claves repetidas ('y')
        fusion = A.copy()
        fusion.update(B)
        print("Con update():", fusion)

        # Forma 2 (Python 3.9+): operador |
        print("Con |:       ", A | B)

    elif opcion == "0":
        print("¡Hasta luego!")

    else:
        print("Opción no válida")
