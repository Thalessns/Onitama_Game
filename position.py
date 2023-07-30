class Position:
    
    # Construtor
    def __init__(self, row, col):
        self.row = row;
        self.col = col;

    # Getters
    @property
    def row(self):
        return self.__row;

    @property
    def col(self):
        return self.__col;

    # Getters
    @row.setter
    def row(self, row):
        self.__row = row;

    @col.setter
    def col(self, col):
        self.__col = col;