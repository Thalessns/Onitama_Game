from color import Color;
from card import Card;
from exception import InvalidCardException;

class Player:
    
    # Construtor
    def __init__(self, name: str, pieceColor: Color, cards: list):
        self.name = name;
        self.pieceColor = pieceColor;
        self.cards = cards;

    # Método que verifica se o jogador possui um determinado card
    def has_card(self, card):
        return True if card in self.cards else False;

    # Método que substitui um card
    def __replace_card(self, old: Card, new: Card):       
        i = self.cards.index(old);
        self.cards[i] = new;

    def swap_card(self, oldCard: Card, newCard: Card):
        if newCard == None:
            raise InvalidCardException("A carta da mesa é inválida!");
        elif not self.has_card(oldCard):
            raise InvalidCardException(f"A carta {oldCard.name} não está na mão do jogador!");
        # Substituindo card
        self.__replace_card(oldCard, newCard);

    # Getters
    @property
    def name(self):
        return self.__name;

    @property
    def pieceColor(self):
        return self.__pieceColor;

    @property
    def cards(self):
        return self.__cards;

    # Setters
    @name.setter
    def name(self, name):
        self.__name = name;

    @pieceColor.setter
    def pieceColor(self, color):
        self.__pieceColor = color;

    @cards.setter
    def cards(self, cards):
        self.__cards = cards;