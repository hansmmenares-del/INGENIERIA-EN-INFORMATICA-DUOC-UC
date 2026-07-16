import random as ran
cantidad_prod,defectuosos,aceptables,excelentes,total_puntaje=0,0,0,0,0
list_prod_puntaje,list_prod_names,list_defectuoso,list_aceptable,list_excelente=[],[],[],[],[]
while cantidad_prod!=50:
    num=ran.randint(1,100)
    cantidad_prod+=1
    total_puntaje+=num
    list_prod_puntaje.append(num)
    if num<40:
        defectuosos+=1
    elif num>=40 and num<=79:
        aceptables+=1
    elif num>=80:
        excelentes+=1
                
##### Lo que sigue con las listas es innecesario pero me gustó para practicar #####

for i in range(len(list_prod_puntaje)):
    list_prod_names.append(f"Producto {i+1} = {list_prod_puntaje[i]}")
    if list_prod_puntaje[i]<40:
        list_defectuoso.append(f"Producto {i+1} = {list_prod_puntaje[i]}")
    elif list_prod_puntaje[i]>=40 and list_prod_puntaje[i]<=79:
        list_aceptable.append(f"Producto {i+1} = {list_prod_puntaje[i]}")
    elif list_prod_puntaje[i]>=80:
        list_excelente.append(f"Producto {i+1} = {list_prod_puntaje[i]}")

#####                                                                         #####      
print(f"Excelentes: {list_excelente}\n\nAceptables: {list_aceptable}\n\nDefectuosos: {list_defectuoso}\n\nTOTAL PUNTAJE: {total_puntaje}\nCANTIDAD EXCELENTES: {excelentes}\nCANTIDAD ACEPTABLES: {aceptables}\nCANTIDAD DEFECTUOSOS: {defectuosos}")