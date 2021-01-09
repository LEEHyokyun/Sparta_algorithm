# [3] -> [4] / 데이터, next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #현재 생성한 링크드리스트(노드 클래스)의 다음 노드는 없음

node = Node(3) #node 객체에는 data 3 저장
first_node = Node(4) #first_node 객체에는 data 4 저장
node.next = first_node #next 메소드 자체는 위에서 정의
                       #여기서 first node로 지정해준것임

print(node.next.data) #최초 node의 next에 data가 주입되어 출력됨

class LinkedList:
    def __init__(self, data): #헤드노드!
        self.head = Node(data) #위 Node 클래스에 데이터가 주입된 객체,
                               #그 자체가 self.head라는 메소드로 저장됨됨
    def append(self, data): #모든 노드 뒤에 새로운 데이터 넣은 노드를 추가하고 싶음
        cur = self.head
        while cur.next is not None: #None이 아닐떄까지 반복
            cur = cur.next
        cur.next = Node(data) #새 데이터를 담은 노드가 cur.next에 넘겨진다
        print(cur.data)

    def print_all(self):
        print("hihihi") #모든 node의 값을 출력하기 위함
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next #있을때까지 반복하고, 있으면 바로 출력됨.

Linked_List = LinkedList(3)
Linked_List.append(4) #main node가 출력 (위 print(cur)일때)
Linked_List.append(5) #일전마지막 저장된 데이터로 지정되어 출력
#다음 또 반복하면 5가 cur.next에 저장되어, 최종적으로 cur에 있는 마지막 데이터가 출력
Linked_List.print_all() #노드에 있는 데이터를 모두 출력

#[3] -> [4] -> [5] -> .. append 함수 실행으로 뒤 데이터가 노드로 생성

