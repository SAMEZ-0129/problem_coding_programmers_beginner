def sol(s):
    s = list(s.split())
    answer = temp = 0
    for i in s:
        if i.lstrip('-').isdigit() == True: 
            answer+=int(i)
            temp = int(i)
        else: answer-=temp
    return answer

print(sol("-1 -2 -3 Z"))