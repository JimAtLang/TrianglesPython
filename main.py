from TriangleSides import TriangleSides
triangles = []
with open("triangles.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.split(",")
        sides = []
        for part in parts:
            side = int(part)
            sides.append(side)
        sides.sort()
        triangles.append(TriangleSides(sides[0], sides[1], sides[2]))
for triangle in triangles:
    print(triangle.short, triangle.middle, triangle.long)