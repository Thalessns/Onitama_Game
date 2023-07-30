from abc import ABC;
from game import Game;
from utils import Utils;

class App(ABC):

    @staticmethod
    def play():
        try:
            # Limpando a tela
            Utils.clear();
            # Obtendo nome dos jogadores
            bName = input("Nome do Jogador Azul: ");
            rName = input("Nome do jogador Vermelho: ");
            # iniciando jogo
            Game(bName, rName);
        except Exception as error:
            print(f"OnitamaGameException: {error}");
        finally:
            # Variável que vai armazenar a resposta do usuário
            resp = "";
            # Loop
            while resp.lower() != "s" and resp.lower() != "n":
                resp = input("Deseja jogar novamente? [S/N]: ");
                Utils.bars();
            # Verificando resposta
            if resp.lower() == "s": App.play();
            # Saindo
            return;
App.play();