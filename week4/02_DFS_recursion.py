# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# 딕셔너리 안에 들어있는 키에 대해 인접한 노드들(데이터)을 넣는다.

# DFS 깊이가 무한정 깊어지면 에러가 발생할수있다.
# 이를 해결하기위해선 스택이 그 방안이 될 수 있다.

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

# 1. 시작노드(루트노드)인 1부터 탐색한다.
# 2. 현재 방문한 노드를 visited_array에 추가
# 3. 현재 방문한 노드와 인접한 노드중, 방문하지 않은 노드에 방문한다.
# 4. 2, 3 반복.

def dfs_recursion(adjacent_graph, cur_node, visited_array):

    visited_array.append(cur_node) #visited = [1]

    for adjacent_node in adjacent_graph:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

# adjacent_node 가 visited_array에 있는지 없는지 검사하는게 탈출조건

    return

# cur node - 시작하는 노드로
# 1부터 우선 탐색하므로 1을 넣어준다(시작노드)
# 모두 방문한 것을 알 수 있도록 visited 배열을 본다.


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!