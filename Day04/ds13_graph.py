# 그래프 표현 개선

class Graph:
    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] # 2차원 배열

# 전역변수
G1 = None
nameAry = ['셔누', '민혁', '기현', '형원', '주헌', '창균']
셔누, 민혁, 기현, 형원, 주헌, 창균 = 0, 1, 2, 3, 4, 5


# 그래프 그리기 함수
def printGraph(graph):
    print('   ', end=' ')
    for v in range(graph.SIZE): 
        print(nameAry[v], end=' ')
    print()

    for row in range(graph.SIZE):
        print(nameAry[row], end=' ')
        for col in range(graph.SIZE):
            print(f'   {graph.graph[row][col]}', end=' ')
        print()
    print()

## 메인  코드
if __name__ == '__main__':
    gSize = 6   # 변수
    G1 = Graph(gSize)
    G1.graph[셔누][민혁] = 1; G1.graph[셔누][기현] = 1   # 두 줄에 있는 로직을 한번에 다 쓰고 싶을 때 ; 사용
    G1.graph[민혁][셔누] = 1; G1.graph[민혁][형원] = 1
    G1.graph[기현][셔누] = 1; G1.graph[기현][형원] = 1
    G1.graph[형원][민혁] = 1; G1.graph[형원][기현] = 1
    G1.graph[형원][주헌] = 1; G1.graph[형원][창균] = 1
    G1.graph[주헌][형원] = 1; G1.graph[주헌][창균] = 1
    G1.graph[창균][형원] = 1; G1.graph[창균][주헌] = 1

    print('무방향 그래프')
    printGraph(G1)

