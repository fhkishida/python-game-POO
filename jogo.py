import random

class Personagem():
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"

    def atacar(self, alvo):
        dano = random.randint(self.__nivel * 1, self.__nivel * 5)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} a vida")
        alvo.receber_ataque(dano)

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            print(f"\nO {self.__nome} Foi de base, press F to respect\n")

class Heroi(Personagem): 
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        dano = self.get_nivel() * 4
        print(f"\n{self.get_nome()} usou habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} a vida")
        alvo.receber_ataque(dano)

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi("Marcos Marquinhos", 40, 5, "Gritim")
        self.inimigo = Inimigo("Xampson", 40, 5, "Fogo")

    def iniciar_batalha(self):
        print("Iniciando Batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens: ")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("precione enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

jogo = Jogo()
jogo.iniciar_batalha()