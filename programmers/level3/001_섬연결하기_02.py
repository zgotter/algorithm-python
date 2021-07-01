# 성공
# 복습
# 최소 신장 트리 (MST) 탐색 알고리즘
# 프림 알고리즘 (Prim's Algorithm) 사용
# 힙(Heap) 사용 (heapq)
# defaultdict 사용

from collections import defaultdict
from heapq import heappush, heappop, heapify

def prim(s_node, graph):
    mst = list()
    
    adj_edges = defaultdict(list)
    for n1, n2, w in graph:
        n1, n2 = str(n1), str(n2)
        adj_edges[n1].append((w, n1, n2))
        adj_edges[n2].append((w, n2, n1))
    conn_nodes = set(s_node)
    candidate_edge_list = adj_edges[s_node]
    heapify(candidate_edge_list)
    while candidate_edge_list:
        w, n1, n2 = heappop(candidate_edge_list)
        if n2 not in conn_nodes:
            conn_nodes.add(n2)
            mst.append((w, n1, n2))
            for edge in adj_edges[n2]:
                if edge[2] not in conn_nodes:
                    heappush(candidate_edge_list, edge)
    return mst

def solution(n, costs):
    mst = prim('0', costs)
    return sum([w for w, n1, n2 in mst])