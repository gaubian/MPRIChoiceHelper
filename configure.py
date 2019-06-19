import grpher
import edges_to_grph
import fix_edges
import os

def main():
    grpher.main()
    edges_to_grph.main()
    fix_edges.main()
    os.system('dot -Tjpg -ogrph.jpg grph.dot')

main()
