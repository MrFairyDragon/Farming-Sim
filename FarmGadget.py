import abc
from GameObject import GameObject


class FarmGadget(GameObject):

    def __init__(self, gridPosX, gridPosY, main, farmBoard, farmTile):
        super().__init__(gridPosX, gridPosY, main)
        self.main = main
        self.farmBoard = farmBoard
        self.farmTile = farmTile

    @abc.abstractmethod
    def gadgetActivate(self):
        pass

    @abc.abstractmethod
    def gadgetInitiate(self):
        pass

    @abc.abstractmethod
    def gadgetShutdown(self):
        pass