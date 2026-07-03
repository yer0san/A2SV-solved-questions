# permutation
permutation = []
k = 3
n = 4
def backtrack(comb):
    # if len(comb) == k:
    permutation.append(comb[:])
        # return
    
    for cc in range(1, n+1):
        if cc in comb:
            continue
        comb.append(cc)
        backtrack(comb)
        comb.pop()

backtrack([])
print(permutation, len(permutation))