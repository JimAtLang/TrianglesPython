from math import floor
from random import randint
from typing import List
from TriangleSides import TriangleSides


def get_triangles_by_side(count:int,min_side:int, max_side:int)->List[TriangleSides]:
    t = []
    half = int(floor(max_side/2))
    for i in range(count):
        shortest_side = randint(min_side,half-1)
        middle_side = randint(min_side,half-1)
        longest_side = randint(shortest_side + middle_side+1, max_side)
        t.append(TriangleSides(shortest_side,middle_side,longest_side))
    return t