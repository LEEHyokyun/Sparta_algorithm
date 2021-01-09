#enqueue
#헤드노드 4, 테일노드 2에 대하여
#new node인 3이 들어가면
#헤드가 4, 테일이 3으로 바뀐다.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 큐는 시작과 끝 모두 있어야 한다!
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None



    def enqueue(self, value):

        new_node = Node(value)

        if self.is_empty(): #비어있으면 None이 head이자 tail이 됨
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node #마지막 노드가 새로운 노드가 되고
        self.tail = new_node #붙여진 상태에서, tail이 새 노드와 같으므로

    def dequeue(self): # 헤드에 있는 데이터를 먼저 호출해야한다.
                       # 호출후 앞에 있는 노드들부터 헤드가 되어야 한다.

        if self.is_empty():
            return "Queue is Empty"

        delete_head = self.head #첫째노드를 변수에 저장
        self.head = self.head.next #이후 노드가 헤드노드가 됨
        return delete_head.data #노드값만 반환

    def peek(self):

        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):

        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek()) # 3 3 3
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())