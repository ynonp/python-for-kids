from p5 import *
from dataclasses import dataclass

@dataclass
class RightLeftBar:
    x: int
    y: int
    dx: int = 2

    def update(self):
        if self.x  + 80 > width:
            self.dx = -2
    
        if self.x < 0:
            self.dx = 2

        self.x = self.x + self.dx


    def draw(self):
        rect(self.x, 100, 80, 20)


# ------------------------------------------------




bar = RightLeftBar(x=50, y=100)

def setup():
    size(400, 600)


def draw():
    background(0, 0, 0)
    fill(255, 255, 255)
    bar.update()
    bar.draw()


run()
