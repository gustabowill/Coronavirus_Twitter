import raspagem
from bot import api, post_tweets
import os
import time
from tqdm import tqdm
from threader import Threader
from googletrans import Translator

time.sleep(21600)
#Percorre cada lista de continente(com seus países)
for u in range(7):
  #Pega a lista com as listas dos continentes
  lista_geral = raspagem.Raspar()
  lista_final = lista_geral[u]
  
  #Tenta traduzir os nomes dos países e continentes
  try:
    translator = Translator()
    for i in lista_geral[0]:
      if i.nome == 'Iran':
        i.nome = 'Irã'
      elif i.nome == 'Brazil':
        i.nome = 'Brasil'
      elif i.nome == 'Turkey':
        i.nome = 'Turquia'
      else:
        i.nome = translator.translate(i.nome,dest='pt').text
        i.continente = translator.translate(i.continente,dest='pt').text
  except:
    print('Não foi possível fazer a tradução')

  #Cria uma string com os dados do continente a ser mostrado
  mensagem = []
  threads = []
  mensagem_paises = "\n\n\U0001F637Casos: --------------> {}\n\u2620\uFE0FMortes: -------------> {}\n\U0001F340Curados: -----------> {} \n\u203C\uFE0FMortalidade: -----> {}%".format(lista_final[0].caso,lista_final[0].morte,lista_final[0].curado,lista_final[0].fatalidade)
  
  #Cria uma string com o nome do continente a ser mostrado
      #Execção para os dados mundiais, já que não são de nenhum continente específico
  if lista_final[0].nome == 'World' or lista_final[0].nome == 'Mundo':
    mensagem_final = '#Coronavírus no Mundo\U0001F30E' + mensagem_paises + '\n\n\u26A0\uFE0FDetalhes na Thread\n\n'
    threads.append(mensagem_final)
  else:
    mensagem_final = '#Coronavírus - {}'.format((lista_final[0].continente).upper()) + mensagem_paises + '\n\n\u26A0\uFE0FDetalhes na Thread\n\n'
    threads.append(mensagem_final)

  #Cria a string com os dados de cada país
      #Execção para a Oceania, já que se possui os dados de apenas 6 países
  if lista_final[0].continente == 'Oceania':
    for h in range(1,7):
      string = "{}{}{}\n\n\U0001F637Casos: {}\n\u2620\uFE0FMortes: {}\n\U0001F340Curados: {} \n\u203C\uFE0FMortalidade: {}%\n\U0001F9EATestes feitos: {}\n\n".format(lista_final[h].emoji,(lista_final[h].nome).upper(),lista_final[h].emoji,lista_final[h].caso,lista_final[h].morte,lista_final[h].curado,lista_final[h].fatalidade,lista_final[h].teste)
      threads.append(string)

  else:
    for h in range(1,15):
      string = "{}{}{}\n\n\U0001F637Casos: {}\n\u2620\uFE0FMortes: {}\n\U0001F340Curados: {} \n\u203C\uFE0FMortalidade: {}%\n\U0001F9EATestes feitos: {}\n\n".format(lista_final[h].emoji,(lista_final[h].nome).upper(),lista_final[h].emoji,lista_final[h].caso,lista_final[h].morte,lista_final[h].curado,lista_final[h].fatalidade,lista_final[h].teste)
      threads.append(string)


  #Organiza as Threads e as envia
  th = Threader(threads, api, wait=5, end_string=False)
  th.send_tweets()
  time.sleep(9000)

time.sleep(800)
