list =[8,3,12,4,2,9,7,1]

def particionado(list):

    pivote = list[0]
    menor = []
    mayor = []

    for i in range(1, len(list)):
        if list[i] < pivote:
            menor.append(list[i])
        else:
            mayor.append(list[i])
    
    return menor,pivote,mayor

def quicksort(list):
    if len(list) < 2:
        return list

    menor, pivote,mayor=particionado(list)
    return quicksort(menor)+[pivote]+quicksort(mayor)
print(quicksort(list))