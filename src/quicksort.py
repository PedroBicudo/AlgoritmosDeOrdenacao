import random

class Quick_Sort():

    def quicksort(self,lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista) - 1
        if inicio < fim:
            posPivo = self.particao(lista, inicio, fim)
            # recursivamente na sublista à esquerda (menores)
            self.quicksort(lista, inicio, posPivo-1)
            # recursivamente na sublista à direita (maiores)
            self.quicksort(lista, posPivo+1, fim)

    def particao(self,lista, inicio, fim):
        pivo = lista[fim]
        i = inicio
        for j in range(inicio, fim):
            # j sempre avança, pois representa o elemento em análise
            # e delimita os elementos maiores que o pivô
            if lista[j] <= pivo:
                lista[j], lista[i] = lista[i], lista[j]
                # incrementa-se o limite dos elementos menores que o pivô
                i = i + 1
        lista[i], lista[fim] = lista[fim], lista[i]
        return i
