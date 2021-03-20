import uuid


class Game:
    def __init__(self):
        self.game_id = uuid.uuid4()

    def get_game_id(self):
        return self.game_id


class FieldXO:
    def __init__(self):
        self.__field__ = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ['X', ' ', ' ']
        ]

    def move(self, x_or_o, x, y):
        self.__field__[y][x] = x_or_o

    def get_field(self):
        return self.__field__
