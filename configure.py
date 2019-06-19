from src import grpher, fix_edges, edges_to_grph, edges_to_js
import os

def main():
    grpher.main()
    fix_edges.main()
    edges_to_grph.main()
    edges_to_js.main()
    os.system('dot -Tjpg -ooutput/grph.jpg output/grph.dot')

main()
