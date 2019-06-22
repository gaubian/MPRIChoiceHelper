def find_codes_names():
    f = open('input/courses.txt')
    ttab = f.read().split('\n')
    ttab.pop()
    codes = [(t.split('\t'))[0].strip() for t in ttab]
    names = [(t.split('\t'))[1].strip() for t in ttab]
    nb_ects = [(t.split('\t'))[2].strip() for t in ttab]
    return (codes, names, nb_ects)

def main():
    with open('input/original.js', 'r+') as original: data = original.read()
    to_print_on = open('output/script.js','w+')
    edges_f = open('output/edges.txt')
    tab = edges_f.read().split('\n')
    tab.pop()
    edges = set()
    for e in tab:
        [s, t] = e.split()
        edges.add((s,t))
    (codes, names, nb_ects) = find_codes_names()
    to_print_on.write('const codes =[\n');
    for code in codes:
        to_print_on.write(' "' + code + '",')
    to_print_on.write('];\n')
    to_print_on.write('const names =[\n');
    for name in names:
        to_print_on.write(' "' + name + '",')
    to_print_on.write('];\n')
    to_print_on.write('const nb_ects =[\n');
    for ects in nb_ects:
        to_print_on.write(' ' + ects + ',')
    to_print_on.write('];\n')
    to_print_on.write('const edges = [\n')
    for (u,v) in edges:
        to_print_on.write(' [' + str(codes.index(u)) + ', ' + str(codes.index(v)) + '],')
    to_print_on.write('];\n')
    to_print_on.write(data)
    to_print_on.flush()
