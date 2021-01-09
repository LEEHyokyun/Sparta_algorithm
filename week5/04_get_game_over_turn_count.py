# 체스말이 4개이상 쌓이면 게임은 종료된다
# 말이 두개이상 이동한다면, 이동하려는 말과 그 위에 있는 말만 이동시킨다
# 즉 복수의 말이라도, 이동대상이 되는 말 아래에 있는 말들은 이동대상이 안됨.

# 말은 순서대로 이동한다, 말의 순서에 따라 반복문 실행!
# 말은 쌓일 수 있다, 맵에 말이 쌓이는 걸 저장!
# 쌓인 순서대로 이동한다, stack 자료구조!

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 파란색일 경우엔
# 동 0 > 1 서 1 > 0 북 2 > 3 남 3 > 2
# 홀수는 -1 짝수는 +1을 하자

def get_d_index_when_go_back(d): #파란색 조건일때 역행함수 만들기
    if d % 2 == 0 :
        return d + 1
    else:
        return d - 1


# 현재 맵에 어떻게 말이 쌓일지 저장하기 위해선
# 체스맵과 동일하게 2차원 배열로 만들고, 링크드 리스트로 만들어보자!

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):

    n = len(chess_map)
    #아래 배열은 2차원 배열입니다.
    #채스맵이 n by n , n=4, 이중 괄호중 안에 있는 괄호가 4번 반복!(이게 큰 괄호안에 저장)
    #3차원 배열(배열안에서, 각 원소들이 배열들을 저장하는 구조!
    current_stacked_horse_map = [
        [
            [] for _ in range(n)# 각 원소들도 링크드리스트처럼 이어서, 현재 쌓여져 있는 말들을 저장하는 배열을 저장한다!
        ] for _ in range(n)
    ]

    for i in range(horse_count): #말들의 배열을 저장하는 반복문
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i) #rc 위치에, i 번째 말이 있다는 정보를 저장한다.

    turn_count = 1 #반환해야하는 값

    while turn_count <= 1000:
        for horse_index in range(horse_count):

            r, c, d = horse_location_and_directions[horse_index] #각 말들의 현재 위치와 방향이 어딘지 알수있음
            new_r = r + dr[d] #새로운 위치
            new_c = c + dc[d]

            #파란색 조건(뒤로 돌아서 한칸 이동하거나 그대로)
            if not 0 <= new_r <n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d #new_d에 해당하는 인덱스에 맞게 업데이트!
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue #뒤돌았는데도 못간다면 그대로 진행한다, continue


            moving_horse_index_array = [] #이동대상인 말들
            for i in range(len(current_stacked_horse_map[r][c])):
            # 현재 어떻게 쌓여져있는지 저장한 배열을 불러오고
            # 쌓여있는 말들을 같이 이동하고, 또 색깔에 따라 어떻게 이동하는지
                current_stacked_horse_index = current_stacked_horse_map[r][c][i] #쌓여져 있는 말의 인덱스번호
                #현재 이동대상은 horse index이고
                if horse_index == current_stacked_horse_index: #이동시키는 말
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:] #현재 이동대상의 인덱스(i)부터, 같은 위치에 있는 애들은 이동대상임(지금 모두 잡아줬음)
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i] #지금 위치에 남을 친구들은 위에 제거하고 남은 애들이다
                    break #이동할 애들을 잡아준 상태

            if game_map[new_r][new_c] == 1: #체스말들을 뒤집어야 하는 조건임
                moving_horse_index_array = reversed(moving_horse_index_array) #체스말들을 뒤집어서 이동

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index) #이동한 친구들을 쌓아올려서 업데이트 시키자
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c #방금 옮긴 애의 새로운 장소를 저장해주는 배열

            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count = turn_count + 1 #while 반복문이 순환할떄마다 count + 1

    print(current_stacked_horse_map) #0~3 체스말들이 어떻게 배치가 되어있는지 보여준다.

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다