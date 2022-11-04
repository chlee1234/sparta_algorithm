def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # 파이썬 내장함수 str.isalpha() 해당 문자열이 알파벳인지 확인 -> True, False
            continue
        arr_index = ord(char) - ord("a")   # ord() 아스키 값 받기
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))