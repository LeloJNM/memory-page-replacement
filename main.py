def fifo(num_frames, references):
    """
    Implementa o algoritmo FIFO (First-In, First-Out).

    Parâmetros:
    - num_frames: número máximo de quadros disponíveis.
    - references: lista de referências de páginas.

    Procedimento:
    - Inicia com uma lista vazia representando os quadros da memória.
    - Para cada referência, se a página não estiver presente nos quadros,
      conta como falta de página.
    - Se houver espaço, adiciona a página; caso contrário, remove a página mais antiga (FIFO)
      e insere a nova página.
    
    Retorna:
    - O total de faltas de página.
    """
    frames = []  # Lista que representa os quadros de memória
    faults = 0   # Contador de faltas de página
    for page in references:
        # Se a página não está nos quadros, temos uma falta de página
        if page not in frames:
            faults += 1
            # Se ainda há espaço disponível, adiciona a página
            if len(frames) < num_frames:
                frames.append(page)
            else:
                # Se não há espaço, remove a página que entrou primeiro (posição 0 da lista) e insere a nova
                frames.pop(0)
                frames.append(page)
    return faults

def lru(num_frames, references):
    """
    Implementa o algoritmo LRU (Least Recently Used).

    Parâmetros:
    - num_frames: número de quadros disponíveis.
    - references: lista de referências de páginas.

    Procedimento:
    - Inicia com uma lista vazia para os quadros de memória.
    - Ao acessar uma página:
       - Se já está na memória, ela é removida e reinserida no final para indicar que foi recentemente usada.
       - Se não estiver, conta como falta de página e insere-a.
         Se a memória estiver cheia, remove a página que está há mais tempo sem uso (a primeira da lista).
    
    Retorna:
    - O total de faltas de página.
    """
    frames = []  # Lista representando os quadros de memória
    faults = 0   # Contador de faltas de página
    for page in references:
        if page in frames:
            # Atualiza a página para o fim da lista para indicar uso recente
            frames.remove(page) ##TIRA DA POSIÇÃO ATUAL DA FILA
            frames.append(page) ##ADICIONA NO FINAL DA FILA(MAIS RECENTE
        else:
            faults += 1  # Conta falta de página
            # Se houver espaço, insere a página diretamente
            if len(frames) < num_frames:
                frames.append(page)
            else:
                # Remove a página menos recentemente usada (primeira posição da lista)
                frames.pop(0)
                frames.append(page)
    return faults

def optimal(num_frames, references):
    """
    Implementa o algoritmo OTM (Optimal Page Replacement).

    Parâmetros:
    - num_frames: número de quadros disponíveis.
    - references: lista de referências de páginas.

    Procedimento:
    - Para cada página referenciada:
       - Se já estiver na memória, não ocorre falta.
       - Se não estiver, ocorre falta de página.
       - Se houver espaço, insere a página; caso contrário, para cada página atualmente na memória,
         busca-se o índice da próxima ocorrência. Se uma página não for referenciada novamente,
         seu próximo uso é definido como infinito.
       - Substitui a página que será usada mais tarde (ou nunca), ou seja, aquela com o maior índice de próxima ocorrência.
    
    Retorna:
    - O total de faltas de página.
    """
    frames = []  # Lista representando os quadros de memória
    faults = 0   # Contador de faltas de página
    n = len(references)
    
    for i, page in enumerate(references):
        if page in frames:
            # A página já está na memória, nenhum processamento adicional é necessário
            continue
        faults += 1  # Faltou a página
        
        if len(frames) < num_frames:
            # Se houver espaço, insere a página sem substituição
            frames.append(page)
        else:
            next_uses = []
            # Para cada página nos quadros, encontra o índice da próxima ocorrência
            for f in frames:
                try:
                    next_use = references.index(f, i + 1)
                except ValueError:
                    # Se a página não for encontrada novamente, define como infinito
                    next_use = float('inf')
                next_uses.append(next_use)
            # Identifica a página com a maior distância para o próximo uso
            idx_to_remove = next_uses.index(max(next_uses))
            # Substitui a página com a nova referência
            frames[idx_to_remove] = page
    return faults

def ler_arquivo(caminho_arquivo):
    """
    Lê um arquivo e extrai os números inteiros para:
    - num_frames: o número de quadros de memória (primeiro número).
    - references: a lista de referências de páginas (demais números).

    Parâmetros:
    - caminho_arquivo: caminho do arquivo de entrada.
    
    Retorna:
    - Uma tupla (num_frames, references)

    Caso o arquivo esteja vazio ou não contenha números válidos, é gerada uma exceção.
    """
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
    # Converte cada linha em um inteiro, ignorando linhas vazias
    valores = [int(linha.strip()) for linha in linhas if linha.strip() != '']
    if not valores:
        raise ValueError("O arquivo está vazio ou não possui números válidos.")
    num_frames = valores[0]    # Primeiro número: quantidade de quadros
    references = valores[1:]   # Demais números: referências de páginas
    return num_frames, references

def main():
    """
    Função principal que executa o programa.
    
    Procedimento:
    1. Solicita ao usuário o caminho do arquivo de entrada.
    2. Lê e processa os dados do arquivo.
    3. Calcula as faltas de página para cada algoritmo de substituição.
    4. Exibe os resultados no formato exigido: ALGORITMO N.
    """
    caminho = input("Digite o caminho do arquivo de entrada: ").strip()
    try:
        num_frames, references = ler_arquivo(caminho)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    # Calcula as faltas de página para cada algoritmo
    faltas_fifo = fifo(num_frames, references)
    faltas_otm = optimal(num_frames, references)
    faltas_lru = lru(num_frames, references)
    
    # Exibe os resultados conforme o formato solicitado:
    print(f"FIFO {faltas_fifo}")
    print(f"OTM {faltas_otm}")
    print(f"LRU {faltas_lru}")

if __name__ == "__main__":
    main()
