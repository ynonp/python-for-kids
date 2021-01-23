from p5 import *
from dataclass import dataclass

@dataclass
class Circle:
    x: int
    y: int
    radius: int = 40

    def draw(self):
        circle(self.x, self.y, self.radius)

    def update(self):
        pass


shapes = [Circle(x=10, y=20), Circle(x=50, y=80), Circle(x=10, y=80)]


def setup():
    size(400, 600)


def draw():
    for shape in shapes:
        shape.draw()

    for shape in shapes:
        shape.update()
