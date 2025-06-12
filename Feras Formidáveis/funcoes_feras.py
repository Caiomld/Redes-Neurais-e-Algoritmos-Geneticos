import random
import itertools
import matplotlib.pyplot as plt


###############################################################################
#                               Caixas binárias                               #
###############################################################################


def gene_cb():
    """Sorteia um valor para uma caixa no problema das caixas binárias"""
    valores_possiveis = [0, 1]
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato_cb(n):
    """Cria uma lista com n valores zero ou um.

    Args:
      n: inteiro que representa o número de caixas.

    """
    candidato = []
    for _ in range(n):
        gene = gene_cb()
        candidato.append(gene)
    return candidato


def populacao_cb(tamanho, n):
    """Cria uma população para o problema das caixas binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_cb(n))
    return populacao


def funcao_objetivo_cb(candidato):
    """Computa a função objetivo no problema das caixas binárias

    Args:
      candidato: uma lista contendo os valores das caixas binárias do problema

    """
    return sum(candidato)


def funcao_objetivo_pop_cb(populacao):
    """Computa a função objetivo para uma população no problema das caixas binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_cb(individuo))
    return fitness


###############################################################################
#                             Caixas não-binárias                             #
###############################################################################


def gene_cnb(valor_max):
    """Sorteia um valor para uma caixa no problema das caixas não-binárias"""
    valores_possiveis = range(valor_max + 1)
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato_cnb(n, valor_max):
    """Cria uma lista com n valores entre zero e valor_max.

    Args:
      n: inteiro que representa o número de caixas.
      valor_max: inteiro represtando o valor máximo das caixas
    """
    candidato = []
    for _ in range(n):
        gene = gene_cnb(valor_max)
        candidato.append(gene)
    return candidato


def populacao_cnb(tamanho, n, valor_max):
    """Cria uma população para o problema das caixas não-binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.
      valor_max: inteiro represtando o valor máximo das caixas

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_cnb(n, valor_max))
    return populacao


def funcao_objetivo_cnb(candidato):
    """Computa a função objetivo no problema das caixas não-binárias

    Args:
      candidato: uma lista contendo os valores das caixas não-binárias do problema

    """
    return sum(candidato)


def funcao_objetivo_pop_cnb(populacao):
    """Computa a função objetivo para uma população no problema das caixas não-binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_cnb(individuo))
    return fitness


###############################################################################
#                                    Senha                                    #
###############################################################################


def gene_senha(letras_possiveis):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    """
    letra = random.choice(letras_possiveis)
    return letra


def cria_candidato_senha(tamanho_senha, letras_possiveis):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    candidato = []

    for _ in range(tamanho_senha):
        candidato.append(gene_senha(letras_possiveis))

    return candidato


def populacao_senha(tamanho_populacao, tamanho_senha, letras_possiveis):
    """Cria população inicial no problema da senha

    Args
      tamanho_populacao: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_senha(tamanho_senha, letras_possiveis))

    return populacao


def funcao_objetivo_senha(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia = 0

    for letra_candidato, letra_senha in zip(candidato, senha_verdadeira):
        num_letra_candidato = ord(letra_candidato)
        num_letra_senha = ord(letra_senha)
        distancia += abs(num_letra_candidato - num_letra_senha)

    return distancia


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return fitness


###############################################################################
#                                   Caixeiro                                  #
###############################################################################


def cria_cidades(n, xy_minimo=0, xy_maximo=300):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: Número de cidades que serão visitadas pelo caixeiro.
      xy_minimo: Valor mínimo possível das coordenadas x e y.
      xy_maximo: Valor máximo possível das coordenadas x e y.

    """
    cidades = {}
    num_digitos = len(str(abs(n)))

    for i in range(n):
        cidades[f"Cidade {i:0>{num_digitos}}"] = (
            random.randint(xy_minimo, xy_maximo),
            random.randint(xy_minimo, xy_maximo),
        )

    return cidades


def plota_cidades(cidades):
    """Plota as cidades do problema do caixeiro viajante

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()


def plota_trajeto(cidades, trajeto):
    """Plota o trajeto do caixeiro

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      trajeto: lista contendo a ordem das cidades que foram viszitadas

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    # plotando os trajetos
    for i in range(len(trajeto) - 1):
        cidade1 = trajeto[i]
        cidade2 = trajeto[i + 1]
        plt.plot(
            [cidades[cidade1][0], cidades[cidade2][0]],
            [cidades[cidade1][1], cidades[cidade2][1]],
            color="red",
        )

    # trajeto de volta à cidade inicial
    cidade1 = trajeto[-1]
    cidade2 = trajeto[0]
    plt.plot(
        [cidades[cidade1][0], cidades[cidade2][0]],
        [cidades[cidade1][1], cidades[cidade2][1]],
        color="red",
    )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()


def dist_euclidiana(coord1, coord2):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      coord1: lista contendo as coordenadas x e y de um ponto.
      coord2: lista contendo as coordenadas x e y do outro ponto.

    """
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]

    distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return distancia


