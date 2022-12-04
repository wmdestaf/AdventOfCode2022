fn = '4_input.txt'

def encloses(pair):
    (lb_0, ub_0), (lb_1, ub_1) = pair
    if lb_0 <= lb_1 and ub_1 <= ub_0:
        return 1
    elif lb_1 <= lb_0 and ub_0 <= ub_1:
        return 1
    return 0

def overlaps(pair):
    (lb_0, ub_0), (lb_1, ub_1) = pair
    if lb_0 <= lb_1 and lb_1 <= ub_0:
        return 1    
    elif lb_1 <= lb_0 and lb_0 <= ub_1:
        return 1
    return 0

with open(fn, 'r') as f:
    pairs = [
        [
            [int(x) for x in line.split(',')[0].split('-')],
            [int(x) for x in line.split(',')[1].split('-')]
        ]
        for line in f.read().split('\n')
    ]
    
    print(sum(encloses(pair) for pair in pairs))
    print(sum(overlaps(pair) for pair in pairs))