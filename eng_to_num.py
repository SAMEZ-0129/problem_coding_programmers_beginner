# def solution(numbers):
#     eng_num,cnt,answer = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],0,''
#     for i in range(len(numbers)):
#         a = numbers[:cnt]
#         print(a)
#         if a in eng_num: 
#             answer+=str(cnt)
#         cnt+=1
#     return answer


def solution(numbers):
    # 숫자와 영어 단어의 매핑 관계 정의
    mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
        }
    # 결과를 저장할 변수 초기화
    result = ""
    # 문자열 "numbers"를 순회하면서 각 단어를 숫자로 바꾸기
    i, j = 0, 3
    while i < len(numbers):
        # 현재 위치에서 길이 3인 부분 문자열 추출
        word = numbers[i:j]
        # 추출한 부분 문자열이 영어 단어에 해당하는지 확인하고 해당하는 숫자로 변환
        if word in mapping:
            result += str(mapping[word])
            i = j
            j += 3
        else:
            # 추출한 부분 문자열이 영어 단어에 해당하지 않으면 다음 문자로 이동
            j += 1
        # 인덱스 범위 체크 및 반복문 탈출 조건
        if j > len(numbers):
            break
    # 변환된 숫자를 정수로 변환하여 반환
    return int(result)

print(solution("onefourzerosixseven"))