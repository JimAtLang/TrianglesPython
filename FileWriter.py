from random import shuffle
from typing import List
from TriangleSides import TriangleSides


def draw_triangles(triangles:List[TriangleSides], filename:str):
    with open(filename,'w') as file:
        for triangle in triangles:
            sides: List[int] = [triangle.short, triangle.middle, triangle.long]
            shuffle(sides)
            file.write(f"{sides[0]},{sides[1]},{sides[2]}\n")