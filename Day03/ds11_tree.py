# 이진트리
# 전역변수

NameAry = ['블랙핑크', '레드벨벳', '마마무', '']



search = input('찾을 걸그룹을 입력 > ')

current = root
while True:
    if search == current.data:
        print(search, '찾음 끝')
        break
    elif search < current.data:  # 왼쪽으로
        if current.left == None:
            print(search, '못찾음 끝')
            break
        else:
            current = current.left
    else:  # 오른쪽 노드로
        if current.right == None:
            print(search, '못찾음 끝')
            break
        else:
            current = current.right

