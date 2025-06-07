import random

class ShellSort():
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)

    
    def sort(self, arr):
        def comparar(a, b):
            return a < b if self.reverse else a > b
        
        tamanio = len(arr)
        gap = tamanio // 2
        
        while gap > 0:
            for i in range(gap, tamanio):
                key = arr[i]
                j = i
                
                while(j >= gap and comparar(arr[j - gap], key)):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = key
            gap //= 2

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
ShellSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
ShellSort(arreglo, True)

print(arreglo)