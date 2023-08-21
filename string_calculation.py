def solution(my_string):
    answer,temp = 0,0
    my_string = my_string.split()
    for i in range(3):
        if my_string[i]=='+':
            temp = int(my_string[0])+int(my_string[2])
            answer += temp
        if my_string[i]=='-':
            temp = int(my_string[0])-int(my_string[2])
            answer += temp
    for i in range(len(my_string)-3):
        print(my_string[i+2])
        if my_string[i+3]=='+':
            answer += int(my_string[i+4])
        if my_string[i+3]=='-':
            answer -= int(my_string[i+4])
    return answer

print(solution("3 + 4 - 3 + 5"))