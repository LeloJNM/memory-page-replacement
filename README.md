# memory-page-replacement

**Simulador de Algoritmos de Substituição de Páginas em Memória Virtual**

Este projeto implementa três algoritmos clássicos de gerenciamento de memória:

- **Ótimo (OTM)**  
- **FIFO (First-In First-Out)**  
- **LRU (Least Recently Used)**  

A simulação permite comparar o desempenho de cada algoritmo com base na quantidade de *page faults* gerados a partir de uma sequência de referências de páginas.

---

## Descrição da Entrada:

A entrada é composta por uma série de números inteiros, um por linha.  

- O **primeiro número** representa a **quantidade de quadros disponíveis na memória RAM**.  
- Os **demais números** formam a **sequência de referências à memória**.

---

## Descrição da Saída:

A saída é composta por **três linhas**, cada uma contendo:  

- A **sigla de um dos algoritmos** (`FIFO`, `OTM`, `LRU`)  
- E a **quantidade de faltas de página** que ocorreram durante a simulação com aquele algoritmo.

---

## Exemplo

**Entrada:**
- Quantidade de quadros: 4  
- Sequência de referências: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5  

**Saída esperada:**
- FIFO 10  
- OTM 6  
- LRU 8

---

## Requisitos

- Python 3.x

---

## Instruções de Uso

1. **Clone o repositório ou baixe os arquivos do projeto.**

2. **Prepare o arquivo de entrada:**  
   Crie um arquivo de texto (`.txt`) com os números de entrada, um por linha, conforme o exemplo acima.

3. **Execute o simulador:**  
   No terminal, navegue até a pasta do projeto e execute:

   ```bash
   python main.py
   ```

   Quando solicitado, informe o caminho para o arquivo de entrada.

---

## Casos de Teste Sugeridos

### Caso Básico:
- 4 quadros
- Referências: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5  
- Saída esperada: FIFO 10 | OTM 6 | LRU 8

### Memória Suficiente:
- 5 quadros
- Referências: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5  
- Saída esperada: FIFO 5 | OTM 5 | LRU 5

### Capacidade Reduzida (1 Quadro):
- 1 quadro
- Referências: 3, 3, 2, 1, 3, 2  
- Saída esperada: FIFO 5 | OTM 5 | LRU 5

---
