import requests

def remove_comments(s):
    l = s.find("<!--")
    if l == -1:
        return s
    r = s.find("-->", l)
    if r == -1:
        return s
    return remove_comments(s[0:l] + s[r+3:])


def test_useless(c):
    return c.isspace() or c in ",.()\"<>"

def find_inside(needle, ny, haystack):
    if haystack.find(ny) > -1:
        return True
    for x in range(len(haystack) - len(needle)):
        b = True
        for y in range(len(needle)):
            if needle[y] != haystack[x+y]:
                b = False
                break
        if b and test_useless(haystack[x + len(needle)]) and test_useless(haystack[x-1]):
            return True
    return False

def main():
    to_print_on = open('output/pre_edges.txt', 'w+')
    f = open('input/courses.txt')
    ttab = f.read().split('\n')
    ttab.pop()
    name = [(t.split('\t'))[1].strip() for t in ttab]
    tab = [(t.split('\t'))[0].strip() for t in ttab]
    se = set()
    for xi in range(len(tab)):
        x = tab[xi]
        rr = requests.get('http://wikimpri.dptinfo.ens-cachan.fr/doku.php?id=cours:c-' + x.replace('.','-'), verify=False)
        r = remove_comments(rr.text)
        for yi in range(len(tab)):
            y = tab[yi]
            if find_inside(y,name[yi],r) or find_inside(y.replace('.','-'),name[yi],r):
                se.add((min(x,y),max(x,y)))
    for (x,y) in se:
        if x != y:
            to_print_on.write(x + ' ' + y + '\n')
    to_print_on.flush()
