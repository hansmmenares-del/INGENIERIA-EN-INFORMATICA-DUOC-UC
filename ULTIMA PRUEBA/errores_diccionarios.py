dic = {
    "nombre" : "pedro",
    "direccion" : "Direccion/calle/numeroxx",
    "color": ["rojo", "verde", "amarillo"], 
    "hermanos" : {
        "name" : "juan",
        "color": "verde",
        "edad" : 15
    }
}
print(dic.get("nombree"))
print(dic["nombre"])
print(dic.keys()) ### ENTREGA TODAS LAS KEYS
print(dic.get("nombre"))

for clave, valor in dic.items():
    print(f"CLAVE: {clave} - VALOR: {valor}")

## insertar dic en una lista