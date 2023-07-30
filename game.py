from color import Color;
from piece import Piece;
from player import Player;
from card import Card;
from spot import Spot;
from position import Position;
from exception import IncorrectTurnOrderException, IllegalMovementException, InvalidCardException, InvalidPieceException, IllegalSpotException;
from os import system, name;

class Game:

    # Construtor
    def __init__(self, blueName="Blue Player", redPlayer="Red Player"):
        # Obtendo cartas
        cards = Card.create_cards();
        # Carta da mesa
        self.__tableCard = cards[4];
        # Criando Players
        self.__bluePlayer = Player(blueName, Color.BLUE, cards[:2]);
        self.__redPlayer  = Player(redPlayer, Color.RED, cards[2:4]);
        # Criando peças
        self.__bluePieces = Piece.create_pieces(Color.BLUE);
        self.__redPieces  = Piece.create_pieces(Color.RED);
        # Criando tabuleiro
        self.__table = Spot.create_table(self.bluePieces, self.redPieces);
        # Primeiro turno
        self.__turn = self.tableCard.color;
        # Iniciando jogo
        self.__play();
    
    # Limpar terminal
    def __clear(self):
        if name is "nt":
            system('cls');
        else:
            system("clear");

    # Passando turno
    def __pass_turn(self):
        # Verificando se era a vez do azul
        if self.turn is Color.BLUE:
            self.__turn = Color.RED;
        elif self.turn is Color.RED:
            self.__turn = Color.BLUE;

    # Devolve o dono de uma determianda carta
    def __find_card_owner(self, target: Card):
        # Referencia dos jogadores
        pB = self.__bluePlayer;
        pR = self.__redPlayer;
        # Verificando qual deles têm a carta
        if pB.has_card(target): return pB;
        elif pR.has_card(target): return pR;
        # Nenhum deles têm a carta
        return None;

    # Método verifica se o movimento pode ser inválido
    def __check_limits(self, current: Position, move: Position):
        # Verificando se a linha resultante é válida
        if((current.row + move.row) not in range(0, 5)):
            return False;
        elif ((current.col + move.col) not in range(0, 5)):
            return False;
        return True;

    def __check_victory(self, color: Color):
        # Verificando se é o jogador azul
        if color is Color.BLUE:
            # Verificando se o mestre vermelho foi derrotado
            if not self.redPieces[2].alive: return True;
            # Verificando se o mestre aliado está no templo inimigo
            piece = self.__get_spot(4, 2).piece;
            if piece and piece.isMaster is True and piece.color is Color.BLUE: return True;
        elif color is Color.RED:
            # Verificando se o mestre azul foi derrotado
            if not self.bluePieces[2].alive: return True;
            # Verificando se o mestre aliado está no templo inimigo
            piece = self.__get_spot(0, 2).piece;
            if piece and piece.isMaster is True and piece.color is Color.RED: return True;
        return False;

    def __make_move(self, card: Card, cardMove: Position, currentPos: Position):
        # Obtendo peça que sera movida
        piece = self.__get_spot(currentPos.row, currentPos.col).piece;

        # Obtendo dono da carta jogada
        cardOwner = self.__find_card_owner(card);

        # Verificando se a peça existe
        if piece is None:
            raise InvalidPieceException(f"Não existe uma peça no espaço escolhido (ROW:{currentPos.row}|COL:{currentPos.col}).");
        # Verificando se a peça que será movida é do jogador atual
        elif piece.color is not self.turn:
            raise IncorrectTurnOrderException(f"Você está tentando mover a peça do adversário! (ROW:{currentPos.row}|COL:{currentPos.col})");
        # Verificando se a peça está viva
        elif not piece.alive:
            raise InvalidPieceException(f"A peça escolhida não está mais no tabuleiro!");
        # Verificando se a carta existe
        elif card is None:
            raise InvalidCardException(f"A carta jogada não é válida!");
        # Verificando se algum jogador possui a carta jogada
        elif cardOwner is None:
            raise InvalidCardException(f"Nenhum dos jogadores possui a carta jogada!");
        # Verificando se o movimento é válido
        elif not card.check_move(cardMove):
            raise IllegalMovementException(f"O movimento escolhido é inválido!");
        # Verificando se o movimento obedece os limites do tabuleiro]
        elif not self.__check_limits(currentPos, cardMove):
            raise IllegalMovementException(f"O movimento não obedece os limites do tabuleiro!");

        # Pegando referência ao espaço que será ocupado
        finalRow = currentPos.row + cardMove.row;
        finalCol = currentPos.col + cardMove.col;
        destiny  = self.__get_spot(finalRow, finalCol);
        # Ocupando espaço
        destiny.occupy_spot(piece);

        # Pegando referência ao espaço inicial
        start = self.__get_spot(currentPos.row, currentPos.col);
        # Liberando espaço inicial
        start.release_spot();

        # Trocando cartas
        tableCardBackup = self.__tableCard;
        cardOwner.swap_card(oldCard=card, newCard=tableCardBackup);
        # Atualizando carta da mesa
        self.__tableCard = card;

        # Passando turno
        self.__pass_turn();

    def show_table(self):
        # Mostrando mensagem
        print("-"*28);
        print(f"{'Mostrando Tabuleiro':^28}");
        print("-"*28);
        # Mostrando número das colunas
        for i in range(0, 5): print(f"x\y {i:>2}", end="") if i == 0 else print(f"{i:>5}", end="");
        print();
        # Passando por cada espaço do tabuleiro
        for row in range(0, 5):
            # Mostrando número das linhas
            print(f" {row} ", end="")
            for col in range(0, 5):
                # Pegando peça que ocupa o espaço
                piece = self.__get_spot(row, col).piece;
                if piece is None:
                    print("|   |", end="");
                elif piece.color is Color.BLUE:
                    print("| B |", end="") if piece.isMaster else print("| b |", end="");
                else:
                    print("| R |", end="") if piece.isMaster else print("| r |", end="");
            print("");
        print("-"*28);
        print(f"Carta da Mesa: {self.__tableCard.name}");
        print("-"*28);

    def __select_card(self, cards: list(), cardName: str):
        if cards[0].name.lower() == cardName.lower():
            return cards[0];
        elif cards[1].name.lower() == cardName.lower():
            return cards[1];
        else:
            raise InvalidCardException("A carta escolhida não existe!");

    def __play(self):
        # Variáveis essenciais
        player = None;
        cards  = list();
        cardChoice = Card;
        # Verificando se algum jogador venceu
        while not self.__check_victory(Color.BLUE) and not self.__check_victory(Color.RED):
            try:
                # Limpando tela
                self.__clear();
                # verificando jogador atual
                if self.__turn == Color.BLUE: player = self.__bluePlayer  
                else: player = self.__redPlayer;
                # Obtendo cartas
                cards = player.cards;
                
                # Mostrando jogador atual
                print("-"*28);
                print(f"Jogador: {player.name}\nCor: {player.pieceColor}");
                
                # Mostrando Tabuleiro
                self.show_table();

                # Mostrando cartas
                for card in cards:
                    print(f"Carta: {card.name}");
                    for move in card.positions:
                        print(f"[{card.positions.index(move)}] -> Row: {move.row:<2} | Col: {move.col}");
                    print("-"*28);

                # Escolhendo a peça que será movida
                target = input(f"Escolha uma peça para mover [x,y]: ");

                # Verificando a posição é válida
                if not ',' in target:
                    raise IllegalSpotException("Você passou uma posição inválida!");
                # Quebrando string
                target = target.split(",");
                # Veruficando se são números
                if (not target[0].isdigit()) or (not target[1].isdigit()):
                    raise TypeError("Digite apenas números para escolher a peça!");
                elif len(target) > 2:
                    raise IllegalSpotException("Digite apenas dois números!");

                # Obtendo posição da peça
                currentPos = Position(int(target[0]), int(target[1]));

                # Verificando se a posição inicial é válida
                if currentPos.row not in range(0, 5) or currentPos.col not in range(0, 5):
                    raise IllegalSpotException("O espaço escolhido não existe!");

                # Escolhendo a carta que sera movida
                cardName = input(f"Escolha uma carta, pelo nome [{cards[0].name} ou {cards[1].name}]: ");
                # Buscando referência da carta
                cardChoice = self.__select_card(cards, cardName);
                
                # Escolhendo movimentos
                move = input(f"Escolha o movimento da carta [0 até {len(cardChoice.positions)-1}]: ");
                
                # Verificando se o movimento foi válido
                if not move.isdigit():
                    raise TypeError("Digite apenas um número para escolher o movimento!");
                elif int(move) not in range(0, len(cardChoice.positions)):
                    raise IllegalMovementException("Digite apenas um número dentro do intervalo dado!");
                
                # Preparando para movimentar a peça
                move = cardChoice.positions[int(move)];

                # Iniciando movimentação
                self.__make_move(cardChoice, move, currentPos);

            except InvalidCardException as error:
                print(f"InvalidCardException: {error}");
                input("Pressione ENTER para continuar...");
                self.__play();
            except IllegalSpotException as error:
                print(f"IllegalSpotException: {error}");
                input("Pressione ENTER para continuar...");
                self.__play();
            except IllegalMovementException as error:
                print(f"IllegalMovementException: {error}");
                input("Pressione ENTER para continuar...");
                self.__play();
            except InvalidPieceException as error:
                print(f"InvalidPieceException: {error}");
                input("Pressione ENTER para continuar...");
                self.__play();
            except IncorrectTurnOrderException as error:
                print(f"IncorrectTurnOrderException: {error}");
                input("Pressione ENTER para continuar...");
                self.__play();
            except TypeError as error:
                print(f"TypeError: {error}");
                input("Pressione ENTER para continuar...");
                self.__play();
            except KeyboardInterrupt as error:
                print(f"\nKeyboardInterrupt: ", end="");
                print("Encerrando...");
                return;
        
        self.__clear();
        # Mostrando jogador atual
        print("-"*28);
        print(f"Jogador: {player.name}\nCor: {player.pieceColor}");
        # Mostrando Tabuleiro
        self.show_table();

        # Mostrando vencedor
        print("-"*28);
        print(f"Parabéns {player.name}, você venceu!");

    # Getters
    @property
    def bluePlayer(self):
        return self.__bluePlayer;

    @property
    def bluePieces(self):
        return self.__bluePieces;

    @property
    def redPlayer(self):
        return self.__redPlayer;

    @property
    def redPieces(self):
        return self.__redPieces;

    @property
    def table(self):
        return self.__table;

    @property
    def tableCard(self):
        return self.__tableCard;

    @property
    def turn(self):
        return self.__turn;

    def __get_spot(self, row, col):
        return self.__table[row][col];


play = Game();
