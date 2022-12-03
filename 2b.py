mat = [
    ['A','B','C'],
    ['X','Y','Z']
]
fn = '2_input.txt'

def calculate_win(play):
    index_p1 = mat[0].index(play[0])
    index_p2 = mat[1].index(play[1])
    
    score = index_p2 * 3 #win or lose

    #figure out the matching piece
    index_p2 -= 1 #encode lose = -1, tie = 0, win = 1
    piece_value = (index_p1 + index_p2) % 3
    piece_value += 1 #rock = 1, not 0

    return score + piece_value

with open(fn, 'r') as f:
    plays = [line.split(' ') for line in f.read().split('\n')]
    
    for play in plays:
        calculate_win(play)
    
    print(sum(calculate_win(play) for play in plays))