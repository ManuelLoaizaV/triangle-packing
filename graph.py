class Graph:
    def __init__(self, n_vertices):
        self._vertices = set([v for v in range(n_vertices)])
        self._edges = set()

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def add_edge(self, u, v):
        edge = (min(u, v), max(u, v))
        self._edges.add(edge)

    def list_triangles(self):
        triangles = []
        for u in self._vertices:
            for v in self._vertices:
                if v <= u or (u, v) not in self._edges:
                    continue
                for w in self._vertices:
                    if w <= v or (v, w) not in self._edges:
                        continue
                    if (u, w) in self._edges:
                        triangles.append((u, v, w))
        return triangles
