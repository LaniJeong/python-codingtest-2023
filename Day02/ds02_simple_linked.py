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

# 노드 삭제
def deletNode(deletData):
    global memory, pre, current, head

    if head.data == deletData:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current            # 모두 첫번째 노드 가리킴
        current = current.link   # 두번째 노드를 가리킴
        if current.data == deletData:
            pre.link = current.link     # current가 가리키는 노드를 pre가 가리키도록(삭제)
            del(current)
            return
# current.link == Node 까지 온것
    node = Node()
    node.data = insertData
    current.link = node
    return 

# 노드검색
def findNode(findData):
    global memory, pre, current, head

    current = head    # 첫번째 노드부터
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link   # 다음노드
        if current.data == findData:
            return current

    return Node()   # 빈노드 반환

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

    print('노드추가 ----')

    inserNode('주헌', '화사')  # 맨 앞에 화사노드 추가
    printNodes(head)

    inserNode('형원', '솔라')
    printNodes(head)

    inserNode('아이엠', '문별')
    printNodes(head)

    print('노드 삭제 ----')
    
    deletNode('화사')
    printNodes(head)

    deletNode('문별')
    printNodes(head)

    deletNode('주헌')
    printNodes(head)

    print('노드 검색 ---')

    result = findNode('아이엠')
    if result.data != None:
        print('데이터를 찾았습니다.')
    else:
        print('검색한 데이터가 없습니다.')

    result = findNode('주헌')
    if result.data != None:
        print('데이터를 찾았습니다.')
    else:
        print('검색한 데이터가 없습니다.')



