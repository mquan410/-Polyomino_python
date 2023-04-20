from coordinate import Coordinate

# add color to piece
class Piece:
    # offsetValues is a list of coordinates
    def __init__(self, *args):
        self.offsetValues = []

        if len(args) % 2 != 0:
            raise Exception("Invalid number of arguments")

        self.initPiece(args)

    def initPiece(self, args):
        coordinateIPlaceholder = 0
        isIFlag = True
        for element in args:
            if isIFlag:
                isIFlag = False
                coordinateIPlaceholder = element
            else:
                isIFlag = True
                self.offsetValues.append(Coordinate(coordinateIPlaceholder, element))

    def addOffset(self, offset):
        self.offsetValues.append(offset)

    def rotateRight(self):
        for offset in self.offsetValues:
            offset.i, offset.j = -offset.j, offset.i

    def rotateLeft(self):
        for offset in self.offsetValues:
            offset.i, offset.j = offset.j, -offset.i

    def flipVertically(self):
        for offset in self.offsetValues:
            offset.j = -offset.j

    def flipHorizontally(self):
        for offset in self.offsetValues:
            offset.i = -offset.i
