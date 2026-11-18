# =====================================================================
#  15.2 ENUNCIADOS: USO DE MATRICES EN PYTHON
# ---------------------------------------------------------------------
#  Reglas del taller:
#   - Las matrices son LISTAS DE LISTAS: matriz = [[1, 2], [3, 4]]
#   - NO se usa numpy.
#   - NO se usan funciones definidas por el usuario (nada de def),
#     solo estructuras secuenciales, condicionales y repetitivas.
#
#  Por eso el código para leer una matriz se repite en cada ejercicio:
#  sin funciones, no hay forma de "reutilizarlo".
#
#  Recordatorio: matriz[i][j]  ->  i = fila, j = columna (empiezan en 0)
# =====================================================================

opcion = ""

while opcion != "0":
    print("\n===== EJERCICIOS DE MATRICES =====")
    print("1. Suma de dos matrices")
    print("2. Matriz transpuesta")
    print("3. Suma de la diagonal principal")
    print("4. Mayor valor y su posición")
    print("5. Matriz por un escalar")
    print("0. Salir")
    opcion = input("Elige un ejercicio: ")

    # -----------------------------------------------------------------
    # ENUNCIADO 1: SUMA DE DOS MATRICES
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Elabore un programa que reciba dos matrices de igual tamaño (filas y
    #   columnas) ingresadas por el usuario, y calcule la matriz resultante de
    #   sumar elemento a elemento ambas matrices. Debe imprimir la matriz
    #   resultante con un formato ordenado (filas y columnas alineadas).
    #   Consideraciones:
    #     - Solicite primero el número de filas y columnas.
    #     - Valide que ambas matrices tengan las mismas dimensiones antes de sumarlas.
    #     - Muestre un mensaje de error si las dimensiones no coinciden.
    #
    # EXPLICACIÓN:
    # Se suma posición por posición: C[i][j] = A[i][j] + B[i][j]
    # Solo se puede si ambas tienen las mismas filas y columnas.
    if opcion == "1":
        # --- Dimensiones de la matriz A ---
        filas_a = int(input("Filas de la matriz A: "))
        columnas_a = int(input("Columnas de la matriz A: "))
        # --- Dimensiones de la matriz B ---
        filas_b = int(input("Filas de la matriz B: "))
        columnas_b = int(input("Columnas de la matriz B: "))

        # Validación: si las dimensiones no coinciden, no se puede sumar
        if filas_a != filas_b or columnas_a != columnas_b:
            print("Error: las matrices deben tener las mismas dimensiones para sumarse.")
        else:
            # --- Leer matriz A elemento por elemento ---
            print("Ingrese los elementos de la matriz A:")
            A = []
            for i in range(filas_a):
                fila = []                                   # Fila vacía
                for j in range(columnas_a):
                    valor = int(input(f"A[{i},{j}]: "))      # f-string muestra la posición
                    fila.append(valor)                      # Agregamos el valor a la fila
                A.append(fila)                              # Agregamos la fila a la matriz

            # --- Leer matriz B ---
            print("Ingrese los elementos de la matriz B:")
            B = []
            for i in range(filas_b):
                fila = []
                for j in range(columnas_b):
                    valor = int(input(f"B[{i},{j}]: "))
                    fila.append(valor)
                B.append(fila)

            # --- Calcular la suma ---
            C = []
            for i in range(filas_a):
                fila = []
                for j in range(columnas_a):
                    fila.append(A[i][j] + B[i][j])          # Suma posición por posición
                C.append(fila)

            # --- Imprimir con formato alineado ---
            # {:6} reserva 6 espacios por número, así las columnas quedan alineadas
            print("\nMatriz resultante (A + B):")
            for i in range(filas_a):
                for j in range(columnas_a):
                    print(f"{C[i][j]:6}", end="")          # end="" evita el salto de línea
                print()                                     # Salto de línea al terminar la fila

    # -----------------------------------------------------------------
    # ENUNCIADO 2: MATRIZ TRANSPUESTA
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Elabore un programa que reciba una matriz de tamaño n x m ingresada por
    #   el usuario y calcule su matriz transpuesta (las filas se convierten en
    #   columnas y viceversa). Debe imprimir la matriz original y la transpuesta.
    #   Consideraciones:
    #     - La matriz de entrada no necesariamente debe ser cuadrada.
    #     - La matriz transpuesta resultante tendrá dimensiones m x n.
    #
    # EXPLICACIÓN:
    # Las filas se vuelven columnas: T[j][i] = M[i][j]
    # Si M es n x m, la transpuesta es m x n.
    elif opcion == "2":
        n = int(input("Número de filas (n): "))
        m = int(input("Número de columnas (m): "))

        # --- Leer la matriz original ---
        M = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(int(input(f"Elemento [{i},{j}]: ")))
            M.append(fila)

        # --- Construir la transpuesta ---
        # El ciclo externo recorre las COLUMNAS de M (j),
        # y cada columna de M se convierte en una FILA de T.
        T = []
        for j in range(m):
            nueva_fila = []
            for i in range(n):
                nueva_fila.append(M[i][j])
            T.append(nueva_fila)

        # --- Imprimir la original ---
        print(f"\nMatriz original ({n} x {m}):")
        for i in range(n):
            for j in range(m):
                print(f"{M[i][j]:6}", end="")
            print()

        # --- Imprimir la transpuesta (ojo: ahora tiene m filas y n columnas) ---
        print(f"\nMatriz transpuesta ({m} x {n}):")
        for i in range(m):
            for j in range(n):
                print(f"{T[i][j]:6}", end="")
            print()

    # -----------------------------------------------------------------
    # ENUNCIADO 3: SUMA DE LA DIAGONAL PRINCIPAL
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Elabore un programa que reciba una matriz cuadrada (mismo número de
    #   filas y columnas) ingresada por el usuario y calcule la suma de los
    #   elementos de la diagonal principal. Debe imprimir la matriz completa y
    #   el valor de la suma obtenida.
    #   Consideraciones:
    #     - Valide que la matriz sea cuadrada; si no, muestre un mensaje de error.
    #     - La diagonal principal son los elementos donde fila == columna.
    #
    # EXPLICACIÓN:
    # La diagonal principal son los elementos donde fila == columna:
    # M[0][0], M[1][1], M[2][2], ...
    # Solo existe en matrices CUADRADAS (filas == columnas).
    elif opcion == "3":
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))

        if filas != columnas:
            print("Error: la matriz debe ser cuadrada (mismo número de filas y columnas).")
        else:
            # --- Leer la matriz ---
            M = []
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    fila.append(int(input(f"Elemento [{i},{j}]: ")))
                M.append(fila)

            # --- Sumar la diagonal ---
            # Basta un solo ciclo porque i se usa como fila Y como columna
            suma = 0
            for i in range(filas):
                suma += M[i][i]

            # --- Imprimir la matriz y el resultado ---
            print("\nMatriz:")
            for i in range(filas):
                for j in range(columnas):
                    print(f"{M[i][j]:6}", end="")
                print()
            print("Suma de la diagonal principal:", suma)

    # -----------------------------------------------------------------
    # ENUNCIADO 4: MAYOR VALOR Y SU POSICIÓN
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Elabore un programa que reciba una matriz de tamaño n x m ingresada por
    #   el usuario y determine el valor mayor contenido en ella, así como la
    #   fila y columna donde se encuentra. Debe imprimir la matriz, el valor
    #   máximo y su posición.
    #   Consideraciones:
    #     - Si el máximo se repite, reportar solo la PRIMERA posición encontrada.
    #     - La posición debe mostrarse en el formato: fila X, columna Y.
    #
    # EXPLICACIÓN:
    # Recorremos toda la matriz guardando el mayor encontrado y dónde está.
    # Usamos > (y no >=) para quedarnos con la PRIMERA posición si se repite.
    elif opcion == "4":
        n = int(input("Número de filas: "))
        m = int(input("Número de columnas: "))

        # --- Leer la matriz ---
        M = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(int(input(f"Elemento [{i},{j}]: ")))
            M.append(fila)

        # --- Buscar el mayor ---
        # Empezamos suponiendo que el mayor es el primer elemento
        mayor = M[0][0]
        fila_mayor = 0
        columna_mayor = 0
        for i in range(n):
            for j in range(m):
                if M[i][j] > mayor:      # Con > no se reemplaza si encuentra uno igual
                    mayor = M[i][j]
                    fila_mayor = i
                    columna_mayor = j

        # --- Imprimir resultados ---
        print("\nMatriz:")
        for i in range(n):
            for j in range(m):
                print(f"{M[i][j]:6}", end="")
            print()
        print("Valor máximo:", mayor)
        print(f"Posición: fila {fila_mayor}, columna {columna_mayor}")

    # -----------------------------------------------------------------
    # ENUNCIADO 5: MATRIZ POR UN ESCALAR
    # -----------------------------------------------------------------
    # ENUNCIADO:
    #   Elabore un programa que reciba una matriz n x m ingresada por el usuario
    #   y un valor escalar (entero o decimal). Debe multiplicar cada elemento por
    #   el escalar e imprimir la matriz original y la resultante.
    #   Consideraciones:
    #     - El escalar puede ser positivo, negativo o cero.
    #     - Verifique que todos los valores ingresados a la matriz sean numéricos.
    #
    # EXPLICACIÓN:
    # Cada elemento se multiplica por el mismo número: R[i][j] = k * M[i][j]
    elif opcion == "5":
        n = int(input("Número de filas: "))
        m = int(input("Número de columnas: "))

        # --- Leer la matriz validando que cada valor sea numérico ---
        M = []
        for i in range(n):
            fila = []
            for j in range(m):
                valido = False
                while not valido:                 # Repetimos hasta que el dato sea numérico
                    dato = input(f"Elemento [{i},{j}]: ")
                    # try/except: intenta convertir a número; si falla (ej: "hola"),
                    # se ejecuta el except en vez de que el programa se detenga
                    try:
                        valor = float(dato)       # float acepta enteros y decimales
                        valido = True
                    except ValueError:
                        print("  Error: ingrese un valor numérico.")
                fila.append(valor)
            M.append(fila)

        # --- Leer el escalar (también validado) ---
        valido = False
        while not valido:
            dato = input("Escalar (puede ser positivo, negativo o cero): ")
            try:
                k = float(dato)
                valido = True
            except ValueError:
                print("  Error: ingrese un valor numérico.")

        # --- Multiplicar ---
        R = []
        for i in range(n):
            fila = []
            for j in range(m):
                # + 0.0 evita que se muestre "-0" cuando el escalar es 0 y el número es negativo
                fila.append(M[i][j] * k + 0.0)
            R.append(fila)

        # --- Imprimir ---
        # :8g muestra el número sin ceros de más (5.0 se ve como 5, 2.5 como 2.5)
        print("\nMatriz original:")
        for i in range(n):
            for j in range(m):
                print(f"{M[i][j]:8g}", end="")
            print()
        print(f"\nMatriz resultante (x {k:g}):")
        for i in range(n):
            for j in range(m):
                print(f"{R[i][j]:8g}", end="")
            print()

    elif opcion == "0":
        print("¡Hasta luego!")

    else:
        print("Opción no válida")
