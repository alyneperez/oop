class Jogador:

    def __init__(self,nome):
        self.nome = nome
        self.gols = 0

    def marcar_gols(self):
        self.gols +=  1

    def get_gols(self):
        return self.gols

    def __str__(self):
        pass
