import requests

def find_inside(needle, haystack):
    for x in range(len(haystack) - len(needle)):
        b = True
        for y in range(len(needle)):
            if needle[y] != haystack[x+y]:
                b = False
                break
        if b and not haystack[x + len(needle)].isdigit():
            return True
    return False

def main():
    f = open('ind.txt')
    tab = f.read().split('\n')
    tab.pop()
    se = set()
    for x in tab:
        rr = requests.get('http://wikimpri.dptinfo.ens-cachan.fr/doku.php?id=cours:c-' + x.replace('.','-'), verify=False)
        r = rr.text
        for y in tab:
            if find_inside(y,r) or find_inside(y.replace('.','-'),r):
                se.add((min(x,y),max(x,y)))
    for (x,y) in se:
        if x != y:
            print(x + ' ' + y)

main()
