
from pieceLibrary import pieceLibrary
from board import Board


class Solver:
    def __init__(self, board: Board):
        self.visitedBoardState = {}
        self.board = board
        self.library = pieceLibrary
        self.isComplete = False

    def solve(self):
        if len(self.library) ==0:
            return False
        if self.isBoardComplete():
            return True

        self.board.print()
        library_iter = iter(self.library)
            
        pieceName = next(library_iter)

        for i in range(self.board.bitboard.sizeI):
            for j in range(self.board.bitboard.sizeJ):
                if self.tryPlacePieceAt(pieceName, i, j, self.visitedBoardState):
                    return True
        return False

    def tryPlacePieceAt(self, pieceName, i, j, visited):
        piece = self.library[pieceName]
        boardHashcode = self.board.getBoardHashcode()
        if self.board.placePiece(piece, i, j, pieceName) and not boardHashcode in visited:
            self.extractUsedPieceFromLibrary(pieceName, visited, boardHashcode)
            if self.solve():
                return True
            self.returnExtractedPieceBack(pieceName, i, j, visited, piece, boardHashcode)
        return False


    def isBoardComplete(self):
        if self.board.isComplete():
            self.isComplete = True
            self.board.print()
            return True
        return False

    def returnExtractedPieceBack(self, pieceName, i, j, visited, piece, boardHashCode):
        self.library[pieceName] = piece
        self.board.removePiece(piece, i, j, pieceName)
        visited.pop(boardHashCode)

    def extractUsedPieceFromLibrary(self, pieceName, visited, boardHashcode):
        visited[boardHashcode] = pieceName
        self.library.pop(pieceName)


    def isSolved(self):
        return self.isComplete
