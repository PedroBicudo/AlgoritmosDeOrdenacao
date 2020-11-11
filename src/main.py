from utils import FileUtils, TempoAlgoritmos
from matplotlib import pyplot
from typing import List
import matplotlib
import utils


class PlotAlgoritmos:
    ALGORITMOS = ['Bubble Sort', 'Binary Insertion Sort' ,'Quick Sort']
    
    def __init__(self):
        self.file_utils = FileUtils()
        self.tempo_algoritmos = TempoAlgoritmos()
        self._definir_o_estilo_de_plot()
        self._gerar_sub_plot_de_cada_quantidade_de_numeros()

    def _definir_o_estilo_de_plot(self):
        pyplot.style.use("classic")

    def _gerar_sub_plot_de_cada_quantidade_de_numeros(self):
        sub_plots = matplotlib.pyplot.subplots(3)
        self.sub_plot_mil_numeros = sub_plots[1][0]
        self.sub_plot_cinco_mil_numeros = sub_plots[1][1]
        self.sub_plot_dez_mil_numeros = sub_plots[1][2]
    
    def mostrar_plot_de_todas_as_quantias_de_numeros(self):
        self._definir_nomes_dos_labels_de_cada_sub_plot()
        pyplot.subplots_adjust(hspace=0.5)
        pyplot.show()

    def _definir_nomes_dos_labels_de_cada_sub_plot(self):
        self.sub_plot_mil_numeros.set(title="Grafico do Arquivo de 1000 Numeros", ylabel="Tempo")
        self.sub_plot_cinco_mil_numeros.set(title="Grafico do Arquivo de 5000 Numeros", ylabel="Tempo")
        self.sub_plot_dez_mil_numeros.set(title="Grafico do Arquivo de 10000 Numeros", ylabel="Tempo")
    
    def adicionar_tempo_de_mil_numeros_ao_plot(self):
        tempos = self._obter_tempo_de_execucao_dos_algoritmos()
        self.sub_plot_mil_numeros.bar(PlotAlgoritmos.ALGORITMOS, tempos)
        for index, value in enumerate(tempos):
            self.sub_plot_mil_numeros.text( index, value, str(value))

    def adicionar_tempo_de_cinco_mil_numeros_ao_plot(self):
        tempos = self._obter_tempo_de_execucao_dos_algoritmos()
        self.sub_plot_cinco_mil_numeros.bar(PlotAlgoritmos.ALGORITMOS, tempos)
        for index, value in enumerate(tempos):
            self.sub_plot_cinco_mil_numeros.text( index, value, str(value))

    def adicionar_tempo_de_dez_mil_numeros_ao_plot(self):
        tempos = self._obter_tempo_de_execucao_dos_algoritmos()
        self.sub_plot_dez_mil_numeros.bar(PlotAlgoritmos.ALGORITMOS, tempos)
        for index, value in enumerate(tempos):
            self.sub_plot_dez_mil_numeros.text(index, value, str(value))

    def _obter_tempo_de_execucao_dos_algoritmos(self) -> List[float]:
        numeros = self.file_utils.getNumerosFromFile()
        tempos = self.tempo_algoritmos.obter_tempo_de_execucao_de_cada_algoritmo(numeros)

        return tempos

def main():
    plot = PlotAlgoritmos()
    plot.adicionar_tempo_de_mil_numeros_ao_plot()
    plot.adicionar_tempo_de_cinco_mil_numeros_ao_plot()
    plot.adicionar_tempo_de_dez_mil_numeros_ao_plot()
    plot.mostrar_plot_de_todas_as_quantias_de_numeros()


if __name__ == '__main__':
    main()