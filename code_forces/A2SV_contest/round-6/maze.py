mapp = [
    [0, 1, 1, 1, 1],
    [1, 2, 1, 1, 2],
    [1, 2, 2, 1, 2],
    [2, 1, 1, 1, 3]
]

path = []

def backtrack(cand):
    i, j = cand
    if mapp[i][j] == 2:
        return
    if mapp[i][j] == 3:
        return path
    
    
    

