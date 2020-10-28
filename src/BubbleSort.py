class BubbleSort():

    def bubble_sort(self, lista_numeros):
        lista_tamanho = len(lista_numeros)
        for i in range(lista_tamanho - 1):
            for x in range(0, lista_tamanho - i - 1):
                if lista_numeros[x] > lista_numeros[x + 1]:
                    tmp = lista_numeros[x]
                    lista_numeros[x] = lista_numeros[x + 1]
                    lista_numeros[x + 1] = tmp