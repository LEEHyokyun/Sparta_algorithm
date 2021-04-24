# 최초 배열은 0 0 0 0 0
# 4에서 쐈을때 7을 저장
# 맨 오른쪽부터 탐색을 시작해서
# [ 0 0 0 0 4]
# 7은 9가 신호를 받기 떄문에
# 이후엔 4가 필요없으므로 6 9 5 7 만 존재한다고 가정
# [ 0 0 0 2 4]
# 6 9 5 만 존재한다고 가정
# [ 0 0 2 2 4]
# 원소가 맨 뒤에거 부터 없어진다 .. 스택!

top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):

    answer = [0] * len(heights) # 0 0 0 0 0
    while heights: #heights가 빈 상태가 아닐떄까지
        height = heights.pop()
        print("poped node is", height)

        for idx in range(len(heights) - 1, 0, -1): #인덱스가 -1까지 비교를 해야함
            if heights[idx] > height:
                answer[len(heights)] = idx + 1 #가장 높은 탑의 인덱스로 업데이트 해줘야함
                break #업데이트 했으면 더이상 비교안해도 되고, 바로 나오면 됨


    return answer



print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!