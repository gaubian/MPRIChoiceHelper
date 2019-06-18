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
    return c.isspace() or c in ",.()\"-<>"

def find_inside(needle, haystack):
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
    f = open('ind.txt')
    tab = f.read().split('\n')
    tab.pop()
    se = set()
    for x in tab:
        rr = requests.get('http://wikimpri.dptinfo.ens-cachan.fr/doku.php?id=cours:c-' + x.replace('.','-'), verify=False)
        r = remove_comments(rr.text)
        for y in tab:
            if find_inside(y,r) or find_inside(y.replace('.','-'),r):
                se.add((min(x,y),max(x,y)))
    for (x,y) in se:
        if x != y:
            print(x + ' ' + y)

main()
