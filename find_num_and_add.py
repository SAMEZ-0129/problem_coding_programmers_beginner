def solution(my_string):
    import re
    x,sum = [int(s) for s in re.findall(r'\d+', my_string)],0
    for i in x: sum+=i
    return sum
    # my_string = list(my_string)
    # number,sum, cnt, a = ['1','2','3','4','5','6','7','8','9','0'], 0, 0, ''
    
    # for i in range(len(my_string)):
    #     # nums included partialy
    #     if my_string[i] == my_string[-1] and my_string[i] in number: # eol & num
    #         if cnt==0: # while eol, if it was counting -> add / if not just add index i element
    #             sum += int(my_string[i])
    #         else:
    #             a = int(''.join(my_string[i-cnt:]))
    #             # for j in range(i-(i-cnt)+1):
    #             #     a+= my_string[i-cnt+j]
    #             # a = int(a)
    #             sum+=a
    #     elif my_string[i] in number and my_string[i+1] in number:
    #         cnt+=1
    #         continue
    #     elif my_string[i] in number and my_string[i+1] not in number:
    #         if cnt == 0:
    #             sum +=  int(my_string[i])
    #         else:
    #             for j in range(i-(i-cnt)+1):
    #                 a+= my_string[i-cnt+j]
    #             a = int(a)
    #             sum+=a
    #         cnt = 0
    # return sum

print(solution("aAb1B2cC34oOp"))