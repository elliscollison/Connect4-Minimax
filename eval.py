import math


def evaluate(rack, comp_id):
    width = len(rack)
    height = len(rack[0])  # might need to switch these????
    rack_score = 0
    print("test")
    if comp_id == 1:
        print("Player score is 2")
        player_id = 2
    else:
        print("Player score is 1")
        player_id = 1

    for i in range(width):
        for j in range(height):
                # Start by checking for largest streaks first

                # Horizontal checks:

                # Comp check (max)
            try:
                if (rack[i][j]) == (rack[i + 1][j]) == rack[i + 2][j] == rack[i + 3][j] == comp_id:
                    return math.inf  # can stop early here
                elif rack[i][j] == rack[i + 1][j] == rack[i + 2][j] == comp_id and rack[i + 3][j] == 0:
                    rack_score += 100
                elif rack[i][j] == rack[i + 1][j] == comp_id and rack[i + 2][j] == rack[i + 3][j] == 0:
                    print("me horizontal 2")
                    rack_score += 10
                elif rack[i][j] == comp_id and rack[i + 1][j] == rack[i + 2][j] == rack[i + 3][j] == 0:
                    print("me horizontal 1")
                    rack_score += 1

                    # Opponent checks (min)
                if rack[i][j] == rack[i + 1][j] == rack[i + 2][j] == rack[i + 3][j] == player_id:
                    return - math.inf  # can stop early here
                elif rack[i][j] == rack[i + 1][j] == rack[i + 2][j] == player_id and rack[i + 3][j] == 0:
                    print("opposite horizontal 3")
                    rack_score += -100
                elif rack[i][j] == rack[i + 1][j] == player_id and rack[i + 2][j] == rack[i + 3][j] == 0:
                    rack_score += -10
                elif rack[i][j] == player_id and rack[i + 1][j] == rack[i + 2][j] == rack[i + 3][j] == 0:
                    rack_score += -1
            except IndexError:
                pass

                # Vertical checks:

                # Comp check (max)
            try:
                if rack[i][j] == rack[i][j + 1] == rack[i][j + 2] == rack[i][j + 3] == comp_id:
                    return math.inf  # can stop early here
                elif rack[i][j] == rack[i][j + 1] == rack[i][j + 2] == comp_id and rack[i][j + 3] == 0:
                    rack_score += 100
                elif rack[i][j] == rack[i][j + 1] == comp_id and rack[i][j + 2] == rack[i][j + 3] == 0:
                    print("me vertical 2")
                    rack_score += 10
                elif rack[i][j] == comp_id and rack[i][j + 1] == rack[i][j + 2] == rack[i][j + 3] == 0:
                    print("me vertical 1")
                    rack_score += 1

                    # Opponent checks (min)
                if rack[i][j] == rack[i][j + 1] == rack[i][j + 2] == rack[i][j + 3] == player_id:
                    return - math.inf  # can stop early here
                elif rack[i][j] == rack[i][j + 1] == rack[i][j + 2] == player_id and rack[i][j + 3] == 0:
                    rack_score += -100
                elif rack[i][j] == rack[i][j + 1] == player_id and rack[i][j + 2] == rack[i][j + 3] == 0:
                    rack_score += -10
                elif rack[i][j] == player_id and rack[i][j + 1] == rack[i][j + 2] == rack[i][j + 3] == 0:
                    print("opposite vertical 1")
                    rack_score += -1
            except IndexError:
                pass

                # Up right Diagonal checks

                # Comp check (max)
            try:
                if rack[i][j] == rack[i + 1][j + 1] == rack[i + 2][j + 2] == rack[i + 3][j + 3] == comp_id:
                    return math.inf  # can stop early here
                elif rack[i][j] == rack[i + 1][j + 1] == rack[i + 2][j + 2] == comp_id and rack[i + 3][j + 3] == 0:
                    rack_score += 100
                elif rack[i][j] == rack[i + 1][j + 1] == comp_id and rack[i + 2][j + 2] == rack[i + 3][j + 3] == 0:
                    print("me up right 2")
                    rack_score += 10
                elif rack[i][j] == comp_id and rack[i + 1][j + 1] == rack[i + 2][j + 2] == rack[i + 3][j + 3] == 0:
                    print("me up right 1")
                    rack_score += 1

                    # Opponent checks (min)
                if rack[i][j] == rack[i + 1][j + 1] == rack[i + 2][j + 2] == rack[i + 3][j + 3] == player_id:
                    return - math.inf  # can stop early here
                elif rack[i][j] == rack[i + 1][j + 1] == rack[i + 2][j + 2] == player_id and rack[i + 3][j + 3] == 0:
                    rack_score += -100
                elif rack[i][j] == rack[i + 1][j + 1] == player_id and rack[i + 2][j + 2] == rack[i + 3][j + 3] == 0:
                    rack_score += -10
                elif rack[i][j] == player_id and rack[i + 1][j + 1] == rack[i + 2][j + 2] == rack[i + 3][j + 3] == 0:
                    rack_score += -1
            except IndexError:
                pass

                # Down right Diagonal checks

                # Comp check (max)
            try:
                if rack[i][j] == rack[i + 1][j - 1] == rack[i + 2][j - 2] == rack[i + 3][j - 3] == comp_id:
                    return math.inf  # can stop early here
                elif rack[i][j] == rack[i + 1][j - 1] == rack[i + 2][j - 2] == comp_id and rack[i + 3][j - 3] == 0:
                    rack_score += 100
                elif rack[i][j] == rack[i + 1][j - 1] == comp_id and rack[i + 2][j - 2] == rack[i + 3][j - 3] == 0:
                    rack_score += 10
                elif rack[i][j] == comp_id and rack[i + 1][j - 1] == rack[i + 2][j - 2] == rack[i + 3][j - 3] == 0:
                    print("me up left 1")
                    rack_score += 1

                    # Opponent checks (min)
                if rack[i][j] == rack[i + 1][j - 1] == rack[i + 2][j - 2] == rack[i + 3][j - 3] == player_id:
                    return - math.inf  # can stop early here
                elif rack[i][j] == rack[i + 1][j - 1] == rack[i + 2][j - 2] == player_id and rack[i + 3][j - 3] == 0:
                    rack_score += -100
                elif rack[i][j] == rack[i + 1][j - 1] == player_id and rack[i + 2][j - 2] == rack[i + 3][j - 3] == 0:
                    rack_score += -10
                elif rack[i][j] == player_id and rack[i + 1][j - 1] == rack[i + 2][j - 2] == rack[i + 3][j - 3] == 0:
                    print("opposite up left 1")
                    rack_score += -1
            except IndexError:
                pass
    return rack_score


def evaluate2(rack, comp_id):
    if comp_id == 1:
        player_id = 2
    else:
        player_id = 1

    rack_score = 0

    # Check vertical quartets
    for col_list in rack:
        for row in range(len(col_list) - 3):
            streak = col_list[row: row + 4]

            print("Vert streak: ", streak)

            if streak.count(comp_id) == 4:
                return math.inf
            elif streak.count(comp_id) == 3 and streak.count(player_id) == 0:
                rack_score += 100
            elif streak.count(comp_id) == 2 and streak.count(player_id) == 0:
                rack_score += 10
            elif streak.count(comp_id) == 1 and streak.count(player_id) == 0:
                print("Comp up + 1")
                rack_score += 1

            if streak.count(player_id) == 4:
                return - math.inf
            elif streak.count(comp_id) == 0 and streak.count(player_id) == 3:
                rack_score += -100
            elif streak.count(comp_id) == 0 and streak.count(player_id) == 2:
                rack_score += -10
            elif streak.count(comp_id) == 0 and streak.count(player_id) == 1:
                print("Other up - 1")
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

            print(up_diag_streak)

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


