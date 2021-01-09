class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index): #index번째 노드를 호출
        node = self.head
        count = 0
        while count < index : #inedx때까지 계속 반복
            node = node.next
            count = count + 1
        return node

                # next_node 메소드를 index번 해야한다는 의미
                # 헤드로부터 시작하여 index만큼 이동한다

    def add_node(self, index, value): #index 번쨰에 새로운 원소값을 추가 #몇번쨰? 무슨값?
        new_node = Node(value)
        if index == 0: #index가 0일때 예외처리 해야함
            new_node.next = self.head
            self.head = new_node #index 0일때 head node 교체

        node = self.get_node(index-1) #클래스내 함수호출 #index-1로 해야 해당 노드수 호출
                                          #0일때 (-1 예외처리필요)

        next_node = node.next #현재 노드 다음거를 next_node
        node.next = new_node
        new_node.next = next_node #별도 반환값 없음

    def delete_node(self, index):
         if index == 0:  # index가 0이면 헤드노드를 없앤다는것! 헤드노드 교체필요!
            self.head = self.head.next  # 현재 헤드노드를 다음 노드로 교체
         node = self.get_node(index - 1)  # 현재 노드를 불러오고
         node.next = node.next.next  # 다음 노드를 그 다음것으로 교체한다


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# 5 > 12 > 8
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!

#linked_list.add_node(1,6) # 5 12 6 8 (5 6 12 8?)
                          # index가 1이면 두번쨰 노드값을 잡아서 뒤에서 연결한 것임
                          # 따라서 index번쨰에 넣기위해선 index-1 노드를 불러와야함
linked_list.add_node(1,6) #index-1 과 추가하고 싶은 숫자 추가
linked_list.print_all()
