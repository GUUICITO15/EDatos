import random

class MergeSort():
    minRun = 32
    
    def __init__(self, arr, reverse=False):
        self.reverse = reverse
        self.sort(arr)
    
    def sort(self, arr):
        def comparar(a,b):
            return a >= b if self.reverse else a <= b
        
        if len(arr) > 1:
            medio = len(arr) // 2
            arrIz = arr[:medio]
            arrDe = arr[medio:]
        
            self.sort(arrIz)
            self.sort(arrDe)
        
            contI, contD, base = 0, 0, 0
            
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

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
MergeSort(arreglo)

print(arreglo)

print("------------------")

arreglo = []
for i in range(100):
    arreglo.append(random.randint(0,100))

print(arreglo)

print()
MergeSort(arreglo, True)

print(arreglo)