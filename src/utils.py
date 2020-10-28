from BinaryInsertionSort import BinaryInsertionSort
from BubbleSort import BubbleSort
from quicksort import Quick_Sort
from typing import List
import easygui
import _io
import sys
import timeit

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


class TempoAlgoritmos:

    def obter_tempo_de_execucao_de_cada_algoritmo(self, lista) -> List[float]:
        """Uma lista de contendo o tempo de algoritmo é retornada.

            posicao[0] -> Bubble Sort
            posicao[1] -> Binary Insertion Sort
            posicao[2] -> Quick Sort

        """
        lista_binary = lista.copy()
        lista_quick = lista.copy()
        lista_bubble = lista.copy()

        return [
            self._tempo_do_bubble_sort_para_ordenar_a_lista(lista_bubble),
            self._tempo_do_binary_insertion_sort_para_ordernar_a_lista(lista_binary),
            self._tempo_do_quick_sort_para_ordernar_a_lista(lista_quick)
        ]
        

    def _tempo_do_binary_insertion_sort_para_ordernar_a_lista(self, lista) -> float:
        binary_insertion_sort = BinaryInsertionSort()
        start = timeit.default_timer()
        binary_insertion_sort.binary_insertion_sort(lista)
        end = timeit.default_timer()

        return end - start

    def _tempo_do_quick_sort_para_ordernar_a_lista(self, lista) -> float:
        quick_sort = Quick_Sort()
        start = timeit.default_timer()
        quick_sort.quicksort(lista, 0, len(lista)-1)
        end = timeit.default_timer()
        
        return end - start    

    def _tempo_do_bubble_sort_para_ordenar_a_lista(self, lista) -> float:
        bubble_sort = BubbleSort()
        start = timeit.default_timer()
        bubble_sort.bubble_sort(lista)
        end = timeit.default_timer()
        
        return end - start