class ArCondicionado:

    def __init__(self):
        self.temperatura = 25
        self.ligado      = False

    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            print("Ar condicionado ligado")
        else:
            print("ERRO: O ar já se encontra ligado!")

    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            print("Ar condicionado desligado")
        else:
            print("ERRO: O ar já está desligado!")

    def aumentar_temp(self):
        if self.temperatura < 27:
            self.temperatura += 1
            print(f"Temperatura = {self.temperatura}")
        else:
            print("ERRO: Ar condicionado já está em sua temperatura máxima.")

    def diminunir_temp(self):
        if self.temperatura > 16:
            self.temperatura -= 1
            print(f"Temperatura = {self.temperatura}")
        else:
            print("ERRO: Ar condicionado já está em sua temperatura mínima.")
            