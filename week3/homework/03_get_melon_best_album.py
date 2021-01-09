# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내 재생 횟수가 같다면 고유번호가 낮은 노래를 먼저 수록한다.

# 장르별 노래 정렬하기
# 즉, 장르(key)별 재생된 횟수(value)를 정렬하기
# 장르 내에서도 플레이 수가 몇인지 저장해놔야한다.
# 장르별 곡의 정보(인덱스, 재생횟수)를 배열로 묶어 저장한다.


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {} #해쉬 딕셔너리를 만드는 배열은 중괄호로!!
    genre_index_play_array_dict ={}

    n = len(genre_array)

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_total_play_dict: #키가 없다면 그대로 대입
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] = genre_total_play_dict[genre] + play
            genre_index_play_array_dict[genre].append([i, play])

    #딕셔너리에서 높은 값을 가진 키를 가져올수 있을지



    print(genre_total_play_dict) #클래식과 팝에 따른 총 플레이 개수가 저장됨
    print(genre_index_play_array_dict)
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_play_array) #play수 기준으로 역정렬된 배열이 나옴

    result = []

    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre] #1 600 / 4 2500
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        print(sorted_index_play_array)

        for i in range(len(sorted_index_play_array)):

            if i > 1: #클래식이 3곡, 팝이 2곡 - 모든곡이 나오게 된다.
                break # i>1이면 반복문 끝, 두곡씩만 넣어지게 된다(0/1).

            result.append(sorted_index_play_array[i][0]) #0번쨰 인덱스값 반환

    # a = {"fast": 33, "slow": 22}
    # a.items()
    # dict_items([('fast', 33), ('slow', 22)])
    # item 메소드를 사용하여, 딕셔너리에 저장되어있는 아이템을 불러올수 있음
    # 내부(튜플)에서, 1번쨰 인덱스(숫자)를 가지고 정렬을 하려면 메소드가 따로 정해져있음
    # sorted() 함수를 사용할것!
    # sorted(a.items(), key=lambda item: item[1])
    # item 정렬을 받아서, item 튜플의 "첫번째" 인덱스를 통해 원소들을 정려할 것이다.
    # sorted(a.items(), key=lambda item: item[1], reverse=True)    
    # 역순 정렬

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!