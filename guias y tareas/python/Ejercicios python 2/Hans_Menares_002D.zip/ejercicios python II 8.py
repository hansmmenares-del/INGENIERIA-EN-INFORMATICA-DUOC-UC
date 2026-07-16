def año_bisiesto():
    año=int(input("Ingresa el año:\n"))
    if año%4==0 and año%100!=0 or año%400:
        print("Su año es bisiesto")
    else:
        print("Su año no es bisiesto")
año_bisiesto()