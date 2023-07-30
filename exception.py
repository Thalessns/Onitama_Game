class OnitamaGameException(Exception):
    pass;

class InvalidCardException(OnitamaGameException):
    pass;

class IllegalMovementException(OnitamaGameException):
    pass;

class IllegalSpotException(OnitamaGameException):
    pass;

class IncorrectTurnOrderException(OnitamaGameException):
    pass;

class InvalidPieceException(OnitamaGameException):
    pass;