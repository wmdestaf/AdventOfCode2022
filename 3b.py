fn = '3_input.txt'

def priority(ch):
    o = ord(ch)
    if o >= ord('a') and o <= ord('z'):
        return o - ord('a') + 1
    elif o >= ord('A') and o <= ord('Z'):
        return o - ord('A') + 27

with open(fn, 'r') as f:
    rucksacks = [line for line in f.read().split('\n')]
    groups = [
        rucksacks[3 * i:(3 * i) + 3] 
        for i in range(len(rucksacks) // 3)
    ] 
    
    s = 0
    for (r1, r2, r3) in groups:
        shared = iter(
            {ch for ch in r1}.intersection(
                {ch for ch in r2}.intersection(
                    {ch for ch in r3}
                )
            )
        ).__next__()
        s += priority(shared)
        
    print(s)