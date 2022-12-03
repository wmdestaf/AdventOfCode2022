mat = [
    ['A','B','C'],
    ['X','Y','Z']
]
fn = '2_input.txt'

def calculate_win(play):
    index_p1 = mat[0].index(play[0])
    index_p2 = mat[1].index(play[1])
    
    score = index_p2 + 1 #selected shape
    
    if (index_p1 + 1) % 3 == index_p2: #won
        score += 6
    elif (index_p2 + 1) % 3 == index_p1: #lost
        score += 0
    else:
        score += 3
    return score

with open(fn, 'r') as f:
    plays = [line.split(' ') for line in f.read().split('\n')]
    
    for play in plays:
        print(calculate_win(play))
        
    print(sum(calculate_win(play) for play in plays))