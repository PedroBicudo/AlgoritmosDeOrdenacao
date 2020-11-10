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

                self._trocar_valores_de_posicao(lista_numeros, i, j)
                
        self._trocar_valores_de_posicao(lista_numeros, i+1, fim)
        
        return i + 1

    def _trocar_valores_de_posicao_na_lista(self, lista, pos_primeira, pos_segunda):
        tmp = lista[pos_primeira]
        lista[pos_primeira] = lista[pos_segunda]
        lista[pos_segunda] = tmp