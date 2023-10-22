class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

f=open('testcases/input.txt','r')
num_nodes,num_edges = map(int,f.readline().split())
g = Graph()
for i in range(1,12):
    g.add_vertex(i)
for i in range(0,num_edges):
    n1,n2 = map(int,f.readline().split())
    g.add_edge(n1,n2)
for v in g:
    print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
num_impassable = int(f.readline().split()[0])
impassables=[]
for i in range(0,num_impassable):
    impassables.append(int(f.readline().split()[i]))
num_morid = int(f.readline().split()[0])
morids={}
for i in range(0,num_morid):
    line = f.readline().split()
    morids[int(line[0])] = list(map(int, line[2:]))

seyed = int(f.readline().split()[0])