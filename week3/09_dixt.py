#임의의 문자열을 넣었을때,
#기존 키(데이터가 저장된)
#의 인덱스가 임의의 문자열 인덱스가 같아질 경우?
#충돌이 발생할 경우도 고려한다.
#기존 데이터가 삭제되지 않고, 새 데이터 기존 데이터 모두 살리는방법은?
#1. 링크드 리스트 (새 데이터가 기존 데이터의 다음 노드에 저장)


class Dict:
    def __init__(self):
        self.items = [None] * 8


    def put(self, key, value):

        index = hash(key) % len(self.items) #인덱스값을 구하는과정, 배열크기 인덱스만큼!
        self.items[index] = value

        print("index is=", index)
        print("key is=", key)
        print("hash value is=", hash(key))
        print("value is=", value)


    def get(self, key):

        index = hash(key) % len(self.items)
        # key1 > self.items[7] = "test1"
        # key2 > self.items[7] = "test2"
        # test2이 저장되면 test1은 사라진다.
        # test1, test2 모두 살리게 하는 방법은?
        # 첫번쨰 방법은 링크드 리스트
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))

