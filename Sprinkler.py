from FarmGadget import FarmGadget


class Sprinkler(FarmGadget):

    neighbouringTiles = []

    def __init__(self, farmBoard, farmTile, main):
        super().__init__(farmBoard, farmTile, main)

    def gadgetInitiate(self):

        boardDimensions = self.farmBoard.getGridSize()
        boardX = boardDimensions[0]
        boardY = boardDimensions[1]

        tileIndexes = self.farmTile.getGridIndexes()
        tileX = tileIndexes[0]
        tileY = tileIndexes[1]

        #Set 3 tiles on the left
        if(tileX > 0 and tileY > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX -1, tileY -1])
        if(tileX > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX -1, tileY])
        if(tileX > 0 and tileY < boardY):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX -1, tileY +1])

        #Set tiles above and below
        if(tileY > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX, tileY -1])
        if(tileY < boardY):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX, tileY +1])

        #Set 3 tiles to the right
        if(tileX < boardX and tileY > 0):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX +1, tileY -1])
        if(tileX < boardX):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX +1, tileY])
        if(tileX < boardX and tileY < boardY):
            self.neighbouringTiles.append(self.farmBoard.grid[tileX +1, tileY +1])

    def gadgetShutdown(self):
        pass #Delet this

    def gadgetActivate(self):
        self.waterTiles()

    def waterTiles(self):
        for tile in self.neighbouringTiles:
            if not tile.isWatered and not tile.isGrown:
                tile.isWatered = True
