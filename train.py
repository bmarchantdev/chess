import os 
import chess.pgn
from state import State

def get_dataset():
    X,Y = [], []
    gn = 0
    #pgn in data folder
    for fn in os.listdir("data"):
        pgn = open(os.path.join("data", fn))
        while 1:
            
            try:
                game = chess.pgn.read_game(pgn)
            except Exception:
                break
            print("Parsing game %d, got %d examples" % (gn, len(X)))
            gn += 1
            value = {'1/2-1/2':0, '0-1':-1, '1-0':1} [game.headers['Result']]
            board = game.board()
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                ser = State(board).serialize()[:, :, 0]
                X.append(ser)
                Y.append(value)
if __name__ == "__main__":
    get_dataset()