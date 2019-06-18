g++ -O3 keep.cc
python3 grpher.py > pre_edges.txt
python3 fix_edges.py > edges.txt 
python3 edges_to_grph.py > grph.dot
dot -Tjpg -ogrph.jpg grph.dot
