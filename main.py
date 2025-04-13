def fifo(num_frames, references):
    """Implementa o algoritmo FIFO (First-In, First-Out)."""
    frames = []           # Inicializa a lista de quadros (representa a memória)
    faults = 0            # Variável para contar as faltas de página
    for page in references:  # Percorre cada página referenciada na lista
        # Se a página não está presente nos quadros, ocorre uma falta de página
        if page not in frames:
            faults += 1  # Incrementa o contador de faltas
            # Se ainda há espaço nos quadros (número de quadros usados é menor que o máximo permitido)
            if len(frames) < num_frames:
                frames.append(page)  # Adiciona a página no final da lista
            else:
                # Se não há espaço, remove a página que entrou primeiro (posição 0 da lista, FIFO)
                frames.pop(0)
                # Adiciona a nova página ao final da lista
                frames.append(page)
    return faults  # Retorna o total de faltas de página ocorridas

def lru(num_frames, references):
    """Implementa o algoritmo LRU (Least Recently Used)."""
    frames = []           # Inicializa a lista dos quadros
    faults = 0            # Inicializa o contador de faltas de página
    for page in references:  # Percorre cada página referenciada
        # Se a página já está na memória
        if page in frames:
            # Remove a página da posição atual
            frames.remove(page)
            # Reinsere a página no final para atualizar seu uso recente
            frames.append(page)
        else:
            # Caso a página não esteja na memória, conta falta de página
            faults += 1
            # Se houver espaço disponível (menos páginas que o número máximo de quadros)
            if len(frames) < num_frames:
                frames.append(page)  # Adiciona a página no final
            else:
                # Se a memória está cheia, remove a página menos recentemente usada (a primeira da lista)
                frames.pop(0)
                # Insere a nova página no final, pois ela acaba de ser usada
                frames.append(page)
    return faults  # Retorna o total de faltas para o algoritmo LRU

def optimal(num_frames, references):
    """Implementa o algoritmo OTM (Optimal Page Replacement)."""
    frames = []           # Inicializa a lista de quadros na memória
    faults = 0            # Contador de faltas de página
    n = len(references)   # Número total de referências para facilitar o laço
    
    # Percorre cada referência com seu índice
    for i, page in enumerate(references):
        # Se a página já estiver em memória, não faz nada
        if page in frames:
            continue
        faults += 1  # Caso contrário, ocorre uma falta de página
        
        # Se ainda existe espaço na memória, apenas adiciona a página
        if len(frames) < num_frames:
            frames.append(page)
        else:
            # Lista que armazenará, para cada página no frame, o índice da sua próxima ocorrência
            next_uses = []
            # Para cada página que está atualmente em memória
            for f in frames:
                try:
                    # Tenta encontrar a próxima referência para a página "f" a partir do índice atual + 1
                    next_use = references.index(f, i + 1)
                except ValueError:
                    # Se a página não for referenciada novamente, define seu próximo uso como infinito,
                    # para dar prioridade à sua substituição
                    next_use = float('inf')
                # Adiciona o índice da próxima ocorrência (ou infinito) à lista
                next_uses.append(next_use)
            # Identifica o índice da página com o maior valor em next_uses,
            # ou seja, que será usada mais tarde ou nunca
            idx_to_remove = next_uses.index(max(next_uses))
            # Substitui a página identificada pela nova página
            frames[idx_to_remove] = page
    return faults  # Retorna o número total de faltas de página para o algoritmo OTM

def ler_arquivo(caminho_arquivo):
    """
    Lê o arquivo do caminho fornecido e retorna:
    - num_frames: número de quadros de memória (primeiro número do arquivo)
    - references: lista das referências de página (demais números do arquivo)
    """
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()  # Lê todas as linhas do arquivo
    # Remove espaços e quebras de linha e converte cada linha em inteiro
    valores = [int(linha.strip()) for linha in linhas if linha.strip() != '']
    if not valores:
        # Se o arquivo estiver vazio ou sem números válidos, gera um erro
        raise ValueError("O arquivo está vazio ou não possui números válidos.")
    num_frames = valores[0]    # O primeiro número indica o número de quadros disponíveis
    references = valores[1:]   # Os demais números representam as referências de páginas
    return num_frames, references  # Retorna os valores lidos

def main():
    # Solicita que o usuário digite o caminho do arquivo que contém os números de entrada
    caminho = input("Digite o caminho do arquivo de entrada: ").strip()
    try:
        # Tenta ler o arquivo e extrair os dados
        num_frames, references = ler_arquivo(caminho)
    except Exception as e:
        # Em caso de erro (por exemplo, arquivo não encontrado ou dados inválidos), exibe a mensagem de erro
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    # Calcula o número de faltas de página para cada algoritmo de substituição
    faltas_fifo = fifo(num_frames, references)
    faltas_otm = optimal(num_frames, references)
    faltas_lru = lru(num_frames, references)
    
    # Exibe os resultados no formato exigido:
    # Nome do algoritmo seguido pelo número de faltas de página
    print(f"FIFO {faltas_fifo}")
    print(f"OTM {faltas_otm}")
    print(f"LRU {faltas_lru}")

# Verifica se o script está sendo executado como programa principal
if __name__ == "__main__":
    main()
