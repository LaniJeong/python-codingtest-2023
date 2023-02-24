from collections import deque

def solution(cards1, cards2, goal):
    cards1_q = deque(list(cards1))
    cards2_q = deque(list(cards2))
    
    for word in goal:
        if cards1_q and cards1_q[0] == word:
            cards1_q.popleft()
        elif cards2_q and cards2_q[0] == word:
            cards2_q.popleft()
        else:
            return "no"
    
    return "yes"