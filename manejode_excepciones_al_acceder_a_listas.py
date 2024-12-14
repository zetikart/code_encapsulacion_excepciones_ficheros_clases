# declaramos una lista
# accedemos a los elementos a traves del operador[]
# si accedemos a un elemento que esta fuera de rango

try:
    lista = ['python', 'java', 'c++']
    print(lista[0])
    print(lista[1])
    print(lista[2])   
    print(lista[3])
except Exception:
    print(BaseException)
