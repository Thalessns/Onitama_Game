from color import Color;
from position import Position;

class Card:

    # Construtor
    def __init__(self, name: str, color: Color, positions: Position):
        self.name       = name;
        self.color      = color;
        self.positions  = positions;

    # Método que sorteia cinco cartas
    @staticmethod
    def randomCards(cards: list):
        # Importando módulo essencial
        from random import randint;
        # Lista que vai armazenar as cartas sorteadas
        result = list();
        # Contador
        count = 0;
        while count != 5:
            sorted = randint(0, 7);
            if cards[sorted] not in result: 
                result.append(cards[sorted]);
                count += 1;
        # Retornando cards sorteados
        return result;

    # Método que verifica se um card executa um determinado movimento
    def check_move(self, move):
        if move in self.positions: return True;
        return False;

    # Método para criar um card
    @staticmethod
    def create_card(name: str, color: Color, rows: list, cols: list):
        # Array que vai guardar as posições
        moves = list();
        # Passando por todas as posições
        for i in range(0, len(rows)):
            moves.append(Position(rows[i], cols[i]));
        # Retornando carta
        return Card(name, color, moves);

    # Método que cria e devolve uma lista de cards
    @staticmethod
    def create_cards():
        
        # Array que vai guardar todos as cartas
        allCards = list();

        # Cartas Vermelhas *************************************************************************

        # Criando a carta Dragon
        dragonRows = [1, 1, -1, -1];
        dragonCols = [-1, 1, 2, -2];
        
        allCards.append(Card.create_card("DRAGON", Color.RED, dragonRows, dragonCols));

        # Criando a carta Frog
        frogRows = [1, -1, 0];
        frogCols = [1, -1, -2];

        allCards.append(Card.create_card("FROG", Color.RED, frogRows, frogCols));

        # Criando a carta Elephant
        eleRows = [0, 0, -1, -1];
        eleCols = [1, -1, 1, -1];

        allCards.append(Card.create_card("ELEPHANT", Color.RED, eleRows, eleCols));

        # Criando a carta Rooster
        roosterRows = [0, -1, 0, 1];
        roosterCols = [1, 1, -1, -1];

        allCards.append(Card.create_card("ROOSTER", Color.RED, roosterRows, roosterCols));

        # Cartas Azuis *************************************************************************

        # Criando a carta Tiger
        tigerRows = [1, -2];
        tigerCols = [0, 0];

        allCards.append(Card.create_card("TIGER", Color.BLUE, tigerRows, tigerCols));

        # Criando a carta Rabbit
        rabbitRows = [1, -1, 0];
        rabbitCols = [-1, 1, 2];

        allCards.append(Card.create_card("RABBIT", Color.BLUE, rabbitRows, rabbitCols));

        # Criando a carta Crab
        crabRows = [-1, 0, 0];
        crabCols = [0, 2, -2];

        allCards.append(Card.create_card("CRAB", Color.BLUE, crabRows, crabCols));

        # Criando a carta Goose
        gooseRows = [0, 0, 1, -1];
        gooseCols = [1, -1, 1, -1];

        allCards.append(Card.create_card("GOOSE", Color.BLUE, gooseRows, gooseCols));

        # Sorteando cinco cards e retornando-os
        return Card.randomCards(allCards);


    # Getters
    @property
    def name(self):
        return self.__name;

    @property
    def color(self):
        return self.__color;

    @property
    def positions(self):
        return self.__positions;

    # Setters
    @name.setter
    def name(self, name):
        self.__name = name;

    @color.setter
    def color(self, color):
        self.__color = color;

    @positions.setter
    def positions(self, positions):
        self.__positions = positions;