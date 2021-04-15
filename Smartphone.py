class Smartphone:

    def __init__(self, memoria, armazenamento, polegadas):
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.polegadas = polegadas

    def enviar_mensagem(self):
        return "Ooooi..."


    def instalar_app(self):
        return "App instalado com sucesso"

    def __str__(self):
        print(f"Memória: {self.memoria} \n"
              f"Armazenamento: {self.armazenamento} \n"
              f"Polegadas: {self.polegadas} \n ")
              