def cria_candidato_caixeiro(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    nomes_cidades = list(cidades.keys())
    caminho = random.sample(nomes_cidades, k=len(nomes_cidades))
    return caminho


def populacao_caixeiro(tamanho_populacao, cidades):
    """Cria uma população no problema do caixeiro viajante

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiro(cidades))

    return populacao


def funcao_objetivo_caixeiro(candidato, cidades):
    """Funcao objetivo de um candidato no problema do caixeiro viajante

    Args:
      candidato: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    distancia = 0

    for pos in range(len(candidato) - 1):
        coord_cidade_partida = cidades[candidato[pos]]
        coord_cidade_chegada = cidades[candidato[pos + 1]]
        distancia += dist_euclidiana(
            coord_cidade_partida, coord_cidade_chegada
        )

    # distância para retornar à cidade inicial
    coord_cidade_final = cidades[candidato[-1]]
    coord_cidade_inicial = cidades[candidato[0]]
    distancia += dist_euclidiana(coord_cidade_final, coord_cidade_inicial)

    return distancia


def funcao_objetivo_pop_caixeiro(populacao, cidades):
    """Funcao objetivo de uma populacao no problema do caixeiro viajante

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_caixeiro(individuo, cidades))

    return fitness


###############################################################################
#                             Problema da mochila                             #
###############################################################################


def calcula_mochila(candidato, itens, ordem_dos_itens):
    peso = 0
    valor = 0
    for pegou_item_ou_nao, nome_item in zip(candidato, ordem_dos_itens):
        if pegou_item_ou_nao == 1:
            peso += itens[nome_item]["peso"]
            valor += itens[nome_item]["valor"]
    return peso, valor


def funcao_objetivo_mochila(candidato, itens, ordem_dos_itens, limite):
    peso, valor = calcula_mochila(candidato, itens, ordem_dos_itens)
    
    if peso <= limite:
        return valor
    else:
        return 0.01
    

def funcao_objetivo_pop_mochila(populacao, itens, ordem_dos_itens, limite):
    fitness = []
    
    for individuo in populacao:
        fitness.append(funcao_objetivo_mochila(individuo, itens, ordem_dos_itens, limite))
        
    return fitness
    
    
###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Realiza seleção da população pela roleta

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo

    """
    selecionados = random.choices(populacao, fitness, k=len(populacao))
    return selecionados


def selecao_torneio_max(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    maximização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        max_fitness = max(fitness_sorteados)
        indice_max_fitness = fitness_sorteados.index(max_fitness)
        individuo_selecionado = sorteados[indice_max_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_simples(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte = random.randint(1, len(mae) - 1)
        filho1 = pai[:corte] + mae[corte:]
        filho2 = mae[:corte] + pai[corte:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ponto_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte1 = random.randint(1, len(mae) - 2)
        corte2 = random.randint(corte1 + 1, len(mae) - 1)
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_uniforme(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        for gene_pai, gene_mae in zip(pai, mae):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ordenado(pai, mae, chance_de_cruzamento):
    """Cruzamento ordenado entre dois individuos

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        tamanho_individuo = len(mae)

        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo - 2)
        corte2 = random.randint(corte1 + 1, tamanho_individuo)

        # filho1
        filho1 = [None] * tamanho_individuo
        filho1[corte1:corte2] = mae[corte1:corte2]
        pai_ = pai[corte2:] + pai[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in pai_:
            if valor not in filho1:
                filho1[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        # filho2
        filho2 = [None] * tamanho_individuo
        filho2[corte1:corte2] = pai[corte1:corte2]
        mae_ = mae[corte2:] + mae[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in mae_:
            if valor not in filho2:
                filho2[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        return filho1, filho2
    else:
        return pai, mae


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_simples(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação simples

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_sorteio = set(valores_possiveis) - set([valor_gene])
            individuo[gene] = random.choice(list(valores_sorteio))


def mutacao_salto(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de salto

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            indice_letra = valores_possiveis.index(valor_gene)
            indice_letra += random.choice([1, -1])
            indice_letra %= len(valores_possiveis)
            individuo[gene] = valores_possiveis[indice_letra]


def mutacao_troca(populacao, chance_de_mutacao):
    """Aplica mutacao de troca em um indivíduo

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1 = random.randint(0, len(individuo) - 1)
            gene2 = random.randint(0, len(individuo) - 1)

            while gene1 == gene2:
                gene1 = random.randint(0, len(individuo) - 1)
                gene2 = random.randint(0, len(individuo) - 1)

            individuo[gene1], individuo[gene2] = (
                individuo[gene2],
                individuo[gene1],
            )


def mutacao_simples_cb(populacao, chance_de_mutacao):
    """Realiza mutação simples no problema das caixas binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            individuo[gene] = 0 if individuo[gene] == 1 else 1


def mutacao_simples_cnb(populacao, chance_de_mutacao, valor_max):
    """Realiza mutação simples no problema das caixas não-binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valor_max: inteiro represtando o valor máximo das caixas

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_possiveis = list(range(valor_max + 1))
            valores_possiveis.remove(valor_gene)
            individuo[gene] = random.choice(valores_possiveis)


def mutacao_sucessiva_cb(populacao, chance_de_mutacao, chance_mutacao_gene):
    """Realiza mutação simples no problema das caixas binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    individuo[gene] = 0 if individuo[gene] == 1 else 1


def mutacao_sucessiva_cnb(
    populacao, chance_de_mutacao, chance_mutacao_gene, valor_max
):
    """Realiza mutação simples no problema das caixas não-binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene
      valor_max: inteiro represtando o valor máximo das caixas

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    valores_possiveis = list(range(valor_max + 1))
                    valor_gene = individuo[gene]
                    valores_possiveis.remove(valor_gene)
                    individuo[gene] = random.choice(valores_possiveis)


##############################################################################################################################################
#                                                             Feras Formidáveis                                                              #
##############################################################################################################################################

###############################################################################
#                                Senha Variável                               #
###############################################################################


def populacao_senha_variavel(tamanho_micro_populacao, tamanho_min,tamanho_max, letras_possiveis):
    """Cria população inicial no problema da senha

    Args
      tamanho_micro_populacao: tamanho da micropopulação, onde micropopulação é uma população de mesmo tamanho.
      tamanho_min: inteiro representando o tamanho mínimo da senha.
      tamanho_min: inteiro representando o tamanho máxima da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []
    for i in range (tamanho_min, tamanho_max+1):
        tamanho_senha = i
        for _ in range(tamanho_micro_populacao):
            populacao.append(cria_candidato_senha(tamanho_senha, letras_possiveis))

    return populacao


def funcao_objetivo_senha_variavel(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia = 0
    candidato_objetivo = candidato.copy()
    senha_verdadeira_objetivo = senha_verdadeira.copy()
    # Preenche a senha verdadeira e o candidato com caracteres nulos para que eles tenham o mesmo tamanho
    if len(candidato_objetivo) < len(senha_verdadeira_objetivo):
        diferenca = len(senha_verdadeira_objetivo) - len(candidato_objetivo)
        for i in range(diferenca):
            candidato_objetivo.append(chr(0))
    elif len(candidato_objetivo) > len(senha_verdadeira_objetivo):
        diferenca = len(candidato_objetivo) - len(senha_verdadeira_objetivo)
        for i in range(diferenca):
            senha_verdadeira_objetivo.append(chr(0))

    for letra_candidato_objetivo, letra_senha in zip(candidato_objetivo, senha_verdadeira_objetivo):
        num_letra_candidato_objetivo = ord(letra_candidato_objetivo)
        num_letra_senha = ord(letra_senha)
        distancia += abs(num_letra_candidato_objetivo - num_letra_senha)

    return distancia


def f_objetivo_pop_senha_variavel(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha_variavel(individuo, senha_verdadeira))

    return fitness


def cruzamento_uniforme_tamanho_variavel(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        if len (pai) == len(mae): # se os pais tem o mesmo tamanho
            for gene_pai, gene_mae in zip(pai, mae):
                if random.choice([True, False]):
                    filho1.append(gene_pai)
                    filho2.append(gene_mae)
                else:
                    filho1.append(gene_mae)
                    filho2.append(gene_pai)

        else: # se os pais tem tamanhos diferentes
            if len(pai) > len(mae): # se o pai é maior que a mãe
                for i in range(len(mae)):
                    if random.choice([True, False]):
                        filho1.append(pai[i])
                        filho2.append(mae[i])
                    else:
                        filho1.append(mae[i])
                        filho2.append(pai[i])

                for i in range(len(mae), len(pai)):
                    if random.choice([True, False]):
                        filho1.append(pai[i])
                    else:
                        filho2.append(pai[i])

            else: # se a mae é maior que o pai
                for i in range(len(pai)):
                    if random.choice([True, False]):
                        filho1.append(pai[i])
                        filho2.append(mae[i])
                    else:
                        filho1.append(mae[i])
                        filho2.append(pai[i])

                for i in range(len(pai), len(mae)):
                    if random.choice([True, False]):
                        filho1.append(mae[i])
                    else:
                        filho2.append(mae[i])

        return filho1, filho2
    
    else:
        return pai, mae


###############################################################################
#                              Palindromos                                    #
###############################################################################


def gene_palindromo(letras_possiveis):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    """
    letra = random.choice(letras_possiveis)
    return letra

def cria_candidato_palindromo(tamanho_palindromo, letras_possiveis):
    """Cria um candidato para o problema da palindromo

    Args:
      tamanho_palindromo: inteiro representando o tamanho da palindromo.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    candidato = []

    for _ in range(tamanho_palindromo):
        candidato.append(gene_palindromo(letras_possiveis))

    return candidato

def populacao_palindromo(tamanho_populacao, tamanho_palindromo, letras_possiveis):
    """Cria população inicial no problema da palindromo

    Args
      tamanho_populacao: tamanho da população.
      tamanho_palindromo: inteiro representando o tamanho da palindromo.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_palindromo(tamanho_palindromo, letras_possiveis))

    return populacao

def funcao_objetivo_palindromo(candidato, lista_vogais):
    """Computa a funcao objetivo de um candidato no problema do palindromo

    Args:
      candidato: um palpite para o palindromo que você quer descobrir
    """
    score = 0

    for i in candidato:
        if i in lista_vogais:
            score += 1
            break

    if candidato[0] == candidato[-1]:
        score += 1
    if candidato[1] == candidato[-2]:  
        score += 1

    return score

def funcao_objetivo_pop_palindromo(populacao, lista_vogais):
    """Computa a funcao objetivo de uma populaçao no problema da palindromo.

    Args:
      populacao: lista contendo os individuos do problema
    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_palindromo(individuo, lista_vogais))

    return fitness


def mutacao_espelhada(populacao, chance_de_mutacao):
    """Realiza mutação espelhada no problema dos palindromos

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            individuo[gene] = individuo[len(individuo) - 1 - gene]

    return populacao


###############################################################################
#                              Caixeiro Ímpares                               #
###############################################################################


def cria_cidades_caixeiro_2(n, xy_minimo=0, xy_maximo=300):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: Número de cidades que serão visitadas pelo caixeiro.
      xy_minimo: Valor mínimo possível das coordenadas x e y.
      xy_maximo: Valor máximo possível das coordenadas x e y.

    """
    cidades = {}
    # num_digitos = len(str(abs(n)))

    for i in range(n):
        cidades[f"Cidade {i}"] = (
            random.randint(xy_minimo, xy_maximo),
            random.randint(xy_minimo, xy_maximo),
        )

    return cidades

def cria_candidato_caixeiro_2(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    nomes_cidades = list(cidades.keys())
    cidades_impares = []
    cidades_pares = []

    ordem = [nomes_cidades[0]]
    for i in range(1,len(nomes_cidades)):
        if i % 2 == 0:
            cidades_pares.append(nomes_cidades[i])
        else:
            cidades_impares.append(nomes_cidades[i])

    random.shuffle(cidades_impares)
    random.shuffle(cidades_pares)

    ordem += cidades_impares + cidades_pares
    
    return ordem

def populacao_caixeiro_2(tamanho_populacao, cidades):
    """Cria uma população no problema do caixeiro viajante

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiro_2(cidades))

    return populacao

def ordenacao_impares_pares(individuo):
    """Ordena os genes do individuo em impares e pares"""
    cidade_0 = individuo[0]
    resto = individuo[1:]
    def extrair_num(cidade):
        return int(cidade.replace("Cidade ", ""))
    cidades_impares = []
    cidades_pares = []
    for i in resto:
        if extrair_num(i) % 2 == 0:
            cidades_pares.append(i)
        else:
            cidades_impares.append(i)
    cidade_ordenada = [cidade_0] + cidades_impares + cidades_pares
    return cidade_ordenada

def cruzamento_ordenado_caixeiro_impares(pai, mae, chance_de_cruzamento):
    """Cruzamento ordenado entre dois individuos

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        pai_sem_zero = pai[1:]
        mae_sem_zero = mae[1:]

        tamanho_individuo_sem_zero = len(mae_sem_zero)

        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo_sem_zero - 2)
        corte2 = random.randint(corte1 + 1, tamanho_individuo_sem_zero)

        # filho1
        filho1_sem_zero = [None] * tamanho_individuo_sem_zero
        filho1_sem_zero[corte1:corte2] = mae_sem_zero[corte1:corte2]
        pai_ = pai_sem_zero[corte2:] + pai_sem_zero[:corte2]
        posicao = corte2 % tamanho_individuo_sem_zero
        for valor in pai_:
            if valor not in filho1_sem_zero:
                filho1_sem_zero[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo_sem_zero

        # filho2
        filho2_sem_zero = [None] * tamanho_individuo_sem_zero
        filho2_sem_zero[corte1:corte2] = pai_sem_zero[corte1:corte2]
        mae_ = mae_sem_zero[corte2:] + mae_sem_zero[:corte2]
        posicao = corte2 % tamanho_individuo_sem_zero
        for valor in mae_:
            if valor not in filho2_sem_zero:
                filho2_sem_zero[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo_sem_zero

        filho1 = [pai[0]] + filho1_sem_zero
        filho2 = [mae[0]] + filho2_sem_zero

        # ordena os filhos
        filho1 = ordenacao_impares_pares(filho1)
        filho2 = ordenacao_impares_pares(filho2)

        return filho1, filho2
    else:
        return pai, mae
    
def mutacao_caixeiro_impares(populacao, chance_de_mutacao):
    """Realiza mutação simples

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1 = random.randint(1, len(individuo) - 1)
            gene2 = random.randint(1, len(individuo) - 1)

            while gene1 == gene2:
                gene1 = random.randint(1, len(individuo) - 1)
                gene2 = random.randint(1, len(individuo) - 1)

            individuo[gene1], individuo[gene2] = individuo[gene2], individuo[gene1]

            individuo[:] = ordenacao_impares_pares(individuo)


###############################################################################
#                              Caixeiros Viajantes                            #
###############################################################################


def cria_candidato_caixeiros(cidades, n_caixeiros):
    """Sorteia um caminho possível no problema dos caixeiros viajantes

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      n_caixeiros: número de caixeiros que irão visitar as cidades.

    """
    nomes_cidades = list(cidades.keys())

    tamanho_base = len(cidades) // n_caixeiros
    resto = len(cidades) % n_caixeiros

    rotas = []
    inicio = 0

    for i in range(n_caixeiros):
        if i < resto:
            fim = inicio + tamanho_base + 1
        else:
            fim = inicio + tamanho_base
        rota = nomes_cidades[inicio:fim]
        rota = random.sample(rota, k=len(rota))
        rotas.append(rota)
        inicio = fim
    
    caminho_dividido = []
    for i, rota in enumerate(rotas):
        caminho_dividido.extend(rota)
        if i < n_caixeiros - 1:
            caminho_dividido.append('|')

    return caminho_dividido


def calcular_distancia_rota(rota, cidades):
    """Calcula a distância total de uma rota de um caixeiro.

    Args:
        rota: lista com os índices das cidades (ex: [2, 5, 0])
        cidades: dicionário com coordenadas (ex: {0: (x0, y0), 1: (x1, y1), ...})

    """
    distancia = 0
    for i in range(len(rota) - 1):
        cidade_1 = cidades[rota[i]]
        cidade_2 = cidades[rota[i + 1]]
        distancia += dist_euclidiana(cidade_1, cidade_2)
    return distancia



def populacao_caixeiros(tamanho_populacao, cidades, n_caixeiros):
    """Cria uma população no problema dos caixeiros viajantes

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiros(cidades, n_caixeiros))

    return populacao


def funcao_objetivo_caixeiros(candidato, cidades):
    """Funcao objetivo de um candidato no problema dos caixeiros viajantes

    Args:
      candidato: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    distancia = 0
    rota = []

    for gene in candidato:
        if gene == '|':
            distancia += calcular_distancia_rota(rota, cidades)
            rota = []
        else:
            rota.append(gene)

    distancia += calcular_distancia_rota(rota, cidades)

    return distancia


def funcao_objetivo_pop_caixeiros(populacao, cidades):
    """Funcao objetivo de uma populacao no problema do caixeiro viajante

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_caixeiros(individuo, cidades))

    return fitness

def cruzamento_ordenado_caixeiros(pai, mae, chance_de_cruzamento):
    """
    Realiza o cruzamento ordenado no problema dos caixeiros viajantes.
    Args:
        pai: lista representando um indivíduo (caminho percorrido).
        mae: lista representando um indivíduo (caminho percorrido).
        chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento.
    """
    # Se o cruzamento não ocorrer, os filhos são cópias dos pais
    if random.random() > chance_de_cruzamento:
        return pai[:], mae[:]

    indices_divisores = [i for i, gene in enumerate(pai) if gene == '|']
    pai_cidades = [gene for gene in pai if gene != '|']
    mae_cidades = [gene for gene in mae if gene != '|']
    tamanho = len(pai_cidades)
    inicio, fim = sorted(random.sample(range(tamanho), 2))
    
    ### Filho 1
    meio_pai = pai_cidades[inicio:fim]
    resto_mae = [item for item in mae_cidades if item not in meio_pai]
    filho1_cidades = resto_mae[:inicio] + meio_pai + resto_mae[inicio:]
    ### Filho 2
    meio_mae = mae_cidades[inicio:fim]
    resto_pai = [item for item in pai_cidades if item not in meio_mae]
    filho2_cidades = resto_pai[:inicio] + meio_mae + resto_pai[inicio:]

    filho1_final = filho1_cidades[:]
    filho2_final = filho2_cidades[:]
    
    for indice in sorted(indices_divisores, reverse=True):
        if indice == len(filho1_final) or indice == (len(filho1_final)-1):
            filho1_final.insert(indice-1, '|')
            filho2_final.insert(indice-1, '|')
        elif indice == 0 or indice == 1:
            filho1_final.insert(indice+1, '|')
            filho2_final.insert(indice+1, '|')
        else:
            filho1_final.insert(indice, '|')
            filho2_final.insert(indice, '|')

    return filho1_final, filho2_final


def mutacao_troca_caixeiros(populacao, chance_de_mutacao):
    """Realiza mutação de troca em indivíduos caixeiros viajantes.

    Args:
      populacao: lista contendo os indivíduos do problema (cada um é uma lista de cidades e '|').
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.
    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            rotas = []
            rota_atual = []
            for gene in individuo:
                if gene == '|':
                    rotas.append(rota_atual)
                    rota_atual = []
                else:
                    rota_atual.append(gene)
            rotas.append(rota_atual) # Adiciona a última rota

            rotas_validas_indices = [i for i, r in enumerate(rotas) if len(r) >= 2]
            
            if not rotas_validas_indices: 
                continue

            indice_rota_escolhida = random.choice(rotas_validas_indices)
            rota_para_mutar = rotas[indice_rota_escolhida]
            idx1, idx2 = random.sample(range(len(rota_para_mutar)), 2)
            rota_para_mutar[idx1], rota_para_mutar[idx2] = rota_para_mutar[idx2], rota_para_mutar[idx1]
            novo_individuo = []
            for i, rota in enumerate(rotas):
                novo_individuo.extend(rota)
                if i < len(rotas) - 1:
                    novo_individuo.append('|')
            
            individuo[:] = novo_individuo 

def plota_trajetos_caixeiros(cidades, trajeto):
    """Plota os trajetos de múltiplos caixeiros.

    Nota: código de base criado pelo Google Gemini.

    Args:
    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      trajeto: lista contendo a ordem das cidades que foram visitadas e separadas por "|"
    """

    x_coords = [coord[0] for coord in cidades.values()]
    y_coords = [coord[1] for coord in cidades.values()]
    plt.figure(figsize=(12, 8))
    plt.scatter(x_coords, y_coords, color="blue", zorder=5) # zorder para ficar na frente

    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    rotas = [
        list(grupo)
        for k, grupo in itertools.groupby(trajeto, lambda x: x == "|")
        if not k
    ]

    cores = plt.cm.get_cmap('tab10', len(rotas))

    for i, rota in enumerate(rotas):
        cor = cores(i)
        if len(rota) < 2:
            continue
        for j in range(len(rota) - 1):
            cidade1_nome = rota[j]
            cidade2_nome = rota[j + 1]
            ponto1 = cidades[cidade1_nome]
            ponto2 = cidades[cidade2_nome]
            plt.plot([ponto1[0], ponto2[0]], [ponto1[1], ponto2[1]], color=cor, linewidth=2)

        cidade_final_nome = rota[-1]
        cidade_inicial_nome = rota[0]
        ponto_final = cidades[cidade_final_nome]
        ponto_inicial = cidades[cidade_inicial_nome]
        plt.plot([ponto_final[0], ponto_inicial[0]], [ponto_final[1], ponto_inicial[1]], color=cor, linewidth=2)

    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title("Trajetos dos Caixeiros Viajantes")
    plt.grid()
    plt.legend()
    plt.show()


###############################################################################
#                                Liga Mais Cara                               #
###############################################################################


def cria_candidato_ligas(preco):
  """Cria um candidato para o problema das ligas.

  Args:
    n: inteiro que representa o número de ligas de cada indivíduo.
    valor_max: inteiro represtando o valor máximo das ligas

  """
  candidato = []
  x = random.randint(5, 80)
  y = random.randint(5, (90 - x))
  z = 100 - (x + y)
  candidato.append(x)
  candidato.append(y)
  candidato.append(z)
  candidato.extend(random.sample(list(preco.keys()),k=3))
  return candidato


def populacao_ligas(tamanho, preco):
  """Cria uma população de candidatos para o problema das ligas.

  Args:
    tamanho: inteiro que representa o tamanho da população.
    n: inteiro que representa o número de ligas de cada indivíduo.
    valor_max: inteiro represtando o valor máximo das ligas
  """
  populacao = []
  for _ in range(tamanho):
      populacao.append(cria_candidato_ligas(preco))
  return populacao

def funcao_objetivo_ligas(candidato, preco):
    """Computa a função objetivo no problema das caixas não-binárias

    Args:
      candidato: uma lista contendo os valores das caixas não-binárias do problema

    """
    lista_de_precos = []
    valores = candidato[:-3]
    elementos = candidato[-3:]
    for elemento, valor in zip (elementos, valores):
      lista_de_precos.append(preco[elemento] * valor)
    return sum(lista_de_precos)


def funcao_objetivo_pop_ligas(populacao, preco):
    """Computa a função objetivo para uma população no problema das caixas não-binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_ligas(individuo, preco))
    return fitness

def cruzamentos_uniformes(pai, mae, chance_de_cruzamento, elementos_possiveis):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """

    pai_xyz = pai[:-3]
    mae_xyz = mae[:-3]
    pai_elementos = pai[-3:]
    mae_elementos = mae[-3:]

    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        #cruzamento xyz
        for gene_pai, gene_mae in zip(pai_xyz, mae_xyz):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        #cruzamento elementos
        for gene_pai, gene_mae in zip(pai_elementos, mae_elementos):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        #garantindo que não possam existir elementos iguais em qualquer um dos filhos
        usados = set()
        for i in range(len(filho1[-3:])):
            if filho1[-3:][i] in usados:
                novos = []
                for elemento in elementos_possiveis:
                    if elemento not in filho1[-3:]:
                        novos.append(elemento)
                if novos:
                    filho1[-3:][i] = random.choice(novos)
            usados.add(filho1[-3:][i])

        usados = set()
        for i in range(len(filho2[-3:])):
            if filho2[-3:][i] in usados:
                novos = []
                for elemento in elementos_possiveis:
                    if elemento not in filho2[-3:]:
                        novos.append(elemento)
                if novos:
                    filho2[-3:][i] = random.choice(novos)
            usados.add(filho2[-3:][i])

        return filho1, filho2
    else:
        return pai, mae

def cruzamentos_ponto_simples(pai, mae, chance_de_cruzamento, elementos_possiveis):
    """Realiza cruzamento de ponto simples

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """

    pai_xyz = pai[:-3]
    mae_xyz = mae[:-3]
    pai_elementos = pai[-3:]
    mae_elementos = mae[-3:]

    filho1 = []
    filho2 = []

    if random.random() < chance_de_cruzamento:
      #cruzamento x,y,z
        corte_xyz = random.randint(1, len(mae_xyz) - 1)
        filho1_xyz = pai_xyz[:corte_xyz] + mae_xyz[corte_xyz:]
        filho2_xyz = mae_xyz[:corte_xyz] + pai_xyz[corte_xyz:]
        filho1.extend(filho1_xyz)
        filho2.extend(filho2_xyz)
      #cruzamento elementos
        corte_elementos = random.randint(1, len(mae_elementos) - 1)
        filho1_elementos = pai_elementos[:corte_elementos] + mae_elementos[corte_elementos:]
        filho2_elementos = mae_elementos[:corte_elementos] + pai_elementos[corte_elementos:]
        filho1.extend(filho1_elementos)
        filho2.extend(filho2_elementos)

        #garantindo que não possam existir elementos iguais em qualquer um dos filhos
        usados = set()
        for i in range(len(filho1[-3:])):
            if filho1[-3:][i] in usados:
                novos = []
                for elemento in elementos_possiveis:
                    if elemento not in filho1[-3:]:
                        novos.append(elemento)
                if novos:
                    filho1[-3:][i] = random.choice(novos)
            usados.add(filho1[-3:][i])

        usados = set()
        for i in range(len(filho2[-3:])):
            if filho2[-3:][i] in usados:
                novos = []
                for elemento in elementos_possiveis:
                    if elemento not in filho2[-3:]:
                        novos.append(elemento)
                if novos:
                    filho2[-3:][i] = random.choice(novos)
            usados.add(filho2[-3:][i])

        return filho1, filho2
    else:
        return pai, mae
    
def mutacao_ligas(populacao, chance_de_mutacao, elementos_possiveis, preco):
    """Realiza mutação em uma população.

    Args:
      populacao: lista contendo os individuos da população
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista contendo os valores possíveis para cada gene

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
          #mutamos o elemento por algum outro elemento presente no dicionário
            elementos = individuo[-3:]
            gene_elementos = random.randint(0, len(elementos) - 1)

            novo_elemento = random.choice(elementos_possiveis)
            while novo_elemento in elementos:
                novo_elemento = random.choice(elementos_possiveis)
            elementos[gene_elementos] = novo_elemento

            individuo[-3:] = elementos
            xyz = individuo[:-3]
            gene_xyz = random.randint(0, len(xyz) - 1)
            xyz[gene_xyz] = random.randint(5, 90) #garantimos que o individuo tenha um peso <= 100 e completaremos posteriormente
            individuo[:-3] = xyz

        # REPARAÇÃO DE DANOS
        xyz = individuo[:-3]
        elementos = individuo[-3:]
        precos_elementos = []
        if sum(xyz) > 100:
          #encontrando o elemento mais barato
            for elemento in elementos:
              precos_elementos.append(preco[elemento])
            preco_minimo = min(precos_elementos)
            #achando o indíviduo mais barato
            min_preco_indice = precos_elementos.index(preco_minimo)
            #achando o segundo indíviduo mais barato
            precos_elementos_restantes = precos_elementos.copy()
            del precos_elementos_restantes[min_preco_indice]
            preco_minimo_2 = min(precos_elementos_restantes)
            min_preco_indice_2 = precos_elementos.index(preco_minimo_2)
            #achando o "terceiro mais barato", vulgo mais caro, indivíduo
            max_preco_indice = precos_elementos.index(max(precos_elementos))
            #reduzindo o valor do x, y ou z referente ao elemento mais barato para se enquadrar na regra x + y + z = 100
            soma = sum(xyz)
            valor_retirar = soma - 100
            while valor_retirar > 0:
              if individuo[min_preco_indice] > 5:
                individuo[min_preco_indice] -= 1
                valor_retirar -= 1
              else:
                if individuo[min_preco_indice_2] > 5:
                  individuo[min_preco_indice_2] -= 1
                  valor_retirar -= 1
                else:
                  individuo[max_preco_indice] -= 1
                  valor_retirar -= 1


        elif sum(xyz) < 100:
          #encontrando o elemento mais caro
            for elemento in elementos:
              precos_elementos.append(preco[elemento])
            preco_maximo = max(precos_elementos)
            max_preco_indice = precos_elementos.index(preco_maximo)
          #aumentando o valor do x, y ou z referente ao elemento mais caro para se enquadrar na regra x + y + z = 100
            soma = sum(xyz)
            valor_colocar = 100 - soma
            individuo[max_preco_indice] += valor_colocar

        else: #se o individuo ja for valido, só seguimos
            pass

        #garantindo que não possam existir elementos iguais em qualquer um dos mutados
        usados = set()
        for i in range(3):
            if elementos[i] in usados:
                novos_possiveis = [e for e in elementos_possiveis if e not in elementos]
                if novos_possiveis:
                    elementos[i] = random.choice(novos_possiveis)
            usados.add(elementos[i])

        individuo[-3:] = elementos

    return populacao

###############################################################################
#                              Liga Leve Mais Cara                            #
###############################################################################


def funcao_objetivo_ligas_leves(candidato, preco, peso_atomico):
    """Computa a função objetivo no problema das caixas não-binárias

    Args:
      candidato: uma lista contendo os valores das caixas não-binárias do problema

    """
    lista_de_precos = []
    lista_de_pesos_atomicos = []
    lista_precos_atomicos = []
    valores = candidato[:-3]
    elementos = candidato[-3:]
    for elemento, valor in zip (elementos, valores):
      lista_de_precos.append(preco[elemento] * valor)
    for elemento, valor in zip(elementos, valores):
      lista_de_pesos_atomicos.append(peso_atomico[elemento] * valor)
    for custo, peso in zip(lista_de_precos, lista_de_pesos_atomicos):
      lista_precos_atomicos.append((custo / peso))
    return sum(lista_precos_atomicos)


def funcao_objetivo_pop_ligas_leves(populacao, preco, peso_atomico):
    """Computa a função objetivo para uma população no problema das caixas não-binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_ligas_leves(individuo, preco, peso_atomico))
    return fitness

def mutacao_ligas_leves(populacao, chance_de_mutacao, elementos_possiveis, precos_atomicos):
    """Realiza mutação em uma população.

    Args:
      populacao: lista contendo os individuos da população
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista contendo os valores possíveis para cada gene

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
          #mutamos o elemento por algum outro elemento presente no dicionário
            elementos = individuo[-3:]
            gene_elementos = random.randint(0, len(elementos) - 1)

            novo_elemento = random.choice(elementos_possiveis)
            while novo_elemento in elementos:
                novo_elemento = random.choice(elementos_possiveis)
            elementos[gene_elementos] = novo_elemento

            individuo[-3:] = elementos
            xyz = individuo[:-3]
            gene_xyz = random.randint(0, len(xyz) - 1)
            xyz[gene_xyz] = random.randint(5, 90) #garantimos que o individuo tenha um peso <= 100 e completaremos posteriormente
            individuo[:-3] = xyz

        # REPARAÇÃO DE DANOS
        xyz = individuo[:-3]
        elementos = individuo[-3:]
        precos_atomicos_elementos = []
        if sum(xyz) > 100:
          #encontrando o elemento mais barato
            for elemento in elementos:
              precos_atomicos_elementos.append(precos_atomicos[elemento])
            preco_minimo = min(precos_atomicos_elementos)
            #achando o indíviduo mais barato
            min_preco_indice = precos_atomicos_elementos.index(preco_minimo)
            #achando o segundo indíviduo mais barato
            precos_elementos_restantes = precos_atomicos_elementos.copy()
            del precos_elementos_restantes[min_preco_indice]
            preco_minimo_2 = min(precos_elementos_restantes)
            min_preco_indice_2 = precos_atomicos_elementos.index(preco_minimo_2)
            #achando o "terceiro mais barato", vulgo mais caro, indivíduo
            max_preco_indice = precos_atomicos_elementos.index(max(precos_atomicos_elementos))
            #reduzindo o valor do x, y ou z referente ao elemento mais barato para se enquadrar na regra x + y + z = 100
            soma = sum(xyz)
            valor_retirar = soma - 100
            while valor_retirar > 0:
              if individuo[min_preco_indice] > 5:
                individuo[min_preco_indice] -= 1
                valor_retirar -= 1
              else:
                if individuo[min_preco_indice_2] > 5:
                  individuo[min_preco_indice_2] -= 1
                  valor_retirar -= 1
                else:
                  individuo[max_preco_indice] -= 1
                  valor_retirar -= 1


        elif sum(xyz) < 100:
          #encontrando o elemento mais caro
            for elemento in elementos:
              precos_atomicos_elementos.append(precos_atomicos[elemento])
            preco_maximo = max(precos_atomicos_elementos)
            max_preco_indice = precos_atomicos_elementos.index(preco_maximo)
          #aumentando o valor do x, y ou z referente ao elemento mais caro para se enquadrar na regra x + y + z = 100
            soma = sum(xyz)
            valor_colocar = 100 - soma
            individuo[max_preco_indice] += valor_colocar

        else: #se o individuo ja for valido, só seguimos
            pass

        #garantindo que não possam existir elementos iguais em qualquer um dos mutados
        usados = set()
        for i in range(3):
            if elementos[i] in usados:
                novos_possiveis = [e for e in elementos_possiveis if e not in elementos]
                if novos_possiveis:
                    elementos[i] = random.choice(novos_possiveis)
            usados.add(elementos[i])

        individuo[-3:] = elementos

    return populacao