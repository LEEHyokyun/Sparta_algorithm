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

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next
        while fast is not None: #노드들 끝까지 이동
            fast = fast.next
            slow = slow.next
        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!


#1. 전체길이르 알아낸 난후, K를 빼서 그만큼 이동한다.
#2. 두개의 포인터를 이용한다
# 예를들어 1 2 3 4 5 6 7...
# 두가지 노드 지정
# 한 노드를 다른 노드보다 k 만큼 떨어지게 한다.
# 계속 한칸씩 같이 이동한다
# 만약 더 빠른 노드가 끝에 도달했다면 느린 노드는 끝에서 k 만큼 떨어진 노드가 된다
# 이를 반환하자.