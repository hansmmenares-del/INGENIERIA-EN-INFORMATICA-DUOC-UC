dic = {
    #  Key   :   Value
    "nombres":"Pedrito",
    
    "apellido" : "Dias",
    
    "edad" : 19,
    
    "colores fav" :[
        "verde", "rojo"
        ],
    
    "juegos fav" : [
        "minecraft", "cs"
        ],
    
    "hermanos" : [
        {
        "nombre" : "Juanito",
        "apellido" : "Dias"
        },
        {
        "nombre" : "Dieguito",
        "apellido" : "Dias"  
        }
        ]
    }

print(dic["hermanos"][1]["nombre"])
for i in dic["hermanos"]:
    print(i["nombre"])






