from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
# 오른쪽 에서  <- 방향으로 들어와 왼쪽부터 삭제된다고 생각하면 된다.
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력

'''
queue 구현시 파이썬에서 기본적으로 제공하는
리스트 자료형이 아닌 deque을 이용하는게 시간적으로 유리.

단순히 리스트를 이용해 특정 인덱스에 존재하는 원소를
꺼내기 위해 pop 메소드를 호출하게 되면
원소를 꺼낸뒤에 원소의 위치를 조정하는 과정이 필요하기 때문에
원소를 꺼내는 연산 자체가 O(k)만큼의 시간 복잡도가
요구된다. 그렇기에 리스트를 이용하지 않는게 좋다.
'''
