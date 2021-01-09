#알파벳을 모두 대입하여 알파벳이 몇번 나오는지 세기

input = "hello my name is sparta"


def find_max_occurred_alphabet(string): # 함수 끝맺음
    alphabet_array = ["a","b","c","d","e","f","g","h","i","J","k","l","m","n","o","p",
                      "q","r","s","t","u","v","w","x","y","z"]
    max_occurence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurence = 0
        for char in string:
             if char == alphabet:
                 occurence += 1

        if occurence > max_occurence:
             max_occurence = occurence
             max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)