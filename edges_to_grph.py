def main():
    f = open('edges.txt')
    tab = f.read().split('\n')
    tab.pop()
    edges = set()
    vertices = set()
    for e in tab:
        [s, t] = e.split()
        vertices.add(s)
        vertices.add(t)
        edges.add((s,t))
    print('graph G {')
    for u in vertices:
        print('\t"' + u + '";')
    for (u,v) in edges:
        print('\t"' + u + '" -- "' + v + '";')
    print('}')

main()
