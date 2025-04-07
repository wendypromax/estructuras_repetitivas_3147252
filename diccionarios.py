##Diccionarios:


##Son coleciones de datos
##cada elemento en un diccionario
##se puede dividir en 2 partes:
# ##   1. clave: el valor del elemento
# ##   2. valor: el valor del elemento
##EJEMPLO  de diccionario:
## Para caracterizar un pais:

Pais = {
    "nombre": "colombia",
    "capital": "bogota",
    "idioma":  "español",
    "poblacion": 51,
    "superficie": 1141748,
    "moneda": "peso colombiano",
    "ciudades": [
     "Bogota",
     "Medellin",
     "Cali",
     "Barranquilla",
     "Cartagena"
    ]
}
#acceder a propiedades:
print("capital de colombia:", Pais["capital"])
print("y se habla:", Pais["idioma"])
print("habitantes:", Pais["poblacion"])
print("y sus ciudades son:")
for ciudad in Pais ["ciudades"]:
    print(ciudad)

