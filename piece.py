from color import Color;

class Piece():

    # Construtor
    def __init__(self, color=Color.NONE, isMaster=False):
        self.color      = color;
        self.isMaster   = isMaster;
        self.alive      = True;

    # Metódo para criação das peças
    @staticmethod
    def create_pieces(pieceColor):
        pieces = list();
        for i in range(0, 5):
            # Inserindo peças na lista     
            pieces.append(Piece(color=pieceColor)) if i != 2 else pieces.append(Piece(color=pieceColor, isMaster=True));
        return pieces;

    # Getters
    @property
    def color(self):
        return self.__color;

    @property
    def isMaster(self):
        return self.__isMaster;

    @property
    def alive(self):
        return self.__alive;

    # Setters
    @color.setter
    def color(self, color):
        self.__color = color;

    @isMaster.setter
    def isMaster(self, status):
        self.__isMaster = status;

    @alive.setter
    def alive(self, status):
        self.__alive = status;