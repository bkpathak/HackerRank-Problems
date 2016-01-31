def is_valid(queen_conf,col):
    for c in range(col):
        if queen_conf[c] == queen_conf[col]: return False
        if queen_conf[c] - queen_conf[col] == col - c: return False
        if queen_conf[col] - queen_conf[c] == col - c: return False
    return True

def solve(queen_conf,col):
    if(col == len(queen_conf)):
        print([r + 1 for r in queen_conf])
    else:
        for row in range(len(queen_conf)):
            queen_conf[col] = row
            if(is_valid(queen_conf,col)):
                solve(queen_conf,col + 1 )

def solve_n_queen(n):
    solve([0]*n,0)

for i in range(10):
    print("Solution for {} queen : ".format( i + 1))
    solve_n_queen(i+1)
