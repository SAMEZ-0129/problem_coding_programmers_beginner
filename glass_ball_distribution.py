def solution(balls, share):
    fact1,fact2,fact3 = 1,1,1
    for i in range(1,balls-share+1):
        fact1*=i
    for i in range(1,balls+1):
        fact2*=i
    for i in range(1,share+1):
        fact3*=i
    return int(fact2/(fact1*fact3))

print(solution(5,3))