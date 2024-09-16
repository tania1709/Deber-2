#Matriz 3D Temperaturas
# Datos de temperaturas
temperaturas = [
  # Ciudad 1
  [
    [22, 23, 25, 26, 27, 28, 29],
    [23, 24, 26, 27, 28, 29, 30],
    [24, 25, 27, 28, 29, 30, 31],
    [25, 26, 28, 29, 30, 31, 32]
  ],

  # Ciudad 2
  [
    [20, 21, 23, 24, 25, 26, 27],
    [21, 22, 24, 25, 26, 27, 28],
    [22, 23, 25, 26, 27, 28, 29],
    [23, 24, 26, 27, 28, 29, 30]
  ],

  # Ciudad 3
  [
    [18, 19, 21, 22, 23, 24, 25],
    [19, 20, 22, 23, 24, 25, 26],
    [20, 21, 23, 24, 25, 26, 27],
    [21, 22, 24, 25, 26, 27, 28]
  ],

  # Ciudad 4
  [
    [15, 16, 18, 19, 20, 21, 22],
    [16, 17, 19, 20, 21, 22, 23],
    [17, 18, 20, 21, 22, 23, 24],
    [18, 19, 21, 22, 23, 24, 25]
  ],

  # Ciudad 5
  [
    [12, 13, 15, 16, 17, 18, 19],
    [13, 14, 16, 17, 18, 19, 20],
    [14, 15, 17, 18, 19, 20, 21],
    [15, 16, 18, 19, 20, 21, 22]
  ]
]

# Nombres de las ciudades
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3", "Ciudad 4", "Ciudad 5"]

# Calcular promedio de temperaturas para cada semana de cada ciudad
for i, ciudad in enumerate(ciudades):
  print(f"Resultados para {ciudad}:")
  for j, semana in enumerate(temperaturas[i]):
    promedio = sum(semana) / len(semana)
    print(f"  Semana {j + 1}: {promedio:.2f}°C")
  print()

#Resultados para Ciudad 1:
Semana 1: 25.71°C
Semana 2: 26.43°C
Semana 3: 27.43°C
Semana 4: 28.43°C


#Resultados para Ciudad 2:
Semana 1: 23.86°C
Semana 2: 24.86°C
Semana 3: 25.86°C
Semana 4: 26.86°C


#Resultados para Ciudad 3:
Semana 1: 21.86°C
Semana 2: 22.86°C
Semana 3: 23.86°C
Semana 4: 24.86°C


#Resultados para Ciudad 4:
Semana 1: 18.57°C
Semana 2: 19.57°C
Semana 3: 20.57°C
Semana 4: 21.57°C


#Resultados para Ciudad 5:
Semana 1: 15.71°C
Semana 2: 16.71°C
Semana 3: 17.71°C
Semana 4: 18.71°C


¡Ejecución completada!

