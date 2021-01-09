# 코니의 위치 변화
# 코니는 처음 위치에서 매초 마다 +1씩 증가하여 움직임
# 증가하는 속도가 1초마다 1씩 증가
# 1 2 3 4 5 6 7 8 9 (속도)
# 3(가정) 4 6 9 13 18 (위치)
# 코니 : x 초후 위치는 1+2+3+...+x

# 브라운의 위치 변화
# B - 1 B +1 B * 2 중 유동적으로 변화
# 2(맨처음 위치)
# 1-1)-1의 경우 > 1
# 1-1-1) > 0
# 1-1-2) > 2
# 1-1-3) > 2
# 1-2) +1의 경우 > 3
# 1-2-1) 2
# 1-2-2) 4
# 1-2-3) 6
# 1-3) *2의 경우 > 4

# 코니와 브라운이 만나려면 모든 경우의수를 고려해야한다.
# 모든 경우의 수를 다 나열
# BFS를 사용해보자.
# 똑같은 시간에 똑같은 위치에 존재해야 한다.
# 시간은 + 1 , 코니 브라운은 자유자재로 위치가 변화한다
# 규칙적 > 배열  자유자재 변화 > 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치를 저장하고 싶다
# 배열안에 딕셔너리를 넣는 방식으로 구현해보자.

from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0  # 현재 시간을 저장하는 변수
    queue = deque()  # import로 queue 뼈대만들고, deque로 선언.
    queue.append((brown_loc, 0))  # 큐에 위치와 시간을 동시에 담아준다.

    # 브라운이 각 초에 존재할 수 있는 장소를 조회할 수 있는 딕셔너리 배열.
    visited = [{} for _ in range(200001)]

    # 초기 위치는 2이고, 초기 시간은 0이다.
    # 각 위치에 어느 초에 도달할 수 있을지 어떻게 분석할 수 있을까?
    # 시간 0 1 2
    # 위치 2 1
    #      3
    #      4
    # visited[2] = {
    #    0: True,
    #    2: True
    # }
    # visited[1] = {
    #    1: True
    # }
    # visited[3] = {
    #    1: True
    # }
    # visited[4] = {
    #
    # }

    # visited[위치][시간]
    # visited[3][5] > 3위치에 5초에 간적이 있냐, visited[3]에 5라는 키가 있냐
    # 0 > 1
    #

    # 일단 처음에 visited 딕셔너리를 사용할 마음가짐(알고리즘)은 아래와 같다.
    # visited[0] = {
    #    2: True
    # }
    # visited[1] = {
    #    1: True,
    #    3: True,
    #    4: True
    # }
    # visited[2] = {
    #    0: True,
    #    2: True,
    #    3: True,
    #    4: True,
    #    8: True
    # }

    # visited의 원소들은 각 시간에 어느 곳을 갔는지를 저장하기위한 시간
    # 배열화한 visited 배열들에 딕셔너리 형식으로 ~초에 어느 곳을 갔는지 저장한다.
    # { key : data }

    # new position 을 모두 탐색하는 후보군을 만들어서 전부 탐색한다.
    # 이를 탐색하기 위한 queue를 만든다.
    # time은 항상 1초씩 증가한다.

    while cony_loc <= 200000:  # 일단 while 1로 작성하고, 그 이후에 탈출조건을 생각해본다.
        cony_loc = cony_loc + time  # 시간만큼 이동

        if time in visited[cony_loc]:
            return time  # 이 시간대에 코니가 방문했으므로

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()  # 큐의 초기위치와 초기시간은 위 큐에 넣어주었던 초기 값들이다.

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            time = time + 1

    return -1  # 위 while을 해도 부합하지 않으면 -1 반환


print(catch_me(c, b))  # 5가 나와야 합니다!
