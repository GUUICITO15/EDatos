import random

class SelectionSort:
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)
        
    def sort(self, arr):
        def comparar(a,b):
            return a > b if self.reverse else a < b
        
        tamanio = len(arr)
        
        for i in range(tamanio):
            min_idx = i
            for j in range(i+1, tamanio):
                if comparar(arr[j], arr[min_idx]):
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
SelectionSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
SelectionSort(arreglo, True)

print(arreglo)