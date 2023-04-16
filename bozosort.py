
from random import randint
from random import shuffle
from time import time
from threading import Thread

def criarLista(tamanho):
    list = []
    for i in range(tamanho):
        list.append(randint(0, 100))
    print("Lista criada com sucesso!")
    return list   

def bubbleSort(lista):
    start = time()
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    end = time()
    print("bubbleSort: ", end - start)
    return lista

def selectionSort(lista):
    start = time()
    for i in range(len(lista)):
        min = i
        for j in range(i + 1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    end = time()
    print("selectionSort: ", end - start)
    return lista

def insertionSort(lista):
    start = time()
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            j -= 1
    end = time()
    print("insertionSort: ", end - start)
    return lista

def mergeSort(lista):
    start = time()
    if len(lista) > 1:

        mid = len(lista) // 2

        left = lista[:mid]

        right = lista[mid:]

        mergeSort(left)

        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
            return lista

def mergeSortImplement(lista):
    start = time()
    mergeSort(lista)
    end = time()
    print("mergeSort: ", end - start)

lista = criarLista(10000)

t1 = Thread(target=bubbleSort, args=(lista,))
t2 = Thread(target=selectionSort, args=(lista,))
t3 = Thread(target=insertionSort, args=(lista,))
t4 = Thread(target=mergeSortImplement, args=(lista,))
t1.start()
t2.start()
t3.start()
t4.start()






