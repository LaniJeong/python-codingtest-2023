# 백준 1920 - 원하는 정수찾기
N = int(input()) # 5
A = list(map(int, input().split())) # 4 1 5 2 3
A.sort()

M = int(input())    # 4
targetList = list(map(int, input().split()))      # 1 3 7 9

for i in range(M):
    find = False
    target  = targetList[i]
    # 이진탐색
    start = 0
    end = N -1
    while start <= end:
        midle = (start + end) // 2   # 중앙 인덱스
        midVal = A[midle]      # 중앙에 있는 값
        if midVal > target:
            end = midle - 1
        elif midVal < target:   # 왼쪽 날림
            start = midle + 1
        else:   # 값 찾음
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
        