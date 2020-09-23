class Tile:

    def __init__(self, SizeX, SizeY, name):
        self.__SizeX = SizeX
        self.__SizeY = SizeY
        self.name = name


class CarrotTile(Tile):
    def __init__(self):
        self.SizeX = 1
        self.SizeY = 1
        self.Name = 'Carrot'

