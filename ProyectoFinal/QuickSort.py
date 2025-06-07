import random

class QuickSort:
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr, 0, len(arr) - 1)
    
    def sort(self, arr, low, high):
        if low < high:
            pi = self.particion(arr, low, high)
            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)
    
    def particion(self, arr, low, high):
        def comparar(a,b):
            return a > b if self.reverse else a < b
        
        pivote = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if comparar(arr[j], pivote):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
QuickSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
QuickSort(arreglo, True)

print(arreglo)