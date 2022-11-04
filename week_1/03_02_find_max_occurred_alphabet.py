input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # 파이썬 내장함수 str.isalpha() 해당 문자열이 알파벳인지 확인 -> True, False
            continue
        arr_index = ord(char) - ord("a")  # ord() 아스키 값 받기
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphanet_occurrence = alphabet_occurrence_array[index]

        if alphanet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphanet_occurrence

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)
