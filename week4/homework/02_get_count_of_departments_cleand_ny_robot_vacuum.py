# BFS / visited(1차원 배열시)

# 1. 현재 위치를 청소한다.
# 2. 2차원 배열이기 때문에 visited는 사용이 힘들고
# 3. 0은 청소하지 않은 장소, 1은 청소하지 못하는 장소, 2는 청소한 장소
# 4. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색 진행
# 5. 방향을 프로그램으로 구현하기위한 방법이 있다.
# * 배열내 row column, 북쪽이라 가정하면 배열내 row가 -1 해줘야 한다(0,1,2,...순)
# * 동쪽으로 간다면 column이 1 증가, 남쪽으로 간다면 row가 1 증가
# 이를 행렬로 저장 (dr, dc)

# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
# 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 북쪽에서 왼쪽으로 회전한다면 서쪽이 되는데
# dr dc에서 0 -> 3 인덱스 변화
# 동쪽에서 왼쪽으로 회전한다면 북쪽이 되는데
# dr dc에서 1 -> 0 인덱스 변화
# 이를 함수화시킨다.

# 왼쪽방향이 청소할 공간이 없다면, 다시 왼쪽으로 회전한다.

# 네 방향 모두 청소가 되어있거나 벽인 경우에는 뒤로 한칸 후진한다.
# 북쪽에서 후진 하면 남쪽 (0 -> 2), 동쪽 후진하면 서쪽(1 -> 3)..
# 이를 역시 함수로 표현.

# 네 방향 모두 청소가 되어있거나 벽이거나, 뒤쪽도 벽이라 후진도 못하면 작동 멈춤

# 반환해줘야 하는 값은 청소한 방의 개수

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0] #북, 동, 남, 서 순
dc = [0, 1, 0, -1] #row, column

def get_d_index_when_rotate_to_left(d): # 0 > 3, 1 > 0, 2 > 1,...
    return (d + 3) % 4

def get_d_index_when_go_back(d): # 0 > 3, 1 > 0, 2 > 1,...
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    n = len(room_map)
    m = len(room_map[0])

    count_of_departments_cleaned = 1 # 처음 칸은 청소완료
    room_map[r][c] = 2 #현재칸 청소함
    queue = list([[r, c, d]]) #모든 칸을 탐색해야하기 떄문에(현재 위치와 방향을 모두 기록해놓고 그 다음에 탐색 고민)

    while queue:
        r, c, d= queue.pop(0) #현재 방향이 d, d를 queue에서 뺸다
        temp_d = d #현재 방향을 저장하는 변수

        for i in range(4): #모든 방향에 대해 d를 바꾸면서 탐색 (0~3에서 탐색)
            temp_d = get_d_index_when_rotate_to_left(temp_d) #한번 왼쪽 회전
            new_r, new_c = r + dr[temp_d], c + dc[temp_d] #왼쪽 방향으로 갔을때 한칸 이동한 값이 됨

            if 0 <= new_r < n and 0 <= new_c < m and current_room_map[new_r][new_c] == 0:
                count_of_departments_cleaned = count_of_departments_cleaned + 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            elif i == 3: #방향을 다 봤는데 갈곳이 없으면 후진
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])
                # 후진 변화량을 r,c에 저장

                if current_room_map[new_r][new_c] == 1: #후진 시도했으나 벽일떄 작동멈춤
                     return count_of_departments_cleaned

    return

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))