import chess
import chess.pgn

class State(object):
    def __init__(self):
        self.board = chess.Board()
    
    def seralized(self):
        # 257 bits (related to neural network)
        pass

    def edges(self):
        #Board visualization goes here
        return list(self.board.legal_moves)


    def value(self):
        #Nueral net goes here
        return 1 #Drawed game state

if __name__ == "__main__":
    s = State()
    print(s.edges())
