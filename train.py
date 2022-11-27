import os 
import chess

for fn in os.listdir("data"):
    pgn = open(os.path.join("data", fn))
    while 1:
        try:
          game = chess.pgn.read_game(pgn)
        except Exception:
            break
        print(game)