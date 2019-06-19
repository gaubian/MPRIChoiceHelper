from src import grpher, fix_edges, edges_to_grph
import os

def main():
    grpher.main()
    fix_edges.main()
    edges_to_grph.main()
    os.system('dot -Tjpg -ooutput/grph.jpg output/grph.dot')

main()
