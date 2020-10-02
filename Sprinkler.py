from FarmGadget import FarmGadget


class Sprinkler(FarmGadget):
    neighbouringTiles = []

    def __init__(self, farmBoard, farmTile, main):
        super().__init__(farmBoard, farmTile, main)

    def gadgetInitiate(self):
        self.neighbouringTiles = []
        boardDimensions = self.farmBoard.getGridSize()
        boardX = boardDimensions[0]
        boardY = boardDimensions[1]

        tileIndexes = self.farmTile.getGridIndexes()
        tileX = tileIndexes[0]
        tileY = tileIndexes[1]

        # Set 3 tiles on the left
        if (tileX > 0 and tileY > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX - 1, tileY - 1])
        if (tileX > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX - 1, tileY])
        if (tileX > 0 and tileY < boardY - 1):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX - 1, tileY + 1])

        # Set tiles above and below
        if (tileY > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX, tileY - 1])
        if (tileY < boardY - 1):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX, tileY + 1])

        # Set 3 tiles to the right
        if (tileX < boardX - 1 and tileY > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX + 1, tileY - 1])
        if (tileX < boardX - 1):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX + 1, tileY])
        if (tileX < boardX - 1 and tileY < boardY - 1):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX + 1, tileY + 1])

    def gadgetShutdown(self):
        pass

    def gadgetActivate(self):
        # print(len(self.neighbouringTiles))
        self.waterTiles()

    def waterTiles(self):
        for tile in self.neighbouringTiles:
            if not tile.isWatered and not tile.isGrown and not tile.isOccupied:
                tile.isWatered = True

    def getTileLocation(self):
        return self.farmTile.getGridIndexes()

