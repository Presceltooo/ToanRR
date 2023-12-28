import sys
from heapq import heappush, heappop

def min_cut_phase(n, graph, used, weights, nodes):
    heap = []
    u = next(i for i in range(n) if not used[i])
    used[u] = True

    for _ in range(n):
        v = -1
        while heap:
            _, w, v = heappop(heap)
            if not used[v]:
                break
        if v == -1:
            break

        if _ == n - 1:
            for i, w in enumerate(graph[u]):
                weights[i] -= w
            for i, w in enumerate(graph[v]):
                weights[i] += w
            graph[u] = [i - j for i, j in zip(graph[u], graph[v])]
            graph[v] = graph[u]
            return nodes.pop(v), min(weights)
        else:
            used[v] = True
            for to, w in enumerate(graph[v]):
                if not used[to] and w:
                    heappush(heap, (-w, w, to))
            u = v

def stoer_wagner(n, graph):
    nodes = list(range(n))
    used = [False] * n
    weights = [0] * n
    cut_weight = float('inf')

    while n > 1:
        node, weight = min_cut_phase(n, graph, used, weights, nodes)
        cut_weight = min(cut_weight, weight)
        n -= 1
    return cut_weight
graph = [[0, 1, 2, 0, 0],
         [1, 0, 3, 4, 0],
         [2, 3, 0, 5, 0],
         [0, 4, 5, 0, 6],
         [0, 0, 0, 6, 0]]
n = len(graph)

print("The minimum cut of the graph is %d" % stoer_wagner(n, graph))
