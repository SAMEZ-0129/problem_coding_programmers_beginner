def solution(sides):
    answer,n = 0,max(sides)-min(sides)+1
    # 주어진 길이 중 가장 긴 변이 있는 경우
    while max(sides) < min(sides) + n and max(sides)+1 != n:
        n+=1
        answer+=1
    # 나머지 하나가 가장 긴 변일 경우
    n = max(sides)+1
    while n < max(sides) + min(sides):
        n+=1
        answer+=1
    return answer
    
print(solution([11,7]))
