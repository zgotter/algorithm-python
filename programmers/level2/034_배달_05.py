# 성공
# 최단경로 찾기 문제 (다익스트라 알고리즘, dijkstra algorithm)
# 복습

from heapq import heappush, heappop

graph = {}

def set_graph(a, b, c):
    global graph
    if b in graph[a].keys():
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c

def dijkstra(s_node):
    global graph
    distances = {node: float('inf') for node in graph}
    distances[s_node] = 0
    queue = []
    heappush(queue, [distances[s_node], s_node])
    while queue:
        now_dist, now_node = heappop(queue)
        if distances[now_node] < now_dist:
            continue
        for nxt_node, nxt_dist in graph[now_node].items():
            new_dist = now_dist + nxt_dist
            if distances[nxt_node] > new_dist:
                distances[nxt_node] = new_dist
                heappush(queue, [new_dist, nxt_node])
    return distances
        
def solution(N, road, K):
    global graph
    graph = {(i+1): dict() for i in range(N)}
    for a, b, c in road:
        set_graph(a, b, c)
        set_graph(b, a, c)
    distances = dijkstra(1)
    result = [node for node, dist in distances.items() if dist <= K]
    return len(result)