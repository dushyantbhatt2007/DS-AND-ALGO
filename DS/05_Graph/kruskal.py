import DS.Graph.priority_dict as priority_dict

from DS.Graph.graph import *


def spanning_tree(graph):
    priority_queue = priority_dict.priority_dict()

    for v in range(graph.num_vertices):
        for neighbour in graph.get_adjacent_vertices(v):
            priority_queue[(v, neighbour)] = graph.get_edge_weight(v, neighbour)

    visited_vertices = set()

    spanning_tree = {}

    for v in range(graph.num_vertices):
        spanning_tree[v] = set()

    num_edges = 0

    while len(priority_queue.keys()) > 0 and num_edges < graph.num_vertices - 1:
        v1, v2 = priority_queue.pop_smallest()

        if v1 in spanning_tree[v2]:
            continue

        vertex_pair = sorted([v1, v2])

        spanning_tree[vertex_pair[0]].add(vertex_pair[1])

        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue

        num_edges = num_edges + 1

        visited_vertices.add(v1)
        visited_vertices.add(v2)

    print("Visited vertices: ", visited_vertices)

    if len(visited_vertices) != graph.num_vertices:
        print("Minimum spanning tree not found")
    else:
        print("Mininum spanning tree:")
        for key in spanning_tree:
            for value in spanning_tree[key]:
                print(key, "-->", value)


def has_cycle(spanning_tree):
    for source in spanning_tree:
        q = []
        q.append(source)

        visited_vertices = set()

        while len(q) > 0:
            vertex = q.pop(0)

            if vertex in visited_vertices:
                return True

            visited_vertices.add(vertex)

            q.extend(spanning_tree[vertex])

    return False


g = AdjacencyMatrixGraph(8, directed=False)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 2)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)

spanning_tree(g)
