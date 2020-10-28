class BinaryInsertionSort:

    def binary_search(self, lista_numeros, key, start, end) -> int:
        """Realiza a busca do valor no lista_numeros."""
        while start <= end:
            mid = (start + end) // 2
            if lista_numeros[mid] == key:
                return mid
            
            elif lista_numeros[mid] > key:
                end = mid - 1
            
            else:
                start = mid + 1
        
        return start
            

    def binary_insertion_sort(self, lista_numeros):
        for i in range(1, len(lista_numeros)):
            j = i - 1
            key = lista_numeros[i]
            location = self.binary_search(lista_numeros, key, 0, j)
            
            while j >= location:
                lista_numeros[j+1] = lista_numeros[j]
                j -= 1

            lista_numeros[j+1] = key    
