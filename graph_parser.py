from graph_types import (
    GraphFamily,
    GraphSubfamily,
    FileExtension
)
from graph import Graph


def parse_interval_graph(file, n_vertices):
    interval_graphs = []
    for line in file:
        interval_graph = Graph(n_vertices)
        tokens = map(lambda t: int(t) - 1, line.split())
        opened_intervals = set()
        for token in tokens:
            if token in opened_intervals:
                opened_intervals.remove(token)
            else:
                for open_interval in opened_intervals:
                    interval_graph.add_edge(token, open_interval)
                opened_intervals.add(token)
        interval_graphs.append(interval_graph)
    return interval_graphs


parsers = {
    GraphFamily.INTERVAL: parse_interval_graph
}


class GraphParser:
    def __init__(
        self,
        family: GraphFamily,
        subfamily: GraphSubfamily,
        n_vertices: int,
        file_extension: FileExtension
    ):
        self._family = family
        self._file_extension = file_extension
        self._n_vertices = n_vertices
        self._subfamily = subfamily

    def build_local_path(self):
        return f"graphs/{self._family.value}/{self._subfamily.value}{self._n_vertices}.{self._file_extension.value}"  # noqa

    def parse(self):
        local_path = self.build_local_path()
        parser = parsers[self._family]
        with open(local_path) as file:
            graphs = parser(file, self._n_vertices)
        return graphs
