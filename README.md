# Coronavirus_Twitter

### Como funciona?

### Bot 1
O programa faz a raspagem de dados no site que contém as informações sobre a situação de todos os países lidando com o Coronavírus no mundo.
Após isso, o programa trata as informações, separando os países em lista de continentes, colocando emojis de suas bandeiras e atribuindo um padrão para a forma de exibição das informações de nome e demais textos.
Feito isso, é criada uma lista com as mensagens a serem postadas (por padrão, são 15 tweets, 1 que informa a situação do continente no geral e outros 14 que informam a situação de 14 países daquele continente).
A lista de mensagens é então enviada para uma API que é responsável por montar a Thread(conjunto de mensagens).
A Thread é então enviada para o Bot que a posta na ordem correta.

### Bot 2
O programa está constantemente monitorando o perfil do Bot 1 à procura de novas threads, que, quando encontrada são retweetadas. A finalidade disso é organizar as threads em um perfil separado, já que o próprio twitter não organiza as threads no perfil do usuário. Assim, o Bot2 retweeta apenas o tweet inicial de cada thread, que serve de gancho para quem quiser ver a thread completa no perfil do Bot 1.

### Avisos
Por questões de segurança as informações de token e ID dos Bots foram retiradas dos arquivos upados, sendo necessário inserir os dados de outros Bots para o funcionamento do programa

O programa está rodando atualmente e pode acessado pelo link abaixo:

##### link Bot 1 = https://twitter.com/Coronavirus_upt

##### link Bot 2 = https://twitter.com/Corona_upt

O programa faz uma nova postagem a cada 2.5 horas

Com o objetivo de entender o funcionamento de diferentes plataformas, cada Bot foi hospedado em um server diferente.

O Bot1 foi hospedado na plataforma Evennode = https://www.evennode.com/

O Bot2 foi hospedado em uma instância linux da Amazon AWS = https://aws.amazon.com/

### Vídeo demonstrativo

[![ITwitter Bot Coronavírus](https://img.youtube.com/vi/8j5k7DxnHEU/0.jpg)](https://www.youtube.com/watch?v=8j5k7DxnHEU)

