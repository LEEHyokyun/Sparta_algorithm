# 규칙성을 찾기가 쉽지 않다
# 모든 경우를 시도해보면서 탈출할수있는지 없는지 탐색해본다

# 모든 경우의 수 = BFS > queue 사용!
# visited!
# 공이 두개...4차원 배열을 사용한다.
# visited[빨간공_raw][빨간공_col[파란공_raw][파란공_col[
# 위 순서대로 크기가 사이즈가 n m n m

from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
                              # 현재 row, column / 이동할 row, column / game_map(벽인지 구멍 등, 상황을 알기위해)
    move_count = 0

    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "0":  # 조건 #,0 이런거 잘 기억하기!
                                                                              # 다음 이동할 칸이 벽이 아닐때까지, 구멍이 아닐떄까지 이동한다 and 지금 위치가 구멍이어도 게임 종료!
        r = r + diff_r
        c = c + diff_c
        move_count = move_count + 1
    return r, c, move_count  # 끝까지 간 위치 반환


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])  # 행 열의 크기
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    print(visited)

    # BFS 탐색을 원활히 하기위해선, 큐에 어디를 시도할 것인지 데이터를 쌓아야 한다
    # 빨간구슬, 파란구슬 위치를 모두 넣어준다
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque()  # 큐 생성, deque로 생성

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j  # 빨간공 위치
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j  # 파란공 위치

    queue.append((red_row, red_col, blue_row, blue_col, 1))  # 현재 탐색하는 숫자이자 이동한 횟수..초기값은 1로 놓고
    visited[red_row][red_col][blue_row][blue_col] = True  # 현재 조회했음을 나타냄
    # 탐색은 최대 10번까지만 할수있다.

    # 탐색할 준비가 되었으니 탐색해보자
    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()  # 큐에 남은 맨왼쪽 원소를 꺼내서 변수에 지정해보자

        if try_count > 10:
            break  # break 하고 바로 아래로, return false

        for i in range(4):  # 4방향

            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)  # 다음 이동하는 방향에 대해, 그리고 어느 방향을 볼것인지(i에 의해 결정)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            # 공들은 같은 위치에 있을수 없다.

            # 저렇게 이동을 했는데, 블루가 먼저 구멍에 들어가면 게임 종료
            if game_map[next_blue_row][next_blue_col] == 'O': #구멍 O (숫자 0 오기 주의!!)
                continue  # 반복취소
            if game_map[next_red_row][next_red_col] == 'O':
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:  # 같은 위치에 있으면 이동한 횟수가 더 많은 애들이 한칸 더 떨어저줘야 한다
                    next_red_row = next_red_row - dr[i]  # 움직이기로 했던 만큼 떨어지게 조정
                    next_red_col = next_red_col - dc[i]
                else:
                    next_blue_row = next_blue_row - dr[i]
                    next_blue_col = next_blue_col - dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:  # 왔는데 방문하지 않은 곳이었다면?
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True  # 일단 방문처리 해준다(지금 방문해줬으니까)
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col,
                              try_count + 1))  # 이 값을 queue에 추가해주면 BFS 가능!

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

print(" hi hi hi ")