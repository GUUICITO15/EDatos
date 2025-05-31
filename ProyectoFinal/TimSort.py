import random

class Timsort():
    minRun = 32
    
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)

    
    def insertion(self, arr, izquierda, derecha):
        def comparar(a,b):
            return a < b if self.reverse else a > b
        
        for i in range(izquierda + 1, derecha + 1):
            key = arr[i]
            j = i - 1
            
            while(j >= izquierda and comparar(arr[j], key)):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    def merge(self, arr, izquierda, medio, derecha):
        def comparar(a,b):
            return a >= b if self.reverse else a <= b
        arrIz = arr[izquierda:medio + 1]
        arrDe = arr[medio + 1:derecha + 1]
        
        contI, contD, base = 0, 0, izquierda
        
        while(contI < len(arrIz) and contD < len(arrDe)):
            
            if comparar(arrIz[contI],arrDe[contD]):
                arr[base] = arrIz[contI]
                contI += 1
            else:
                arr[base] = arrDe[contD]
                contD += 1
            base += 1
        
        while(contI < len(arrIz)):
            arr[base] = arrIz[contI]
            contI += 1
            base += 1
        
        while(contD < len(arrDe)):
            arr[base] = arrDe[contD]
            contD += 1
            base += 1
    
    def sort(self, arr):
        tamanio = len(arr)
        
        for i in range(0, tamanio, self.minRun):
            self.insertion(arr=arr, izquierda=i, derecha=min(i + self.minRun - 1, tamanio - 1))
        
        grupos = self.minRun
        while (grupos < tamanio):
            for left in range(0, tamanio, grupos * 2):
                mid = left + grupos - 1
                right = min(left + grupos * 2 - 1, tamanio - 1)
                if mid < right:
                    self.merge(arr=arr, izquierda=left, medio=mid, derecha=right)
            grupos *= 2

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
Timsort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
Timsort(arreglo, True)

print(arreglo)