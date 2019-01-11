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
        
        def get_nn(self):
            min = ('',sys.maxsize)
            #print(min[1])
            for k,v in self.adj.items():
                #print(k,v)
                if min[1] > v:
                    min = k,v
                    #print(min)
            return min
                
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
        self.alist[to].add_n(frm,wt)
    
    def get_vertices(self):
        if not self.isEmpty():
            return list(self.alist.keys())
        
    def get_adj_vertices(self,node):
        if node in self.alist:
            return (self.alist[node].neigs())
    
    def get_edj_cost(self,frm,to):
        if frm in self.alist and to in self.alist:
            return (self.alist[frm].edge_cost(to))
        else:
            return "not entering if loop"
    
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
    
    def get_max_edge(self):
        max = ('','',0)
        for vertex in self.get_vertices():
            for node in self.get_vertices():
                #print(vertex,'--',node)
                #print(self.get_edj_cost(vertex,node))
                if max[2] < self.get_edj_cost(vertex,node) and self.get_edj_cost(vertex,node) != sys.maxsize :
                    max = (vertex,node,self.get_edj_cost(vertex,node))
        return max



def main():
    G1 = Graph()
    G1.add_edge('0','1',30)
    G1.add_edge('0','2',25)
    G1.add_edge('1','3',10)
    G1.add_edge('1','4',40)
    G1.add_edge('1','5',5)
    G1.add_edge('2','6',30)
    G1.add_edge('4','7',53)
    G1.add_edge('5','7',87)
    G1.add_edge('6','7',5)
    #G1.add_edge('A','B',10)
    print(G1.find_path('0','1'))

    ##sub ques 1 :1.	Compute the neighbours of each node.
    print("-- Neighbours of each node")
    for k,v in G1.alist.items():
        print(k,"-->>",v.neigs())

    ## 2.	Find the nearest neighbour of each node.
    print("-- Nearest Neighbours of each node")
    for k,v in G1.alist.items():
        print(k,"-->>",v.get_nn())
    
    ##3.	Find the node which has more neighbours.
    print("-- Node with max Neighbours")
    max_n = ('',0)
    for k,v in G1.alist.items():
        if max_n[1] < len(v.neigs()):
            max_n = (k,len(v.neigs()))
    print(max_n[0],"-->>",max_n[1])

    ##4.	Find the edge whose cost is maximum (give source and destination node).
    print("-- Max Edge")
    print(G1.get_max_edge())

if __name__ == "__main__":
    main()