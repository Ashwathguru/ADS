import sys

class Graph:
	class _vertex:
		def __init__(self,node):
			self.vid = node
			self.adj = {}

		def n_present(self,node):
			return node in self.adj.keys()

		def add_neighbour(self,node,wt = 0):
			if not self.n_present(node):
				self.adj[node] = wt

		def neighbours(self):
			return list(self.adj.keys())

		def get_edge_cost(self,node):
			if self.n_present(node):
				#print(self.adj[node])
				return self.adj[node]
			else:
				return sys.maxsize

	def __init__(self):
		self.vcount = 0
		self.alist = {}

	def add_vertex(self,node):
		if node not in self.alist.keys():
			nn = self._vertex(node)
			self.alist[node] = nn
			self.vcount += 1

	def add_edge(self, frm, to, wt = 0):
		if frm not in self.alist.keys():
			self.add_vertex(frm)
		if to not in self.alist.keys():
			self.add_vertex(to)

		self.alist[frm].add_neighbour(to,wt)
		self.alist[to].add_neighbour(frm,wt)

	def get_vertices(self):
		return list(self.alist.keys())

	def get_neighbours(self,node):
		if node in self.alist.keys():
			return self.alist[node].neighbours()

	def get_edge_cost(self, frm, to):
		return self.alist[frm].get_edge_cost(to)

	def path(self, start, end, path = [], all_path = []):
		path = path + [start]
		if start == end:
			return path
		if not start in self.alist:
			return None
		nlist = self.get_neighbours(start)
		for node in nlist:
			if node not in path:
				npath = self.path(node,end,path,all_path)
				if npath and npath not in all_path:
					all_path.append(npath)
					#print(npath)
					#self.add_path(npath)
					#print(all_path)
			#print("---")
		#print("---->>>")
		#return None
		return all_path

	def add_path(path):
		return path

	def all_path(self,start,end, all_path = []):
		all_path = []

		pass

	def display(self):
		for v in self.alist.values():
			print(v.vid,"-->>",v.adj)

	def get_shortest(self,allp):
		spath = ('',sys.maxsize)
		for path in allp:
			#print(path)
			cost = 0
			for i in range(len(path)-1):
				cost += self.get_edge_cost(path[i],path[i+1])
			if spath[1] > cost:
				spath = (path,cost)
		return(spath)


def main():
	G = Graph()
	G.add_vertex('A')
	G.add_vertex('B')
	G.add_vertex('C')
	G.add_vertex('D')
	G.add_vertex('E')

	G.add_edge('A','B',15)
	G.add_edge('A','D',5)
	G.add_edge('B','C',30)
	G.add_edge('B','E',20)
	G.add_edge('C','D',10)
	G.add_edge('C','E',5)

	G.display()
	all_path = G.path('A','D')
	nall = []
	for x in all_path:
		if type(x[0]) == str:
			nall.append(x)
	print(nall)
	spath = G.get_shortest(nall)
	print("shortest path -->>",spath[0],"\ncost -->>",spath[1])

if __name__ == '__main__':
	main()