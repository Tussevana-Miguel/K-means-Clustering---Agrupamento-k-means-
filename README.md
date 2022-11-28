<h1 align="center"> K-means-Clustering---Agrupamento-k-means- </h1>

K-means clustering faz parte dos algoritmos pertencentes ao aprendizado não supervisionado que é um ramo do aprendizado de máquinas (Machine Learning) que aprende a partir de dados que não foram rotulados, classificados ou categorizados. Em vez de responder ao feedback, a aprendizagem não supervisionada identifica as semelhanças nos dados e reage com base na presença ou ausência dessas semelhanças em cada novo dado. 

**Como funciona o K-means**
  
  No agrupamento de k-means, tentamos separar os dados em k clusters, os dados geralmente têm que estar na forma de vetores numéricos. Estritamente falando, o método funcionará desde que você tenha uma maneira de calcular a média de um conjunto de pontos de dados e a distância euclidiana entre eles. 
  K-means vem de modelos de centróide de algoritmos de agrupamento. O algoritmo k-means pertence à família de algoritmos chamados de algoritmos de otimização de agrupamento. Ou seja, os exemplos são divididos em grupos de clusters, de forma que o cluster dê bons resultados de acordo com os critérios definidos. O nome do algoritmo foi derivado de forma que os k clusters são formados a partir do conjunto de dados em que o centro do cluster é a média aritmética de todos os objetos dentro desse tipo de cluster. O número de clusters k é conhecido de antemão. A primeira etapa é encontrar os centróides iniciais para cada cluster. A próxima etapa é associar cada objeto de dados a seu centróide mais próximo. O agrupamento inicial é feito atribuindo cada dado, objeto ao centróide que está tão próximo a ele e a primeira iteração é concluída. O algoritmo funciona em iterações até que os objetos não mudem seus centros de cluster. Os centróides movem suas posições até que os critérios de convergência sejam alcançados. 
  
  <img src="https://miro.medium.com/max/786/1*rwYaxuY-jeiVXH0fyqC_oA.gif" width="500" height="400">

**Lembre que:**
1. O "centro do cluster (centróide)" é a média aritmética de todos os pontos pertencentes ao cluster.
2. Cada ponto está mais próximo de seu própriocentróide do que de outros centróides. 
3. Essas duas suposições são a base do modelo k-means. Em breve, mergulharemos exatamente em como o algoritmo chega a essa solução. 

**Um simples Algoritmo de funcionamento de K-means clustering**
Algoritmo de agrupamento K-mean 

**Entrada:** 

Conjunto de dados  

Número de clusters k  

**Saída:** 

O conjunto de número de clusters obtidos. 

Passos: 

Escolhaaleatoriade objetos do conjunto de dados como centróides iniciais. 
Repita
Associe cada objeto ao seu mais próximo 

centróide; 

Para cada cluster, a nova média é
calculado; 

Até que o ponto de convergência seja alcançado. 

O algoritmo converge quando a atribuição de registros aos clusters torna-se constante (quer dizer os integrantes de cada cluster já não mudam). 

O algoritmo funciona essencialmente supondo o primeiro k “centros” dos clusters propostos. Em seguida, cada ponto de dados é atribuído ao centro de que está mais próximo, criando um agrupamento de dados e, em seguida, todos os centros são movidos para a posição média de seus clusters. Isso é repetido até que um equilíbrio seja alcançado. Como os centros iniciais são escolhidos aleatoriamente, diferentes inicializações para a função não levarão necessariamente ao mesmo resultado. No mínimo, espere que a rotulagem dos clusters seja diferente dependendo da inicialização que teve lugar. 

**Escolhendo o número de Clusters “K”**

O algoritmo K-means requer que você especifique o número de clusters K. Às vezes, o número de clusters é orientado pela necessidade da entidade que a aplica. Por exemplo, uma empresa que gerencia uma equipe de vendas pode querer agrupar os clientes em “personas” para enfocar e orientar as ligações de vendas. Nesse caso, as considerações gerenciais ditariam o número de segmentos de clientes desejados - por exemplo, dois podem não produzir uma diferenciação útil de clientes, enquanto oito podem ser muito para gerenciar. 

Na ausência de um número de cluster ditado por considerações práticas ou gerenciais, uma abordagem estatística pode ser usada. Não existe um método padrão único para encontrar o “melhor” número de clusters. 

 Uma abordagem comum, chamada de método do cotovelo (Elbow method), é identificar quando o conjunto de clusters explica “a maior parte” da variação nos dados. Adicionar novos clusters além desse conjunto contribui relativamente pouco na variação explicada. O cotovelo é o ponto onde a variância cumulativa explicada se aplaina depois de subir abruptamente, daí o nome do método. 
 
 A imagem mostra claramente o cotovelo no ponto 4, querendo dizer que o numero de clusters ideal é 4.
 
 <img src="https://miro.medium.com/max/828/1*eVyOdx4gIcGWQ3lF4xAu6g.webp" width="400" height="300">
 
 **Agrupamento hierárquico no k-means clustering**
 
 <img src="https://miro.medium.com/max/828/0*NYmQ-gam67WzzdgY.png" width="300" height="200">
 
 O clustering hierárquico é uma alternativa ao K-means que pode gerar clusters muito diferentes. O clustering hierárquico permite que o usuário visualize o efeito da especificação de diferentes números de clusters. É mais sensível na descoberta de grupos ou registros anormais ou ruidos. O agrupamento hierárquico também se presta a uma interface gráfica intuitiva exibição, levando a uma interpretação mais fácil dos clusters. 
 O clustering hierárquico é uma alternativa ao K-means que pode gerar clusters muito diferentes. O clustering hierárquico permite que o usuário visualize o efeito da especificação de diferentes números de clusters. É mais sensível na descoberta de grupos ou registros anormais ou ruidos. O agrupamento hierárquico também se presta a uma interface gráfica intuitiva exibição, levando a uma interpretação mais fácil dos clusters. 
 
 **Um Exemplo Simples: **
 
 O clustering hierárquico funciona em um conjunto de dados com n registros e p variáveis e é baseado em dois blocos de construção básicos: 

1. Uma métrica de distância d i, j para medir a distância entre dois registros i e j.
2. Uma métrica dedissimilaridadeD A, B para medir a diferença entre dois clusters A e B com base nas distâncias d i, j entre os membros de cada cluster. 
Para aplicações que envolvem dados numéricos, a escolha mais importante é o dissimilaridade métrica. O clustering hierárquico começa definindo cada registro como seu próprio cluster e itera para combinar os clusters menos diferentes. 

**Termos-chave para clustering hierárquico** 

**Dendrograma** 

Uma representação visual dos registros e da hierarquia dos clusters aos quais pertencem. 

**Distância** 

Uma medida de quão próximo um registro está de outro. 

**Dissimilaridade** 

Uma medida de quão próximo um cluster está de outro. 

*Valeu por ter passado por aqui, bom trabalho ai na aprendizagem.*
