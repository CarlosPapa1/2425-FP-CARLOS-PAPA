# Calcular el promedio de las temperaturas de diferentes ciudades
# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (Cayambe, Puyo, Chone)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1-Cayambe
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ]
    ],
    [   # Ciudad 2- Puyo
        [   # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Ciudad 3-Chone
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
Ciudades = ["ciudad 1-Cayambe", "ciudad 2-Puyo", "ciudad 3-Chone"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad) :
        suma_temperatura = sum([dia["temp"] for dia in semana])
        promedio = suma_temperatura / len(semana)
        print(f'Promedio de temperaturas en {Ciudades[ciudad_idx]}, semana {semana_idx + 1} : {promedio: .2f} grados')
