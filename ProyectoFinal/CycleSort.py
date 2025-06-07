import random

class CycleSort:
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)
        
    def sort(self, arr):
        def comparar(a,b):
            return a > b if self.reverse else a < b
        
        tamanio = len(arr)
        
        for ini_cycle in range(tamanio - 1):
            item = arr[ini_cycle]
            pos = ini_cycle
            
            for i in range(ini_cycle + 1, tamanio):
                if comparar(arr[i], item):
                    pos += 1
            
            if pos == ini_cycle:
                continue
            
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

            while pos != ini_cycle:
                pos = ini_cycle
                for i in range(ini_cycle + 1, tamanio):
                    if comparar(arr[i], item):
                        pos += 1
                while item == arr[pos]:
                    pos += 1
                arr[pos], item = item, arr[pos]
                

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
CycleSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
CycleSort(arreglo, True)

print(arreglo)