import random

class HeapSort:
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)
    
    def heapify(self, arr, tamanio, i):
        def comparar(a,b):
            return a < b if self.reverse else a > b
        
        mayor = i
        iz = 2 * i + 1
        de = 2 * i + 2
        
        if iz < tamanio and comparar(arr[iz], arr[mayor]):
            mayor = iz
        if de < tamanio and comparar(arr[de], arr[mayor]):
            mayor = de
        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            self.heapify(arr, tamanio, mayor)
    
    
    def sort(self, arr):
        
        tamanio = len(arr)
        
        for i in range(tamanio // 2 - 1, -1, -1):
            self.heapify(arr, tamanio, i)
            
        for i in range(tamanio -1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)


arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
HeapSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
HeapSort(arreglo, True)

print(arreglo)