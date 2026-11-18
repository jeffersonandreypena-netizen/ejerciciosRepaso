'''persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}
print(persona["nombre"])      # Ana
print(persona.get("correo"))  # None (no existe esa clave)

persona["correo"] = "ana@example.com"
persona["edad"] = 26
persona.update({"pais": "Colombia"})

valor = persona.pop("correo", None) 
ultimo = persona.popitem() 
print(persona)

for clave in persona.keys ():
    print("Clave:", clave)

for valor in persona.values ():
    print("Valor:", valor)

for clave, valor in persona.items():
    print(clave, "→", valor)'''


'''persona1 = {"nombre": "Jefferson", "apellido": "Peña", "edad": 26, "correo": "jefferchitto@gmail.com", "Hobbies": ["estudiar", "trabajar", "comer"]}
print(persona1)

persona1 ["edad"] = 27

print (persona1)

print (persona1["Hobbies"][0])

for i in persona1 ["Hobbies"]:
    print (i)

for i in persona1["Hobbies"] [0:2]:
    print (i)

persona1 ["edad"] = "test"

print (persona1)'''


'''matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz[1][1]=99
print(matriz)

for i in range(len(matriz)):
    for j in range(len (matriz[i])):
        print (matriz[i][j], end=" ")
    print()'''


filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Elemento [{i},{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("Matriz ingresada:")
for fila in matriz:
    print(fila)
