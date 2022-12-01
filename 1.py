fn = '1_input.txt'
with open(fn, 'r') as f:
    lines_grouped = f.read().split('\n\n')
    cals = [sum(int(x) for x in lines.split('\n')) for lines in lines_grouped]
    print(max(cals))
    
print(sum(sorted(cals)[-3:]))