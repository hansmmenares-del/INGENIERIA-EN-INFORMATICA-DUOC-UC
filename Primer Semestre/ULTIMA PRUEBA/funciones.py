### 4 tipos de funciones
#### sin retorno, sin argumentos
#### con retorno, sin argumentos

### Parametros, es cuando se llama una funcion, cuando se crea la funcion, la funcion suma() no tiene parametros.

# tipo 1.
# SIN ARGUMENTOS Y SIN RETORNO
def sumar(): # PARENTESIS VACIO == sin argumentos, no retorna nada o retorna none
    print(10 + 10)
sumar() # -> No tiene argumentos.

def restar() -> int:
    'Esta funcion sin parametros, sin argumentos pero con retorno. Devuelve 100 - 70.'
    return 100-70

restar()
print(restar())

def mult(num1: int, num2: int):
    "Esta funcion multiplica la multiplicación entre dos números"
    print(num1 * num2)
mult(90, "ola")

def div(num1: int, num2: int) -> float:
    "Esta función devuelve la division entre dos numeros."
    return num1/num2
print(div(500,5))
    