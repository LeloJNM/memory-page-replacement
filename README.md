# memory-page-replacement
Simulador de Algoritmos de Substituição de Páginas em Memória Virtual
Este projeto implementa um simulador para comparar o desempenho de três algoritmos clássicos de gerenciamento de memória: Ótimo (OPT/OTM), FIFO (First-In First-Out) e LRU (Least Recently Used). O simulador calcula a quantidade de page faults ocorridos com base em uma sequência de referências a páginas, permitindo assim a comparação entre as estratégias de substituição.

Funcionalidades
FIFO: Utiliza uma fila para manter a ordem de chegada das páginas. Quando ocorre uma falta de página e a memória está cheia, a página mais antiga é removida.

LRU: Mantém uma lista ordenada segundo o uso recente das páginas. A cada acesso, uma página é atualizada para refletir o seu uso mais recente; quando necessário, a página menos recentemente utilizada é substituída.

OTM (Ótimo/Optimal): Analisa as referências futuras para tomar a decisão ideal de substituição, removendo a página que será utilizada no maior intervalo de tempo ou que não será utilizada novamente.

Estrutura do Projeto
O projeto é desenvolvido em Python e é composto pelos seguintes arquivos principais:

main.py: Contém a implementação dos algoritmos (FIFO, LRU e OTM), funções de leitura do arquivo e a função principal que executa a simulação.

README.md: Este arquivo, que documenta o projeto, descrevendo sua finalidade, instruções de uso e detalhes técnicos.

Como Funciona
Entrada:
O simulador lê um arquivo contendo números inteiros.

A primeira linha representa a quantidade de quadros de memória RAM disponíveis.

As linhas subsequentes contêm a sequência de referências a páginas.

Exemplo de arquivo de entrada:

4
1
2
3
4
1
2
5
1
2
3
4
5
Processamento:
Cada algoritmo processa a sequência de referências e conta a quantidade de page faults que ocorrem conforme as suas respectivas estratégias de substituição.

Saída:
O simulador imprime a quantidade de page faults para cada algoritmo no seguinte formato:

nginx
FIFO 10
OTM 6
LRU 8
Requisitos
Python 3.x

Instruções de Uso
Clone o repositório ou baixe os arquivos do projeto.

Prepare o arquivo de entrada:
Crie um arquivo de texto com os números de entrada conforme o exemplo acima. Por exemplo, entrada.txt.

Execute o simulador:
Abra o terminal, navegue até a pasta do projeto e execute:

bash
python main.py
Em seguida, informe o caminho do arquivo de entrada quando solicitado.

Casos de Teste
Você pode testar o simulador utilizando diferentes arquivos de entrada. Alguns casos de teste sugeridos:

Caso Básico:
Arquivo com 4 quadros e sequência conforme o exemplo:


4
1
2
3
4
1
2
5
1
2
3
4
5
Saída esperada:

nginx
FIFO 10
OTM 6
LRU 8
Memória Suficiente:
Arquivo onde a quantidade de quadros é igual ou maior que o número de páginas únicas:

5
1
2
3
4
5
1
2
3
4
5
Saída esperada:

nginx
FIFO 5
OTM 5
LRU 5
Capacidade Reduzida (1 Quadro):
Arquivo para testar o comportamento com apenas um quadro:

1
3
3
2
1
3
2
Saída esperada:

nginx
FIFO 5
OTM 5
LRU 5
Outros casos de teste podem ser criados para simular sequências alternadas, padrões crescentes/decrescentes, entre outros.