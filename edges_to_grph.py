def main():
    to_print_on = open('grph.dot','w+')
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
    to_print_on.write('graph G {\n')
    for u in vertices:
        to_print_on.write('\t"' + u + '";\n')
    for (u,v) in edges:
        to_print_on.write('\t"' + u + '" -- "' + v + '";\n')
    to_print_on.write('}\n')
