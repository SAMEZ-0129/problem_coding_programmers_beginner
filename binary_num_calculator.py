def solution(bin1, bin2):
    answer,len_1,len_2,sum1,sum2 = '', len(bin1), len(bin2), 0, 0
    for i in range(len(bin1)):
        sum1 += int(bin1[len_1-1-i]) * (2**i)
    for i in range(len(bin2)):
        sum2 += int(bin2[len_2-1-i]) * (2**i) 
    answer = format(sum1 + sum2, 'b')
    return answer

print(solution("10","11"))