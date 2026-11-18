#---------------------------------------------------------------------
# 1.2. SINTAXIS BÁSICA
# ---------------------------------------------------------------------
#  def            -> indica que se está definiendo una función
#  nombre_funcion -> el nombre (identificador) de la función
#  (p1, p2)       -> los parámetros van entre paréntesis
#  return         -> devuelve el valor al lugar donde se llamó la función
#  El cuerpo de la función va INDENTADO (4 espacios) debajo del def.
def nombre_funcion(parametro1, parametro2):
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado  # Devuelve un valor


print("----- 1.2 Sintaxis básica -----")
print("nombre_funcion(2, 3) =", nombre_funcion(2, 3))   # 5


# ---------------------------------------------------------------------
# 1.3. EJEMPLO SIMPLE: FUNCIÓN QUE SUMA DOS NÚMEROS
# ---------------------------------------------------------------------
#  - La función sumar "encapsula" (guarda adentro) la operación de suma.
#  - Se puede llamar muchas veces con distintos valores.
#  - a y b son PARÁMETROS (van en el def).
#  - x y y son ARGUMENTOS (los valores que se envían al llamarla).
def sumar(a, b):
    """Devuelve la suma de a y b."""   # Docstring: documenta qué hace la función
    resultado = a + b
    return resultado


print("\n----- 1.3 Función que suma -----")
x = 3
y = 5
s = sumar(x, y)  # Llamada a la función: a recibe 3 y b recibe 5
print("La suma es:", s)                 # La suma es: 8
print("Otra llamada:", sumar(10, 20))   # Se reutiliza con otros valores -> 30


# ---------------------------------------------------------------------
# 1.4. FUNCIÓN SIN PARÁMETROS
# ---------------------------------------------------------------------
#  - No recibe parámetros (los paréntesis van vacíos).
#  - Solo realiza una acción interna (imprimir).
#  - Igual hay que llamarla con paréntesis: saludar()
def saludar():
    """Imprime un saludo fijo."""
    print("Hola, bienvenido a Python")


print("\n----- 1.4 Función sin parámetros -----")
saludar()   # Hola, bienvenido a Python


# ---------------------------------------------------------------------
# 1.5. FUNCIÓN CON PARÁMETROS Y SIN RETORNO
# ---------------------------------------------------------------------
#  - Recibe datos (a y b) pero NO usa return: solo imprime.
#  - Tiene un CONDICIONAL DENTRO de la función (if / elif / else).
#  - Como no tiene return, si guardas su resultado en una variable,
#    esa variable valdrá None.
def mostrar_mayor(a, b):
    """Muestra cuál de los dos números es mayor."""
    if a > b:
        print("El mayor es:", a)
    elif b > a:
        print("El mayor es:", b)
    else:
        print("Son iguales")


print("\n----- 1.5 Función con parámetros y sin retorno -----")
mostrar_mayor(10, 7)   # El mayor es: 10
mostrar_mayor(4, 4)    # Son iguales
r = mostrar_mayor(1, 9)          # Imprime "El mayor es: 9"...
print("Valor devuelto:", r)      # ...pero devuelve None (no hay return)


# ---------------------------------------------------------------------
# 1.6. PARÁMETROS CON VALOR POR DEFECTO
# ---------------------------------------------------------------------
#  - saludo="Hola" es un valor por defecto.
#  - Si NO se envía el segundo argumento, se usa "Hola".
#  - Si SÍ se envía, reemplaza al valor por defecto.
#  - Los parámetros con valor por defecto van al FINAL.
def saludar_persona(nombre, saludo="Hola"):
    """Muestra un saludo personalizado usando un saludo por defecto."""
    print(saludo, nombre)


print("\n----- 1.6 Parámetros con valor por defecto -----")
saludar_persona("Ana")                # Usa el valor por defecto -> Hola Ana
saludar_persona("Luis", "Buenas")     # Sobrescribe el valor por defecto -> Buenas Luis


# ---------------------------------------------------------------------
# 1.7. RETORNO DE MÚLTIPLES VALORES
# ---------------------------------------------------------------------
#  - return cociente, resto  devuelve una TUPLA: (cociente, resto)
#  - Esa tupla se puede DESEMPAQUETAR en dos variables: q, r = ...
#  - // es división entera y % es el residuo (resto).
def dividir_y_resto(a, b):
    """Devuelve el cociente y el resto de dividir a entre b."""
    cociente = a // b
    resto = a % b
    return cociente, resto  # Devuelve una tupla


print("\n----- 1.7 Retorno de múltiples valores -----")
q, r = dividir_y_resto(10, 3)     # q = 3, r = 1
print("Cociente:", q)
print("Resto:", r)
print("Sin desempaquetar:", dividir_y_resto(10, 3))   # (3, 1) -> es una tupla


# ---------------------------------------------------------------------
# 1.8. VARIABLES LOCALES Y GLOBALES
# ---------------------------------------------------------------------
#  - GLOBAL: se define fuera de cualquier función; se puede leer en todo
#    el archivo (usarla con precaución).
#  - LOCAL: se define dentro de una función y SOLO existe allí.
x = 10  # Variable global


def ejemplo():
    y = 5  # Variable local (solo existe dentro de ejemplo)
    print("Dentro de la función, x =", x)   # Puede LEER la global
    print("Dentro de la función, y =", y)


print("\n----- 1.8 Variables locales y globales -----")
ejemplo()
print("Fuera de la función, x =", x)
# La siguiente línea daría error si se descomenta:
# print("Fuera de la función, y =", y)  # NameError: y no existe fuera de la función
#
# (Ojo: arriba en el 1.3 se creó otra y = 5 global. En un archivo
#  limpio, sin esa y, la línea comentada daría NameError.)
