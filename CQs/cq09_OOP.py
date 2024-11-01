# Point class from previous lesson: Line class assumes there is a defined Point class
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        """calculates length of line"""
        return (
            ((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)
        ) ** 0.5
