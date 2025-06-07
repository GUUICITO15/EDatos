import random

class RadixSort:
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)
    
    def couting_sort(self, arr, exp):
        tamanio = len(arr)
        output = [0] * tamanio
        count = [0] * 10
        
        for i in range(tamanio):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        if not self.reverse:
            for i in range(1, 10):
                count[i] += count[i - 1]
        else:
            for i in range(8, -1, -1):
                count[i] += count[i + 1]

        for i in reversed(range(tamanio)):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(tamanio):
            arr[i] = output[i]

    def sort(self, arr):
        if not arr:
            return
        
        numero_max = max(arr)
        exp = 1
        
        while numero_max // exp > 0:
            self.couting_sort(arr, exp)
            exp *= 10


arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
RadixSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
RadixSort(arreglo, True)

print(arreglo)