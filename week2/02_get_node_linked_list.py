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

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index : #inedx때까지 계속 반복
            node = node.next
            count = count + 1
        return node

                # next_node 메소드를 index번 해야한다는 의미
                # 헤드로부터 시작하여 index만큼 이동한다

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!

print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
