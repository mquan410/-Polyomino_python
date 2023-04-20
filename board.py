from typing import Tuple

from bitboard import BitboardManager
from coordinate import Coordinate


class Board:
    def __init__(self, width, height):
        self.boardID = '#'
        self.pieceOffset = {}
        self.bitboard = BitboardManager()
        self.bitboard.buildBitboard(self.boardID, height, width)

    def addOffsetToPosition(self, i, j, offset: Coordinate):
        return Coordinate(i + offset.i, j + offset.j)

    def isCollided(self, i, j):
        return self.bitboard.isPieceSet(self.boardID, i, j)

    def isValidPlacement(self, piece, i, j):
        for offset in piece.offsetValues:
            piecePosition = self.addOffsetToPosition(i, j, offset)
            if not self.bitboard.isInBound(piecePosition.i, piecePosition.j):
                return False
            if self.isCollided(i, j):
                return False
        return True

    def placePiece(self, piece, i, j, pieceName):
        if not self.isValidPlacement(piece,i,j):
            return False
        self.setBitInBoard(piece, i,j, pieceName)
        return True

    def setBitInBoard(self, piece, i ,j, pieceName):
        for offset in piece.offsetValues:
            piecePosition = self.addOffsetToPosition(i, j, offset)
            self.bitboard.setPiece(self.boardID, piecePosition.i, piecePosition.j)
            self.pieceOffset[pieceName] = piecePosition
    def getBoardHashcode(self):
        return self.bitboard[self.boardID].data

    def print(self):
        sb = ""
        for y in range(self.bitboard.sizeI):
            for x in range(self.bitboard.sizeJ):
                # index = y * self.bitboard.sizeJ + x
                sb += "#" if self.bitboard.isPieceSet('#', y, x) else "_"
            sb += "\n"
        print(sb)

    def isComplete(self):
        if self.bitboard.isAllBitsSet(self.boardID):
            return True

    def removePiece(self, piece, i, j, pieceName):
        self.clearBitInBoard(piece, i, j)
        self.pieceOffset.pop(pieceName)

    def clearBitInBoard(self, piece, i, j):
        for offset in piece.offsetValues:
            offsetCoord = self.addOffsetToPosition(i, j, offset)
            self.bitboard.deletePiece(self.boardID, offsetCoord.i, offsetCoord.j)
