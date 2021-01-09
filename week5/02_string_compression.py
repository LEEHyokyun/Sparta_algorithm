# 모든 경우의 수를 다 봐서 최소값을 반환
# 1, 2, 3...,n 의 길이로 자른다.
# 반을 넘어서면 반복이 되지 않으므로, n//2 까지 반복.


input = "abcabcabcabcdededededede"


def string_compression(string):

    n = len(string)
    compression_length_array = []

    for split_size in range(1, n // 2 + 1): #몇의 사이즈로 문자열을 쪼갤것인가? (split size는 최소 1임)
                                            #slicing할때 +1을 붙여줘야 n//2까지 실제로 자르게 됨
        splited = [
            string[i : i + split_size] for i in range(0, n, split_size)
        ]

        count = 1 #몇번 반복되었는지 기록하는 변수
        compressed = ""

        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count = count + 1
            else: #이전거, 현재거 반복하다가 count 늘리고, 더이상 반복할게 없으면 이 else문을 실행
                if count > 1: # 1개 이상이라면 반복된게 몇개 있었다는 뜻
                    compressed = compressed + (str(count) + prev) #숫자를 문자화할수있음 = 2abc
                else:
                    compressed = compressed + prev #반복된게 없으므로 그대로 문자열 사용
                count = 1 # 1차반복이 끝난 순간, count는 1로 초기화.

        if count > 1: #위 반복문을 하고 뒤 문자열 압축 재처리하는 과정
            compressed = compressed + (str(count) + splited[-1]) #prev = 꼬다리
        else:
            compressed = compressed + splited[-1]

        print(compressed)
        compression_length_array.append(len(compressed))


    return min(compression_length_array)
        # 배열의 최소값은 반복순환이 아닌, min 을 사용해서 바로 반환할수있다!
        # 이 return은 뭔데 들여쓰기 잘못하면 결과가 바뀌지?

        # print(splited) 어떻게 쪼개졌는지 확인
        # split[0] split[1]과 비교하면서 몇번 반복되었는지 확인탐색해야함

        # 위 명렁어와 아래 명령어는 동일한 알고리즘입니다.
        # for i in range(0, n, split_size): # 0부터 n까지 인덱스를 split size 만큼 더하면서 반복순환
        #splited.append(string[i : i+split_size]) 위 공 배열에 자른 배열을 추가시킨다.
        #자른 압축 배열을 splited에 추가한다. string[i : i + split_size] # 문자열의 i번째부터 i + split size 까지, 그만큼의 배열을 압축!




print(string_compression(input))  # 14 가 출력되어야 합니다!