# https://api.boostr.cl/holidays.json
# En el link está el diccionario
dic = {
  "status": "success",
  "data": [
    {
      "date": "2026-01-01",
      "title": "Año Nuevo",
      "type": "Civil",
      "inalienable": True,
      "extra": "Civil e Irrenunciable"
    },
    {
      "date": "2026-04-03",
      "title": "Viernes Santo",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-04-04",
      "title": "Sábado Santo",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-05-01",
      "title": "Día Nacional del Trabajo",
      "type": "Civil",
      "inalienable": True,
      "extra": "Civil e Irrenunciable"
    },
    {
      "date": "2026-05-21",
      "title": "Día de las Glorias Navales",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-06-21",
      "title": "Día Nacional de los Pueblos Indígenas",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-06-29",
      "title": "San Pedro y San Pablo",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-07-16",
      "title": "Día de la Virgen del Carmen",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-08-15",
      "title": "Asunción de la Virgen",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-09-18",
      "title": "Independencia Nacional",
      "type": "Civil",
      "inalienable": True,
      "extra": "Civil e Irrenunciable"
    },
    {
      "date": "2026-09-19",
      "title": "Día de las Glorias del Ejército",
      "type": "Civil",
      "inalienable": True,
      "extra": "Civil e Irrenunciable"
    },
    {
      "date": "2026-10-12",
      "title": "Encuentro de Dos Mundos",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-10-31",
      "title": "Día de las Iglesias Evangélicas y Protestantes",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-11-01",
      "title": "Día de Todos los Santos",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-12-08",
      "title": "Inmaculada Concepción",
      "type": "Civil",
      "inalienable": False,
      "extra": "Civil"
    },
    {
      "date": "2026-12-25",
      "title": "Navidad",
      "type": "Civil",
      "inalienable": True,
      "extra": "Civil e Irrenunciable"
    }
  ]
}
# La idea es obtener la fecha de todos los feriados y lo que ocurre ese dia,
# especificamente porqué sería feriado.
for i in dic["data"]:
    print(i["date"])
    print(i["title"])