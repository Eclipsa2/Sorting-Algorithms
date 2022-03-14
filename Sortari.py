import copy
import random
import time
from copy import deepcopy
#Merge Sort
def mergeSort(listaNumere):
    n = len(listaNumere)
    if n == 1:
        return listaNumere
    mij = n//2
    stanga = []
    for i in range (0, mij):
        stanga.append(listaNumere[i])
    dreapta = []
    for i in range(mij, n):
        dreapta.append(listaNumere[i])

    #stanga = listaNumere[:mij]
    #dreapta = listaNumere[mij:]

    stanga = mergeSort(stanga)
    dreapta = mergeSort(dreapta)

    return merge(stanga, dreapta)

'''def merge(stanga, dreapta):
    aux = []
    while len(stanga) != 0 and len(dreapta) != 0:
        if stanga[0] < dreapta[0]:
            aux.append(stanga[0])
            del stanga[0]
        else:
            aux.append(dreapta[0])
            del dreapta[0]

    while len(stanga) != 0:
        aux.append(stanga[0])
        del stanga[0]

    while len(dreapta) != 0:
        aux.append(dreapta[0])
        del dreapta[0]

    return aux'''

def merge(stanga, dreapta):
    aux = []
    i,j = 0,0
    while i < len(stanga) and j < len(dreapta):
        if stanga[i] < dreapta[j]:
            aux.append(stanga[i])
            i += 1
        else:
            aux.append(dreapta[j])
            j += 1

    while i < len(stanga):
        aux.append(stanga[i])
        i += 1

    while j < len(dreapta):
        aux.append(dreapta[j])
        j += 1

    return aux

#Shell Sort - optim pt liste de numere de lungime medie(cateva mii)
def shellSort(listaNumere):
    n = len(listaNumere)
    mij = n//2
    while mij > 0:
        for i in range(mij, n):
            aux = listaNumere[i]
            j = i
            while j >= mij and listaNumere[j-mij] > aux:
                listaNumere[j] = listaNumere[j-mij]
                j -= mij
            listaNumere[j] = aux
        mij = mij // 2
    return listaNumere

#Insertion Sort - eficient pt liste scurte; cel mai intuitiv mod de sortare
def insertionSort(listaNumere):
    for i in range(1, len(listaNumere)):
        n = listaNumere[i]
        j = i

        while j > 0 and listaNumere[j-1] > n:
            listaNumere[j] = listaNumere[j-1]
            j -= 1

        listaNumere[j] = n
    return listaNumere

#Radix Sort
def nrCif(listaNumere):
    max = -1
    for nr in listaNumere:
        if max < nr:
            max = nr
    return len(str(max))

def radixSort(listaNumere):
    aux = [[] for i in range(10)]
    nrCifre = nrCif(listaNumere)
    for i in range (0, nrCifre):
        for nr in listaNumere:
            cif = (nr // (10 ** i))%10
            aux[cif].append(nr)
        listaNumere.clear()
        for lista in aux:
            for element in lista:
                listaNumere.append(element)
        aux = [[] for i in range(10)]
    return listaNumere

#QuickSort
def quickSort(listaNumere):
    if len(listaNumere) <= 1:
        return listaNumere

    pivot = listaNumere[(len(listaNumere)-1)//2]
    del listaNumere[(len(listaNumere)-1)//2]
    stanga = []
    dreapta = []
    for nr in listaNumere:
        if nr > pivot:
            dreapta.append(nr)
        else:
            stanga.append(nr)
    return quickSort(stanga) + [pivot] + quickSort(dreapta)

#functieVerif sortare
def test_sort(listaNumere):
    for i in range(0,len(listaNumere)-1):
        if listaNumere[i+1] < listaNumere[i]:
            return -1
    return 1

fisier = open("tests","r")
nrTeste = int(fisier.readline())

for i in range(nrTeste):
    linieInput = fisier.readline()
    linieInputSplit = linieInput.split(" ")
    n = int(linieInputSplit[0])
    Max = int(linieInputSplit[1])
    print(f"Test {i + 1}:\nN = {n} Max = {Max}")
    if n> 10**7:
        print("Antentie! Sortarile vor dura mai mult de 5 minute! Alegeti o dimensiune mai mica a listei")
    else:
        lista = []
        for i in range(0, n + 1):
            lista.append(random.randint(0, Max))

        cpy_lista = copy.deepcopy(lista)
        start = time.time()
        rezultat = mergeSort(lista)
        if test_sort(rezultat) == 1:
            print(f"Merge sort: {time.time() - start} secunde")

        lista = copy.deepcopy(cpy_lista)
        start = time.time()
        rezultat = shellSort(lista)
        if test_sort(rezultat) == 1:
            print(f"Shell sort: {time.time() - start} secunde")

        lista = copy.deepcopy(cpy_lista)
        if n >= 10 ** 5:
            print(
                "Atentie! Aceasta sortare va dura mai mult de 5 minute pentru algoritmul de Insertion Sort! Alegeti o dimensiune mai mica a listei")
        else:
            start = time.time()
            rezultat = insertionSort(lista)
            if test_sort(rezultat) == 1:
                print(f"Insertion sort: {time.time() - start} secunde")

        lista = copy.deepcopy(cpy_lista)
        start = time.time()
        rezultat = radixSort(lista)
        if test_sort(rezultat) == 1:
            print(f"Radix sort: {time.time() - start} secunde")

        lista = copy.deepcopy(cpy_lista)
        start = time.time()
        rezultat = quickSort(lista)
        if test_sort(rezultat) == 1:
            print(f"Quick sort: {time.time() - start} secunde")

        lista = copy.deepcopy(cpy_lista)
        start = time.time()
        rezultat = lista.sort()
        print(f"Algoritm sortare default al compilatorului: {time.time() - start} secunde")
        print()






