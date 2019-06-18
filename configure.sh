g++ -O3 keep.cc
./a.out < courses.txt > ind.txt
python3 grpher.py > pre_edges.txt
python3 fix_edges.py > edges.txt 
g++ -O3 edges_to_graph.cc
./a.out < edges.txt > grph.dot
dot -Tjpg -ogrph.jpg grph.dot
