n = int(input())
faces = 0
for _ in range(n):
    poly = input()
    if poly == "Tetrahedron":
        faces += 4
    elif poly == "Cube":
        faces += 6
    elif poly == "Octahedron":
        faces += 8
    elif poly == "Dodecahedron":
        faces += 12
    else:
        faces += 20
print(faces)