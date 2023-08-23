def solution(score):
    avg = []
    for a in score:
        avg.append((a[0]+a[1])/2)
    print(avg)
    sorted_score = sorted(avg, reverse=True)
    print(sorted_score)
    answer = [sorted_score.index(avg)+1 for avg in avg]
    for avg in avg:
        print(sorted_score.index(avg))
    return answer


print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
print(solution([[80, 70],[24,13]]))
