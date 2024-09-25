"""coordinates"""

__author__ = "730667690"


def get_coords(xs: str, ys: str) -> None:
    """print formatted pairs of each character from both strings"""
    index1: int = 0
    index2: int = 0
    coord: str = "("
    while index1 < len(xs):
        coord += xs[index1] + ","
        while index2 < len(ys):
            coord = "(" + xs[index1] + ","
            coord += ys[index2] + ")"
            print(coord)
            index2 += 1
        index1 += 1
        index2 = 0


if __name__ == "__main__":
    get_coords(xs="hi", ys="bye")
