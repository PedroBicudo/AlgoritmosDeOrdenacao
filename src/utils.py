import easygui
import _io
from typing import List
# from src import Bubble_Sort
# from src import BinaryInsertionSort
# import timeit
# from src import teste

class FileUtils():

    def getNumerosFromFile(self) -> List[int]:
        numbers = []
        file_content = self._abrir_arquivo()
        for line in file_content:
            valor = int(self._remover_break_line(line))
            numbers.append(valor)
        return numbers
    
    def _remover_break_line(self, text: str) -> str:
        return text.replace("\n", "")

    def _abrir_arquivo(self) -> _io.TextIOWrapper:
        file_path = self._obter_caminho_do_arquivo_usando_easygui()
        file = open(f"{file_path}", "r")
        return file

    def _obter_caminho_do_arquivo_usando_easygui(self) -> str:
        return easygui.fileopenbox()
    
    def rodarMetodos(self, lista) -> List[float]:
        tempo = []
        #Instanciando os metodos
        Bubsort = Bubble_Sort.bubble_sort()
        quick = teste.Quick_Teste()
        binary = BinaryInsertionSort.BinaryInsertionSort()
        #Recebendo a lista e marcando o tempo de execução de cada metodo em uma lista
        Inicio = timeit.default_timer()
        Bubsort.bubbleSort(lista)
        print('bubble')
        Fim = timeit.default_timer()
        tempo.append(Fim-Inicio)
        Inicio = timeit.default_timer()
        binary.binary_insertion_sort(lista)
        Fim = timeit.default_timer()
        tempo.append(Fim-Inicio)
        print('binary')
        Inicio = timeit.default_timer()
        quick.quickSort(lista, 0, len(lista) - 1)
        print('quick')
        Fim = timeit.default_timer()
        tempo.append(Fim-Inicio)

        return tempo