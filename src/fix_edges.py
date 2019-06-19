def parse(filename):
    f = open(filename)
    tab = f.read().split('\n')
    tab.pop()
    return [x.split() for x in tab]

def main():
    f = open('output/edges.txt','w+')
    edges = parse("output/pre_edges.txt")
    to_mod = parse("input/to_modify.txt")
    to_add = set()
    to_rem = set()
    for [sg, u, v] in to_mod:
        if sg == '+':
            to_add.add((min(u,v), max(u,v)))
        else:
            to_rem.add((min(u,v), max(u,v)))
    ans = (to_add | set([(u,v) for [u,v] in edges])) - to_rem
    for (x,y) in ans:
        f.write(x + ' ' + y + '\n')
    f.flush()
