# 성공
# 최단경로 찾기 문제 (다익스트라 알고리즘, dijkstra algorithm)
# 복습

import heapq

def set_graph(graph, a, b, c):
    if b in graph[a].keys():
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c
    return graph

def dijkstra(graph, s_node):
    distances = {node: float('inf') for node in graph.keys()}
    distances[s_node] = 0
    queue = []
    heapq.heappush(queue, [distances[s_node], s_node])
    while queue:
        now_dist, now_node = heapq.heappop(queue)
        if distances[now_node] < now_dist:
            continue
        for nxt_node, weight in graph[now_node].items():
            new_dist = now_dist + weight
            if distances[nxt_node] > new_dist:
                distances[nxt_node] = new_dist
                heapq.heappush(queue, [new_dist, nxt_node])
    return distances

def solution(N, road, K):
    graph = {(i+1): dict() for i in range(N)}
    for a, b, c in road:
        graph = set_graph(graph, a, b, c)
        graph = set_graph(graph, b, a, c)
    distances = dijkstra(graph, 1)
    ans = [node for node, dist in distances.items() if dist <= K]
    return len(ans)