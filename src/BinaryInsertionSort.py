from typing import List

class BinaryInsertionSort:

    def binary_search(self, lista_numeros, key, start, end) -> int:
        """Realiza a busca do valor no lista_numeros."""
        if end <= start:
            if key > lista_numeros[start]:
                return start+1
            else:
                return start
        
        mid = (start + end) // 2
        if lista_numeros[mid] == key:
            return mid + 1
        
        if key > lista_numeros[mid]:
            return self.binary_search(lista_numeros, key, mid+1, end)
        else:
            return self.binary_search(lista_numeros, key, start, mid-1)

    def binary_insertion_sort(self, lista_numeros) -> List[int]:
        """Ordena a lista"""
        for i in range(1, len(lista_numeros)):
            j = i - 1
            key = lista_numeros[i]
            location = self.binary_search(lista_numeros, key, 0, j)
            
            while j >= location:
                lista_numeros[j+1] = lista_numeros[j]
                j -= 1

            lista_numeros[j+1] = key
        
        return lista_numeros
    
