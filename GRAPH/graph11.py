import sys

class Graph:
    class _vertex:
        def __init__(self,node):
            self.vid = node
            self.adj = {}
        
        def n_present(self,node):
            return node in self.adj
        
        def add_n(self,node,wt=0):
            if not self.n_present(node):
                self.adj[node] = wt
        
        def neigs(self):
            return list(self.adj.keys())
        
        def edge_cost(self,node):
            if self.n_present(node):
                return self.adj[node]
            else:
                return sys.maxsize
        
    def __init__(self):
        self.vcount = 0
        self.alist = {}
    
    def isEmpty(self):
        return self.vcount == 0
    
    def get_vcount(self):
        return self.vcount
    
    def add_v(self,node):
        if not node in self.alist:
            nn = self._vertex(node)
            self.alist[node] = nn
            self.vcount += 1
    
    def add_edge(self,frm,to,wt = 0):
        if not frm in self.alist:
            self.add_v(frm)
        if not to in self.alist:
            self.add_v(to)
        
        self.alist[frm].add_n(to,wt)
        #self.alist[to].add_n(frm,wt)
    
    def get_vertices(self,node):
        if not self.isEmpty():
            return list(self.alist.keys())
        
    def get_adj_vertices(self,node):
        if node in self.alist:
            return (self.alist[node].neigs())
    
    def get_edj_cost(self,frm,to):
        if frm in self.alist and to in self.alist:
            return (self.alist[frm].edge_cost(to))
    
    def find_path(self,start,end,path = []):
        path = path + [start]
        if start == end:
            return path
        if not start in self.alist:
            return None
        nlist = self.get_adj_vertices(start)
        for node in nlist:
            if node not in path:
                npath = self.find_path(node,end,path)
                if npath:
                    return npath
        return None

def main():
    G1 = Graph()
    G1.add_edge('A','B',2000)
    G1.add_edge('B','C',1500)
    G1.add_edge('B','E',3500)
    G1.add_edge('C','D',750)
    G1.add_edge('D','A',4100)
    G1.add_edge('D','B',2500)
    G1.add_edge('E','B',3000)
    #G1.add_edge('A','B',10)
    print(G1.find_path('A','B'))


if __name__ == "__main__":
    main()