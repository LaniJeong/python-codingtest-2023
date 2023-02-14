# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수
memory = []  #lists()
head, current, pre = None, None, None
dataArray = ['셔누', '민혁', '형원','기현', '주헌', '아이엠']

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

# 노드추가
def inserNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData:   # 첫노드 앞
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head  # 제일 앞으로
    while current.link != None: # 중간노드
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

# current.link == Node 까지 온것
    node = Node()
    node.data = insertData
    current.link = node
    return 

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]   # 다현
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두번째 노드 이후
        pre = node
        node =Node()
        node.data = data    # 정연, 쯔위, 사나, 지효 순
        pre.link = node
        memory.append(node)

    printNodes(head)       # 전체출력





