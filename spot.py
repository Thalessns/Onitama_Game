from color import Color;
from piece import Piece;
from position import Position;
from exception import IllegalMovementException;

class Spot:

    # Construtor
    def __init__(self, position, piece=None, color=Color.NONE):
        self.position = position;
        self.piece = piece;
        self.color = color;

    # Método que libera o espaço
    def release_spot(self):
        self.piece = None;

    # Método que verifica se um espaço pode ser ocupado
    def occupy_spot(self, piece: Piece):
        # Verificando se o espaço já está vazio
        if self.piece is None:
            self.piece = piece;
            return;
        elif piece.color is self.piece.color:
            raise IllegalMovementException("Existe outra peça de mesma cor neste espaço!");
        self.piece.alive = False;
        self.piece = piece;
        return;

    # Método de criação do tabuleiro
    @staticmethod
    def create_table(bluePieces, redPieces):
        table = [list(), list(), list(), list(), list()];
        for i in range(0, 5): # Coluna
            for j in range(0, 5): # Linha
                # Verificando se é uma linha de peças
                if i == 0 or i == 4:
                    # Verificando se é um templo
                    if i == 0 and j == 2:
                        # É um templo azul
                        table[i].append(Spot(piece=bluePieces[j], position=Position(i, j), color=Color.BLUE));
                    elif i == 4 and j == 2:
                        # È um tempo vermelho
                        table[i].append(Spot(piece=redPieces[j], position=Position(i, j), color=Color.RED));
                    else:
                        # Não é um tempo, mas tem uma peça
                        if i == 0: 
                            table[i].append(Spot(piece=bluePieces[j], position=Position(i, j)));
                        else:
                            table[i].append(Spot(piece=redPieces[j], position=Position(i, j)));
                else:
                    # Não possui peça nem cor
                    table[i].append(Spot(position=Position(i, j)));
        
        # Retornando tabuleiro
        return table;
        
    # Getters
    @property
    def position(self):
        return self.__position;
    
    @property
    def piece(self):
        return self.__piece;

    @property
    def color(self):
        return self.__color;

    # Setters
    @position.setter
    def position(self, pos):
        self.__position = pos;

    @piece.setter
    def piece(self, piece):
        self.__piece = piece;

    @color.setter
    def color(self, color):
        self.__color = color;