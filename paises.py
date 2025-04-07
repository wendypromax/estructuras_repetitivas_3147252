paises=[
    {
        "nombre":"colombia",
        "capital":"Bogota",
        "idioma":"español",
        "moneda":"peso colombiano",
        "ciudades":
        [
           {
               "nombre":"Bogota",
               "poblacion":8.2,
               "fundacion":1538,
            },
           {
               "nombre":"Medellin",
               "poblacion":7.4,
               "fundacion":1452,
            },
            {
               "nombre":"Cali",
               "poblacion":4.2,
               "fundacion":1465,
            },
        ]
    },
    { "nombre":"peru",
        "capital":"lima",
        "idioma":"español",
        "moneda":"sol",
        "ciudades":
        [
           {
               "nombre":"lima",
               "poblacion":8.0,
               "fundacion":1508,
            },
           {
               "nombre":"cuzco",
               "poblacion":9.0,
               "fundacion":1542,
            },
        ]
    },
    { "nombre":"japon",
        "capital":"tokio",
        "idioma":"japones",
        "moneda":"yen",
        "ciudades":
        [   
            {
               "nombre":"Tokio",
               "poblacion":8.1,
               "fundacion":1202,
            },
           {
               "nombre":"kioto",
               "poblacion":7.1,
               "fundacion":1524,
            },
            {
               "nombre":"osaka",
               "poblacion":4.3,
               "fundacion":1465,
            },
        ]
    },
    { "nombre":"Noruega",
        "capital":"oslo",
        "idioma":"noruego",
        "moneda":"corona noruega",
        "ciudades":
        [
           {
               "nombre":"oslo",
               "poblacion":8.4,
               "fundacion":1302,
            },
           {
               "nombre":"bergen",
               "poblacion":6.1,
               "fundacion":1434,
            },
            {
               "nombre":"bodo",
               "poblacion":4.9,
               "fundacion":1495,
            },
        ]
    }
]

#interar cada pais
print("---------------")
print("Recoddido de paises")
print("---------------")
for pais in paises:
    print("nombre:" ,pais["nombre"])
    print("capital:", pais["capital"])
    print("moneda:", pais["moneda"])
    print("idioma:", pais["idioma"])
    for ciudad in pais ["ciudades"]:
        print ("-nombre: " , ciudad["nombre"])
        print ("-poblacion: " , ciudad["poblacion"])
        print ("-fundacion: " , ciudad["fundacion"])
    print("---------------")