import chess
import numpy as np

class State(object):
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
    
    def serialize(self):
        assert self.board.is_valid()

        bstate = np.zeros(64, np.uint8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
               bstate[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                            "p": 9, "n": 10, "b": 11, "r": 12, "q": 13, "k": 14}[pp.symbol()]

        if self.board.has_queenside_castling_rights(chess.WHITE):
            assert bstate[0] == 4
            bstate[0] = 7
        if self.board.has_kingside_castling_rights(chess.WHITE):
            assert bstate[7] == 4
            bstate[7] = 7
        if self.board.has_queenside_castling_rights(chess.BLACK):
            assert bstate[56] == 8+4
            bstate[56] = 8+7
        if self.board.has_kingside_castling_rights(chess.BLACK):
            assert bstate[63] == 8+4
            bstate[63] = 8+7
        if self.board.ep_square is not None:
            assert bstate[self.board.ep_square] == 0
            bstate[self.board.ep_square] = 8
        bstate = bstate.reshape(8,8)
                
        #binary state
        state = np.zeros((8,8,5), np.uint8)

        # 0-3 columns to binary
        state[:,:,0] = (bstate>>3)&1
        state[:,:,1] = (bstate>>2)&1
        state[:,:,2] = (bstate>>1)&1
        state[:,:,3] = (bstate>>0)&1
                

        #4th column is whos turn
        state[:,:, 4] = (self.board.turn*1.0)

        # 257 bits (related to neural network)
        return state

    def edges(self):
        #Board visualization goes here
        return list(self.board.legal_moves)

    def value(self):
        #Nueral net goes here
        return 0 #Drawed game state

if __name__ == "__main__":
    s = State()
    print(s.edges())
