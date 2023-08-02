class Position:
    
    # Construtor
    def __init__(self, row, col):
        self.__row = row;
        self.__col = col;

    # Getters
    @property
    def row(self):
        return self.__row;

    @property
    def col(self):
        return self.__col;