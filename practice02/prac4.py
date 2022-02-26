# 네트워크

'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
'''


def dfs(n, computers, start, visited):
    visited[start] = True

    for i in range(0, n):
        if(visited[i] == False and computers[start][i] == 1):
            visited = dfs(n, computers, visited)
    return visited


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for start in range(0, n):
        if(visited[start] == False):
            dfs(n, computers, start, visited)
            answer += 1
    return answer
