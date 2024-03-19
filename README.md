# Problema do Caixeiro Viajante

## Descrição
Esse projeto se trata de um trabalho para a disciplina de Teoria dos Grafos na Universidade Federal de Alagoas (UFAL), Campus Arapiraca. Ele se trata do Problema do Caixeiro Viajante, cujo objetivo principal é descobrir o caminho mais curto que visita cada cidade exatamente uma vez, retornando à cidade de origem. A abordagem adotada utiliza a Teoria dos Grafos, onde as cidades são representadas por vértices e as conexões entre elas são expressas por arestas.

Serão utilizadas cinco base de dados (ATT48, DANTZIG42, FRI26, GR17 e P01) para a resolução desse problema, disponíveis através do [link](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html).

Os dados utilizados dos datasets estão em um formato de matriz de adjacência (arquivos .d.txt), que correspondem às distâncias intermunicipais. Isso tornou possível simplesmente armazená-los em uma matriz. Isso porque, ela proporciona uma manipulação mais eficiente do grafo, facilitando as operações necessárias para abordar o PCV.

Posteriormente serão implementados algoritmos para encontrar os caminhos mínimos para cada uma da base de dados.

## Instalação

Antes de utilizar o projeto, é necessário baixar os arquivos para o seu computador. Assim, isso pode ser feito de 2 maneiras:

-> <b>Pelo próprio GitHub</b>

Você vai clicar no botão verde <b><>Code</b> e ao fazer isso aparecerá as seguintes informações:

<img src="./images/image1.png">

Ao clicar em Download ZIP, você terá os arquivos no formato zip em seu computador. Dessa forma, basta fazer a extração da pasta e terá o projeto completo na sua máquina.

-> <b>Terminal</b>

Outra forma bastante rápida de obter os arquivos do projeto, através de um simples comando:

```
$ git clone https://github.com/evellyn489/Caixeiro-Viajante.git
```
Isso tanto para sistemas Windows como para sistemas Linux.

Assim, feito esse passo faleremos em seguida como utilizar o projeto.

<b>Obs</b>: essa parte será mostrada no VsCode, além disso, é necessário ter o <a href="https://www.python.org/" target="_blank">Python</a> instalado na máquina para poder executar o código baixado.

## Como usar

Caso você já tenha o Python instalado, basta escolher qual algoritmo você quer executar, dentro do arquivo, edite a variável "filename" com o caminho do dataset que deseja utilizar, o repositório disponibiliza um conjunto de datasets extraídos do TSPLIB. Todos os datasets estão em formato .txt como uma matriz de adjacência.

## Resultados obtidos

<ul>
    <li>Algoritmo de Dijkstra:</li>
</ul>
<table>
    <thead>
        <tr>
            <th>Base de dados</th>
            <th>Resultado do custo mínimo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ATT48</td>
            <td>40551</td>
        </tr>
        <tr>
            <td>DANTZIG42</td>
            <td>956</td>
        </tr>
        <tr>
            <td>FRI26</td>
            <td>1112</td>
        </tr>
        <tr>
            <td>GR17</td>
            <td>2187</td>
        </tr> 
        <tr>
            <td>P01</td>
            <td>291</td>
        </tr> 
    </tbody>
</table>

<ul>
    <li>Algoritmo de Christofides:</li>
</ul>
<table>
    <thead>
        <tr>
            <th>Base de dados</th>
            <th>Resultado do custo mínimo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ATT48</td>
            <td>37362</td>
        </tr>
        <tr>
            <td>DANTZIG42</td>
            <td>562</td>
        </tr>
        <tr>
            <td>FRI26</td>
            <td>963</td>
        </tr>
        <tr>
            <td>GR17</td>
            <td>2333</td>
        </tr> 
        <tr>
            <td>P01</td>
            <td>281</td>
        </tr> 
    </tbody>
</table>

<ul>
    <li>Algoritmo de Kruskal:</li>
</ul>

<table>
    <thead>
        <tr>
            <th>Base de dados</th>
            <th>Resultado do custo mínimo</th>
            <th>Árvore Geradora Mínima</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ATT48</td>
            <td>27670</td>
            <td> <img src='./images/att48.png'> </td>
        </tr>
        <tr>
            <td>DANTZIG42</td>
            <td>591</td>
            <td> <img src='./images/dantzig42.png'> </td>
        </tr>
        <tr>
            <td>FRI26</td>
            <td>741</td>
            <td> <img src='./images/fri26.png'> </td>
        </tr>
        <tr>
            <td>GR17</td>
            <td>1421</td>
            <td> <img src='./images/gr17.png'> </td>
        </tr> 
        <tr>
            <td>P01</td>
            <td>260</td>
            <td> <img src='./images/p01.png'> </td>
        </tr> 
    </tbody>
</table>

<ul>
    <li>Força Bruta:</li>
</ul>

Nenhuma das bases de dados resultaram numa resposta dentro do tempo máximo de execução de 12h

<table>
    <thead>
        <tr>
            <th>Base de dados</th>
            <th>Qtd de iterações</th>
            <th>Qtd de possibilidades</th>
            <th>Tempo de execução</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ATT48</td>
            <td>31477230000</td>
            <td> 1,241391559×10⁶¹ </td>
            <td>12h</td>
        </tr>
        <tr>
            <td>DANTZIG42</td>
            <td>30753210000</td>
            <td>1,405006118×10⁵¹</td>
            <td> 12h </td>
        </tr>
        <tr>
            <td>FRI26</td>
            <td>25437780000</td>
            <td>4,032914611×10²⁶</td>
            <td> 12h </td>
        </tr>
        <tr>
            <td>GR17</td>
            <td>14461740000</td>
            <td>3,556874281×10¹⁴</td>
            <td>12h</td>
        </tr> 
        <tr>
            <td>P01</td>
            <td>1251440000</td>
            <td>1,307674368×10¹²</td>
            <td>12h</td>
        </tr> 
    </tbody>
</table>


## Licença
A licença do projeto é MIT (Massachusetts Institute of Technology) , o que significa que os usuários têm a liberdade de usar, modificar e distribuir o código-fonte conforme suas necessidades. 

## Contato dos desenvolvedores

- Evellyn Rodrigues: evellyn.rocha@arapiraca.ufal.br
- Kauã Fellipe: kaua.bispo@arapiraca.ufal.br
- Lara Fernanda: lara.cavalcante@arapiraca.ufal.br
- Mayara Bispo: mayara.bispo@arapiraca.ufal.br

## Hardware sugerido
Por enquanto, não há uma sugestão específica de hardware, tendo em vista que os dados foram apenas armazenados. Para a aplicação do projeto, até o momento, foram utilizados 3 tipos de hardware:

- Processador Intel Core i5 - 1135G7, 8GB de RAM, SSD de 256 GB e sistema operacional Windows 11;
- Processador 2.300GHz Intel Core i3, 4GB de RAM, HD de 1 TB e sistema operacional Ubuntu;
- Processador AMD Ryzen 5 5600G, 16GB de RAM, SSD de 500GB, Debian GNU/Linux 12 (bookworm).
- Processador AMD Ryzen 5 5500U, 8GB de RAM, Linux

## Software necessário

Todo o projeto está rodando em sistemas Linux e Windows.
