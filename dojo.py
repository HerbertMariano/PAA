def merge(lista1, lista2):
    i = j = 0
    aux = []

    while (i < len(lista1)) and (j < len(lista2)):
        if lista1[i] < lista2[j]:
            aux.append(lista1[i])
            i += 1

        else:
            aux.append(lista2[j])
            j += 1

    while i < len(lista1):
        aux.append(lista1[i])
        i += 1

    while j < len(lista2):
        aux.append(lista2[j])
        j += 1

    return aux

def merge_sort(lista, inicio, fim):
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        lista1 = lista[inicio:meio]
        lista2 = lista[meio:fim]
        lista[inicio:fim] = merge(lista1, lista2)


def main():
    lista = [4, 9, 2, 11, 27, 13, 17, 8]
    n = len(lista)
    merge_sort(lista, 0, n)
    print(lista)

main()
