def remove_duplicates(s):
    # 파이썬의 set는 순서를 보장하지 않기 때문에, 순서대로 중복을 제거하려면 아래와 같이 처리합니다.
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def solution(spell, dic):
    words_no_duplicates = [remove_duplicates(dic) for dic in dic]
    count = 0
    for i in words_no_duplicates:
        for a in i:
            if a in spell:
                count += 1
        if count == len(spell): return 1
        count = 0
    return 2
print(solution(["s", "o", "m", "d"],["moos", "dzx", "smm", "sunmmo", "som"]	))