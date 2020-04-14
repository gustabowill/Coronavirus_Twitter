# Coronavirus_Twitter

O programa faz a raspagem de dados no site que contém as informações sobre a situação de todos os países lidando com o Coronavírus no mundo.
Após isso, o programa trata as informações, separando os países em lista de continentes, colocando emojis de suas bandeiras e atribuindo um padrão para a forma de exibição das informações de nome e demais textos.
Feito isso, é criada uma lista com as mensagens a serem postadas (por padrão, são 15 tweets, 1 que informa a situação do continente no geral e outros 14 que informam a situação de 14 países daquele continente).
A lista de mensagens é então enviada para uma API que é responsável por montar a Thread(conjunto de mensagens).
A Thread é então enviada para o Bot que a posta na ordem correta.

(O programa está programado para fazer um post com uma thread a cada 2.5 horas)

Por questões de segurança as informações de token do Bot foram retiradas do arquivo upado Bot.py, sendo necessário inserir os dados de outro Bot para o funcionamento do programa

O programa está rodando atualmente e pode acessado pelo link abaixo:

link = https://twitter.com/Coronavirus_cha

Caso seja aberto no Desktop, a exibição é diferente, sendo mais desorganizada do que a apresentada no vídeo abaixo.


### Vídeo Demonstrativo

[![](http://img.youtube.com/vi/X_n4xrU1I6E/0.jpg)](http://www.youtube.com/watch?v=X_n4xrU1I6E "Vídeo Demonstrativo")


