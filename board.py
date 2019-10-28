from collections import Counter
from enum import IntEnum


class InvalidMoveException(Exception):
    pass


class Status(IntEnum):
    INCOMPLETE = 0
    TIE = 1

    X_WINS = 2
    O_LOSES = 2

    O_WINS = 3
    X_LOSES = 3


class Board:

    def __init__(self):
        self._state = [" "] * 9

    @property
    def state(self):
        return self._state

    def reset(self):
        self._state = [" "] * 9

    def play(self, pos, player):
        '''Updates board state

        # Arguments:
            pos: tuple(row, col). Index starts at 0
            player: char. Either of 'X' or 'O'
        '''
        player = player.upper()
        if player not in {"X", "O"}:
            raise InvalidMoveException("Player must either be 'X' or 'O'")
        opp = ({'X', 'O'} - {player}).pop()

        if pos < 0 or pos > 8:
            raise InvalidMoveException("Position must be 0 <= value < 9 ")

        if self.state[pos] != " ":
            raise InvalidMoveException(
                "The position {} is not empty".format(pos))

        counts = Counter(self.state)
        if (counts[player] + 1) - counts[opp] > 1:
            raise InvalidMoveException(
                "Difference between number of moves will be greater than 2")

        self._state[pos] = player

    @property
    def R1(self):
        return [self.state[0], self.state[1], self.state[2]]

    @property
    def R2(self):
        return [self.state[3], self.state[4], self.state[5]]

    @property
    def R3(self):
        return [self.state[6], self.state[7], self.state[8]]

    @property
    def C1(self):
        return [self.state[0], self.state[3], self.state[6]]

    @property
    def C2(self):
        return [self.state[1], self.state[4], self.state[7]]

    @property
    def C3(self):
        return [self.state[2], self.state[5], self.state[8]]

    @property
    def D1(self):
        return [self.state[0], self.state[4], self.state[8]]

    @property
    def D2(self):
        return [self.state[2], self.state[4], self.state[6]]

    @property
    def rows(self):
        return [self.R1, self.R2, self.R3]

    @property
    def cols(self):
        return [self.C1, self.C2, self.C3]

    @property
    def diags(self):
        return [self.D1, self.D2]

    @property
    def game_status(self):
        for squares in self.rows + self.cols + self.diags:
            if set(squares) == {'X'}:
                return Status.X_WINS
            if set(squares) == {'O'}:
                return Status.O_WINS

        if " " in set(self.state):
            return Status.INCOMPLETE
        else:
            return Status.TIE

    def __str__(self):
        str_ = ""
        for i, square in enumerate(self._state):
            if i % 3 == 0:
                str_ += '\n'

            if square == " ":
                str_ += "* "
            else:
                str_ += square + " "

        str_ += '\n'

        return str_
