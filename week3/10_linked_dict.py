class LinkedTuple:
    def __init__(self):
        self.items = list()


    def add(self, key, value):
        self.items.append((key, value))

    #[("fast", "빠른"), ("slow", "느린")]이 있으면
    #k는 key고 v는 value인데
    #key값을 받아서, 그 k값이 ket값과 동일하다면
    #거기에 해당되는 데이터를 반환해준다.

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = [] #LinkedTuple(), LinkedTuple() 이렇게 들어가있음
        for i in range(8): #저 위에서 키가 동일하면 LinkedTuple 안에서 쭉쭉 늘어나는 구조임
            self.items.append(LinkedTuple())

    def put(self, key, value):

        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

        return

    def get(self, key):

        index = hash(key) % len(self.items)
        #LinkedTuple이 있는 상황임
        #저 안에 들어있는 데이터들 중에 key1, value1 / key2,value2
        #키가 동일하면 value를 반환해준다
        return self.items[index].get(key)

