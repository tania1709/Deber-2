#Matriz 3D Temperaturas
temperaturas = [
    # Ciudad 1
    [
        [22, 23, 25, 26, 27, 28, 29],  # Semana 1
        [23, 24, 26, 27, 28, 29, 30],  # Semana 2
        [24, 25, 27, 28, 29, 30, 31],  # Semana 3
        [25, 26, 28, 29, 30, 31, 32]  # Semana 4
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

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in range(len(temperaturas)):
    for semana in range(len(temperaturas[ciudad])):
        promedio = sum(temperaturas[ciudad][semana]) / len(temperaturas[ciudad][semana])
        print(f"Promedio de temperatura para la ciudad {ciudad + 1} en la semana {semana + 1}: {promedio:.2f}°C")
