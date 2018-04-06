class Directions:
  NORTH = 'North'
  SOUTH = 'South'
  EAST = 'East'
  WEST = 'West'
  NORTHEAST = 'Northeast'
  NORTHWEST = 'Northwest'
  SOUTHEAST = 'Southeast'
  SOUTHWEST = 'Southwest'
  #
  # Reverse = {NORTH = SOUTH,
  #           SOUTH = NORTH,
  #           EAST = WEST,
  #           WEST = EAST,
  #           NORTHEAST = SOUTHWEST,
  #           NORTHWEST = SOUTHEAST,
  #           SOUTHEAST = NORTHWEST,
  #           SOUTHWEST = NOTHEAST}

class Configuration:
    """
    holds the x, y coordinates of a piece with its traveling direction
    """

    def __init__(self, pos, direction):
        self.pos = points
        self.direction = direction

    def getPosition(self):
        return (self.pos)

    def getDirection(self):
        return (self.direction)

    def coordinates(self):
        x, y = self.points
        return x == int(x) and y == int(y)

class Grid:
    """
    A 2-dimensional array of objects backed by a list of lists
    Access through grid[x][y] where (x, y) are the positions on
    the game board.
    4 x 3
    """
    def __init__(self):
        self.width = 3;
        self.height = 4;
        self.matrix = [[0 for x in range(width)] for y in range(height)] #set everything to 0

class Actions:
    _directions = {Directions.NORTH: (0, 1),
                   Directions.SOUTH: (0, -1),
                   Directions.EAST:  (1, 0),
                   Directions.WEST:  (-1, 0),
                   Directions.NORTHEAST: (1, 1),
                   Directions.NORTHWEST: (-1, 1),
                   Directions.SOUTHEAST: (1, -1),
                   Directions.SOUTHWEST: (-1, -1)}

    _
