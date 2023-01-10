class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def contratar_jogador(self, jogador):
        self.jogadores.append(jogador)
        

