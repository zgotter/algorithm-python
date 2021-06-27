# 성공
# 최단경로 찾기 문제 (다익스트라 알고리즘, dijkstra algorithm)

import heapq

def dijkstra(graph, s_node):
    dist = {n: float('inf') for n in graph.keys()}
    dist[s_node] = 0
    queue = []
    heapq.heappush(queue, [dist[s_node], s_node])
    
    while queue:
        now_dist, now_node = heapq.heappop(queue)
        if dist[now_node] < now_dist: continue
        for nxt_node, weight in graph[now_node].items():
            new_dist = now_dist + weight
            if new_dist < dist[nxt_node]:
                dist[nxt_node] = new_dist
                heapq.heappush(queue, [new_dist, nxt_node])
    return dist

def solution(N, road, K):
    graph = {(i+1): {} for i in range(N)}
    for n1, n2, w in road:
        if n2 in graph[n1].keys():
            if graph[n1][n2] > w:
                graph[n1][n2] = w
        else:
            graph[n1][n2] = w
        if n1 in graph[n2].keys():
            if graph[n2][n1] > w:
                graph[n2][n1] = w
        else:
            graph[n2][n1] = w
    #print(graph)
    distances = dijkstra(graph, 1)
    #print(distances)
    answer = [n for n, d in distances.items() if d <= K]
    return len(answer)