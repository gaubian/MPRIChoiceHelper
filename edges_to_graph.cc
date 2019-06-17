#include <bits/stdc++.h>

using namespace std;

int main() {
    string s, t;
    set<pair<string,string>> edges;
    set<string> vertices;
    while(cin >> s >> t) {
	edges.insert(make_pair(s,t));
	vertices.insert(s);
	vertices.insert(t);
    }
    cout << "graph G {\n";
    for(string u : vertices)
	cout << "\t\"" << u << "\";\n";
    for(auto e : edges)
	cout << "\t\"" << e.first << "\" -- \""
	     << e.second << "\";\n";
    cout << "}";
}
