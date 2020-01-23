"""
This Connect Four player uses minimax to choose the optimal column to play in.
It's difficulty level is based on the number of plies that it will search through
to find the optimal move.
"""
__author__ = "Ellis W. Collison"
__license__ = "MIT"
__date__ = "October 2019"

import math
from copy import deepcopy


class ComputerPlayer:
    def __init__(self, id, difficulty_level):
        """
        Constructor, takes a difficulty level (likely the # of plies to look
        ahead), and a player ID that's either 1 or 2 that tells the player what
        its number is.
        """
        self.id = id
        self.difficulty_level = difficulty_level

    def pick_move(self, rack):
        """
        Pick the move to make. It will be passed a rack with the current board
        layout, column-major. A 0 indicates no token is there, and 1 or 2
        indicate discs from the two players. Column 0 is on the left, and row 0 
        is on the bottom. It must return an int indicating in which column to 
        drop a disc. The player current just pauses for half a second (for 
        effect), and then chooses a random valid move.
        """
        rack_list = list(map(list, rack))
        possible_moves = {}

        if self.id == 1:
            opposing_player = 2
        else:
            opposing_player = 1

        for col in range(len(rack_list)):
            if self._is_legal(rack_list, col):
                hldr = _make_move(rack_list, col, self.id)
                possible_moves[col] = -self._search(hldr, self.difficulty_level - 1, opposing_player)

        return max(possible_moves, key=possible_moves.get)

    def _eval(self, rack, current_player):
        comp_id = current_player
        if comp_id == 1:
            player_id = 2
        else:
            player_id = 1

        rack_score = 0

        # Check vertical quartets
        for col_list in rack:
            for row in range(len(col_list) - 3):
                streak = col_list[row: row + 4]

                if streak.count(comp_id) == 4:
                    return math.inf
                elif streak.count(comp_id) == 3 and streak.count(player_id) == 0:
                    rack_score += 100
                elif streak.count(comp_id) == 2 and streak.count(player_id) == 0:
                    rack_score += 10
                elif streak.count(comp_id) == 1 and streak.count(player_id) == 0:
                    rack_score += 1

                if streak.count(player_id) == 4:
                    return - math.inf
                elif streak.count(comp_id) == 0 and streak.count(player_id) == 3:
                    rack_score += -100
                elif streak.count(comp_id) == 0 and streak.count(player_id) == 2:
                    rack_score += -10
                elif streak.count(comp_id) == 0 and streak.count(player_id) == 1:
                    rack_score += -1

        # Check horizontal quartets
        for height in range(len(rack)-1):
            row_list = [col[height] for col in rack]

            for i in range(len(row_list) - 3):
                horizontal_streak = row_list[i:i+4]

                if horizontal_streak.count(comp_id) == 4:
                    return math.inf
                elif horizontal_streak.count(comp_id) == 3 and horizontal_streak.count(player_id) == 0:
                    rack_score += 100
                elif horizontal_streak.count(comp_id) == 2 and horizontal_streak.count(player_id) == 0:
                    rack_score += 10
                elif horizontal_streak.count(comp_id) == 1 and horizontal_streak.count(player_id) == 0:
                    rack_score += 1

                if horizontal_streak.count(player_id) == 4:
                    return -math.inf
                elif horizontal_streak.count(comp_id) == 0 and horizontal_streak.count(player_id) == 3:
                    rack_score += -100
                elif horizontal_streak.count(comp_id) == 0 and horizontal_streak.count(player_id) == 2:
                    rack_score += -10
                elif horizontal_streak.count(comp_id) == 0 and horizontal_streak.count(player_id) == 1:
                    rack_score += -1

        # Check up diag quartets
        for i in range(len(rack) - 3):
            for j in range(len(rack[i]) - 3):
                up_diag_streak = [rack[i+k][j+k] for k in range(4)]

                if up_diag_streak.count(comp_id) == 4:
                    return math.inf
                elif up_diag_streak.count(comp_id) == 3 and up_diag_streak.count(player_id) == 0:
                    rack_score += 100
                elif up_diag_streak.count(comp_id) == 2 and up_diag_streak.count(player_id) == 0:
                    rack_score += 10
                elif up_diag_streak.count(comp_id) == 1 and up_diag_streak.count(player_id) == 0:
                    rack_score += 1

                if up_diag_streak.count(player_id) == 4:
                    return -math.inf
                elif up_diag_streak.count(comp_id) == 0 and up_diag_streak.count(player_id) == 3:
                    rack_score += -100
                elif up_diag_streak.count(comp_id) == 0 and up_diag_streak.count(player_id) == 2:
                    rack_score += -10
                elif up_diag_streak.count(comp_id) == 0 and up_diag_streak.count(player_id) == 1:
                    rack_score += -1

        # Check down diag quartets
        for i in range(len(rack) - 3):
            for j in reversed(range(3, len(rack[i]))):
                down_diag_streak = [rack[i + k][j - k] for k in range(4)]

                if down_diag_streak.count(comp_id) == 4:
                    return math.inf
                elif down_diag_streak.count(comp_id) == 3 and down_diag_streak.count(player_id) == 0:
                    rack_score += 100
                elif down_diag_streak.count(comp_id) == 2 and down_diag_streak.count(player_id) == 0:
                    rack_score += 10
                elif down_diag_streak.count(comp_id) == 1 and down_diag_streak.count(player_id) == 0:
                    rack_score += 1

                if down_diag_streak.count(player_id) == 4:
                    return -math.inf
                elif down_diag_streak.count(comp_id) == 0 and down_diag_streak.count(player_id) == 3:
                    rack_score += -100
                elif down_diag_streak.count(comp_id) == 0 and down_diag_streak.count(player_id) == 2:
                    rack_score += -10
                elif down_diag_streak.count(comp_id) == 0 and down_diag_streak.count(player_id) == 1:
                    rack_score += -1

        return rack_score

    def _search(self, rack, depth, current_player):
        possible_moves = []
        for i in range(len(rack)):
            if self._is_legal(rack, i):
                temp_rack = _make_move(rack, i, current_player)
                possible_moves.append(temp_rack)

        if depth == 0 or self._is_goal(rack) or len(possible_moves) == 0:
            return self._eval(rack, current_player)
        else:
            if current_player == 1:
                opposing_player = 2
            else:
                opposing_player = 1

            val = -9999999
            for child in possible_moves:
                val = max(val, -self._search(child, depth - 1, opposing_player))

            return val

    def _is_goal(self, rack):
        rack_score = self._eval(rack, 1)

        if rack_score == math.inf or rack_score == -math.inf:
            return True
        else:
            return False

    def _is_legal(self, rack, col):
        if 0 in rack[col]:
            return True
        else:
            return False


def _make_move(rack, col, player_id):
    new_rack = deepcopy(rack)
    for row in range(len(new_rack[col])):
        if new_rack[col][row] == 0:
            new_rack[col][row] = player_id
            return new_rack
