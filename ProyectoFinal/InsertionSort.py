import random

class InsertionSort():
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)

    
    def sort(self, arr):
        def comparar(a,b):
            return a < b if self.reverse else a > b
        tamanio = len(arr)
        
        for i in range(tamanio):
            key = arr[i]
            j = i - 1
            
            while(j >= 0 and comparar(arr[j], key)):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
InsertionSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
InsertionSort(arreglo, True)

print(arreglo)