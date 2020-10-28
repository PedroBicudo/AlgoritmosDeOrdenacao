from utils import FileUtils, TempoAlgoritmos
import utils
from matplotlib import pyplot as plt

#Declaração de Variaveis e Parametros
metodos = ['Bubble Sort', 'Binary Insertion Sort' ,'Quick Sort']
plt.style.use("classic")
fig, (ax1,ax2,ax3) = plt.subplots(3)
#Começando a Contagem
Archive = utils.FileUtils()
valueArchive = Archive.getNumerosFromFile()
Tempo = TempoAlgoritmos().obter_tempo_de_execucao_de_cada_algoritmo(valueArchive)
print(Tempo)
ax1.bar(metodos,Tempo)


#Plotagem do graficos do arquivo de 5000 Numeros
Tempo = []
Archive = utils.FileUtils()
valueArchive = Archive.getNumerosFromFile()
Tempo = TempoAlgoritmos().obter_tempo_de_execucao_de_cada_algoritmo(valueArchive)
print(Tempo)
ax2.bar(metodos,Tempo)


#Plotagem do graficos do arquivo de 10000 Numeros
Tempo = []
Archive = utils.FileUtils()
valueArchive = Archive.getNumerosFromFile()
Tempo = TempoAlgoritmos().obter_tempo_de_execucao_de_cada_algoritmo(valueArchive)
print(Tempo)
ax3.bar(metodos,Tempo)


ax1.set(title="Grafico do Arquivo de 1000 Numeros", ylabel="Tempo")
ax2.set(title="Grafico do Arquivo de 5000 Numeros", ylabel="Tempo")
ax3.set(title="Grafico do Arquivo de 10000 Numeros", ylabel="Tempo")

plt.show()
print(Tempo)