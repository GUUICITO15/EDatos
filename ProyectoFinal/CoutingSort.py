import random

class CoutingSort:
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)
        
    def sort(self, arr):
        if not arr:
            return
        
        tamanio = len(arr)
        valor_max = max(arr)
        valor_min = min(arr)
        rango = valor_max - valor_min + 1
        
        output = [0] * tamanio
        count = [0] * rango
        
        for num in arr:
            count[num - valor_min] += 1
        
        if not self.reverse:
            for i in range(1, rango):
                count[i] += count[i - 1]
        else:
            for i in range(rango - 2, -1, -1):
                count[i] += count[i + 1]

        for i in reversed(range(tamanio)):
            num = arr[i]
            count[num - valor_min] -= 1
            output[count[num - valor_min]] = num

        for i in range(tamanio):
            arr[i] = output[i]

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
CoutingSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
CoutingSort(arreglo, True)

print(arreglo)