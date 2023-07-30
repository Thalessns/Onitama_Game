from abc import ABC;
from os import system, name;

class Utils(ABC):

    # Limpar terminal
    @staticmethod
    def clear():
        if name is "nt":
            system('cls');
        else:
            system("clear");

    # Mensagem
    def title(msg: str):
        Utils.bars();
        print(f"{msg:^28}");
        Utils.bars();

    # Divisão Visual
    def bars():
        print("-"*28);
    