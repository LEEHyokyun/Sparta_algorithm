# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

# 시작노드를 스택에 넣는다
# 현재 스택의 노드를 뺴서 visited에 추가한다
# 현재 방문한 노드와 인접한 노드중에, 방문하지 않은 노드를 스택에 추가한다.


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


def dfs_stack(adjacent_graph, start_node):

    stack = [start_node]
    visited = []

    while stack: #stack이 비어있을때까지 반복(=True)
        current_node = stack.pop() #현재 스택의 노드를 빼서
        visited.append(current_node) #visited에 추가

        for adjacent_node in adjacent_graph[current_node]: #현재 노드의 인접한 노드를 탐색한다.
            if adjacent_node not in visited : #방문 안한거임
                stack.append(adjacent_node)


    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!