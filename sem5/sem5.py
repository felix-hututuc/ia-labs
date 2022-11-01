class Player:
    def __init__(self, name, moves) -> None:
        self.name = name
        self.moves = moves


class Game:
    def __init__(self, player1: Player, player2: Player, points) -> None:
        self.player1 = player1
        self.player2 = player2
        self.points = points


def read_input(path):
    with open(path, "r") as f:
        line = f.readline()
        words = line.split('        ')
        player_1 = Player(words[0].strip(), [move.strip() for move in words[1:]])
        line = f.readline()
        words = line.split('        ')
        player_2 = Player(words[0].strip(), [move.strip() for move in words[1:]])
        line = f.readline()
        points_matrix = []
        while line:
            words = line.split('        ')
            points = []
            for move in words:
                points.append((int(move.split('/')[0].strip()), int(move.split('/')[1].strip())))
            points_matrix.append(points)
            line = f.readline()

        game = Game(player_1, player_2, points_matrix)

    return game


def compute_best_response(game: Game):
    best_responses = {}
    for i in range(len(game.player2.moves)):
        best_outcome = max([game.points[j][i][0] for j in range(len(game.player1.moves))])
        best_responses[game.player2.moves[i]] = [game.player1.moves[j] for j in range(len(game.player1.moves)) if
                                                 game.points[j][i][0] == best_outcome]
        best_outcome = max([game.points[i][j][1] for j in range(len(game.player2.moves))])
        best_responses[game.player1.moves[i]] = [game.player2.moves[j] for j in range(len(game.player2.moves)) if
                                                 game.points[i][j][1] == best_outcome]
    return best_responses


def compute_nash_eq(game: Game):
    best_responses = compute_best_response(game)
    for move in game.player1.moves:
        for i in range(len(best_responses[move])):
            if move in best_responses[best_responses[move][i]]:
                print(f"({move}, {best_responses[move][i]})")


def compute_dominant_strat(game: Game):
    best_responses = compute_best_response(game)
    for move in game.player1.moves:
        dominant = True
        for opp_move in game.player2.moves:
            if move not in best_responses[opp_move]:
                dominant = False
                break
        if dominant:
            print(f"{move} is a dominant strategy for {game.player1.name}")
    for move in game.player2.moves:
        dominant = True
        for opp_move in game.player1.moves:
            if move not in best_responses[opp_move]:
                dominant = False
                break
        if dominant:
            print(f"{move} is a dominant strategy for {game.player2.name}")


game = read_input("game1.txt")
compute_nash_eq(game)
compute_dominant_strat(game)
