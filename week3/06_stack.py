#링크드리스트를 기반으로 스택구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 4에서 3이 들어온다면
# 새로운값이 3을 헤드로 올리고
# 3 의 포인터는 4를 가르키도록 해야한다.

class Stack:
    def __init__(self):
        self.head = None #헤드노드

    def push(self, value):

        new_head = Node(value) #새로운데이터가 헤드
        new_head.next = self.head #포인터가 다음 헤드드
        self.head = new_head

    # pop 기능 구현
    def pop(self):

        if self.is_empty():
            return "Stack is empty"
        delete_head = self.head
        self.head = self.head.next

        return delete_head

    def peek(self):

        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop().data)
print(stack.is_empty())
