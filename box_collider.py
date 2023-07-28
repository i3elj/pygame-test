class BoxCollider:
    side: int
    pos: (int, int)

    def __init__(self, side: int, pos: (int, int)):
        self.side = side
        self.pos = pos
