from Animal import Animal


class Chicken(Animal):
    def __init__(self, gridPosX, gridPosY, main, farmland):
        super().__init__(gridPosX, gridPosY, main, farmland)

    def getTexture(self):
        return 'Chicken'
