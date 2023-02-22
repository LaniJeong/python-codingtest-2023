# 백준 18352 - 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X, = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)                        # 방문리스트 초기화

def BFS(v):
    q = deque()
    q.apppend(v)
    visited[v] += 1
    while q:
        now = q.popleft()
        for i in A[now]:
            if visited[i] == -1:                # 미방문이면
                visited[i] = visited[now] + 1
                q.append(i)

# 두번째 줄 부터 엣지 입력
for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X)                                          # 시작점부터 BFS시작

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
