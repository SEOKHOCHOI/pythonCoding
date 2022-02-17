from collections import defaultdict


def solution(n, results):
    arr = defaultdict(set)
    arr2 = defaultdict(set)
    for i in results:
        arr[i[0].add(i[1])]
        arr2[i[1]].add(i[0])
    answer = 0
    for i in range(1, n+1):
        if bfs(arr, i) + bfs(arr2, i) == n-1:
            answer += 1
    return answer


def bfs(graph, start):
    queue = [[start, 0]]
    visited = []
    a = -1
    while queue:
        current = queue.pop(0)
        if current[0] not in visited:
            a += 1
            visited.append(current[0])
            if current[0] in graph:
                arr = set(graph[current[0]]) - set(visited)
                queue.extent([[i, current[1]+1] for i in arr])
    return a
