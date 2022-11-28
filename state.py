import chess
import numpy as np

class State(object):
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
    
    def serialize(self):
        state = np.zeros((8,8,5))
        state[:,:, 4] = (self.board.turn*1.0)
        print(state)
        # 257 bits (related to neural network)
        pp = self.board.shredder_fen
        return pp

    def edges(self):
        #Board visualization goes here
        return list(self.board.legal_moves)

    def value(self):
        #Nueral net goes here
        return 0 #Drawed game state

if __name__ == "__main__":
    s = State()
    print(s.edges())
