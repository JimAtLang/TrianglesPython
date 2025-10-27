from TriangleFactory import *
from FileWriter import *

triangles = get_triangles_by_side(500, 50,1000)
draw_triangles(triangles,"triangles.txt")