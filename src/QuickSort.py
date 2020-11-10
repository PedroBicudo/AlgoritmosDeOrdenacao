class QuickSort():
    
    def quick_sort(self, lista_numeros, inicio: int, fim: int):
        if inicio < fim:
            posPivo = self.particao(lista_numeros, inicio, fim)
            # recursivamente na sublista_numeros à esquerda (menores)
            self.quick_sort(lista_numeros, inicio, posPivo-1)
            # recursivamente na sublista_numeros à direita (maiores)
            self.quick_sort(lista_numeros, posPivo+1, fim)
 
    def particao(self, lista_numeros, inicio: int, fim: int):
        pivo = lista_numeros[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            # j sempre avança, pois representa o elemento em análise
            # e delimita os elementos maiores que o pivô
            if lista_numeros[j] <= pivo:
                # incrementa-se o limite dos elementos menores que o pivô
                i = i + 1

                tmp = lista_numeros[j]
                lista_numeros[j] = lista_numeros[i]
                lista_numeros[i] = tmp
                
        tmp = lista_numeros[i + 1]
        lista_numeros[i + 1] = lista_numeros[fim]
        lista_numeros[fim] = tmp
        
        return i + 1
