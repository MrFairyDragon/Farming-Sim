import abc

class FarmGadget:

    def __init__(self, farmBoard, farmTile, main):
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