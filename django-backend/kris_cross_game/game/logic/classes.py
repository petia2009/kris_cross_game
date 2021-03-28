import uuid


class Game:
    def __init__(self):
        self.__game_id__ = str(uuid.uuid4())
        self.__field_class__ = FieldXO()

    def get_field_class(self):
        return self.__field_class__

    def get_game_id(self):
        return self.__game_id__


class FieldXO:
    def __init__(self):
        self.__field__ = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.move_x = True
        self.move_y = False

    def is_this_move_win(self, x_or_o, x, y):
        self.__field__[y][x] = x_or_o
        if self.is_winner(self.get_whoose_move()):
            return True
        else:
            self.move_x, self.move_y = self.move_y, self.move_x
            return False

    def get_whoose_move(self):
        if self.move_x:
            return "X"
        else:
            return "O"

    def get_field(self):
        return self.__field__

    def is_winner(self, player_type):
        for i in range(3):
            has_winner = False
            if self.__field__[i][0] != player_type:
                continue
            for j in range(1, 3):
                if self.__field__[i][j] != player_type:
                    has_winner = False
                    break
                else:
                    has_winner = True
            if has_winner:
                return True

        for i in range(3):
            has_winner = False
            if self.__field__[0][i] != player_type:
                continue
            for j in range(1, 3):
                if self.__field__[j][i] != player_type:
                    has_winner = False
                    break
                else:
                    has_winner = True
            if has_winner:
                return True

        if (self.__field__[0][0] == player_type and self.__field__[2][2] == player_type) \
                or (self.__field__[0][2] == player_type and self.__field__[2][0] == player_type):
            return True
