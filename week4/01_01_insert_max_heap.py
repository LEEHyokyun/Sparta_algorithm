# 1. 새노드를 맨 끝에 추가한다.
# 2. 지금 넣은 새노드를 부모와 비교하고, 부모보다 크다면 교체.
# 3. 과정을 맨 위로 올라갈때까지 반복한다.

class MaxHeap:
    def __init__(self):
        self.items = [None]




    def insert(self, value):

        self.items.append(value)

        cur_index = len(self.items) - 1

        while cur_index > 1:  # 꼭대기 올라가면 중단
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:  # 새노드가 부모보다 크면 자리를 바꾼다
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]

                cur_index = parent_index  # 노드가 바뀌었다면 인덱스 교체
            else:
                break

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!