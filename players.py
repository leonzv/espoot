import json


class Jogador:
    def __init__(self, nome, nacionalidade, idade, inteligencia, paciencia, mecanica, confianca, lane, funcao):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.inteligencia = inteligencia
        self.paciencia = paciencia
        self.mecanica = mecanica
        self.confianca = confianca
        self.lane = lane
        self.funcao = funcao

class Coach:
    def __init__(self, nome, nacionalidade, idade, inteligencia, paciencia):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.inteligencia = inteligencia
        self.paciencia = paciencia

class TimeBase:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores
        




# Carrega o arquivo JSON em um dicionário
with open('players.json', 'r') as f:
    cblol = json.load(f)

# Itera pelos times
for time in cblol['times']:
    # Armazena os dados do time
    nome_time = time['nome']
    cidade = time['cidade']
    jogadores = time['jogadores']

    # Imprime os dados do time
    print(f'Time: {nome_time}')
    print(f'Cidade: {cidade}')
    print('Jogadores:')
    for jogador in jogadores:
        print(f' - {jogador["nome"]} ({jogador["nacionalidade"]}, {jogador["posicao"]})')
    print()  # Adiciona uma linha em branco entre os times