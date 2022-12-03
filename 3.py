fn = '3_input.txt'

def priority(ch):
    o = ord(ch)
    if o >= ord('a') and o <= ord('z'):
        return o - ord('a') + 1
    elif o >= ord('A') and o <= ord('Z'):
        return o - ord('A') + 27

with open(fn, 'r') as f:
    rucksacks = [
        (line[:len(line) // 2], line[len(line) // 2:])
        for line in f.read().split('\n')
    ]
    
    s = 0
    for (comp1, comp2) in rucksacks:
        comp1_s = {ch for ch in comp1}
        comp2_s = {ch for ch in comp2}
        shared = iter(comp1_s.intersection(comp2_s)).__next__()
        s += priority(shared)
        
    print(s)