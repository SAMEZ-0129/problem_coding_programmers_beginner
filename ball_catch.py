# def solution(numbers, k):
#     # answer = 0
#     # for i in range(k):
#     #     if len(numbers)%2:
#     #         if int(len(numbers)/2)+1 < k:
#     #             if (k// int(len(numbers)/2)+1)%2:
#     #                 return numbers[(2*k// int(len(numbers)/2)+1)//2]
#     if len(numbers)%2==0:
#         a = numbers[::2]
#         if k>len(a):
#             k%=len(a)
#             return a[k-1]
#         else:
#             return a[k-1]
#     else:
#         a = numbers[::2]
#         b = numbers[1::2]
#         if k>len(numbers):
#             while k > len(numbers): k-=len(numbers)
#             if k > round(len(numbers)/2): return b[(k - round(len(numbers)/2))-1]
#             else: return a[k-1]
#         else:
#             if k > round(len(numbers)/2): return b[(k - round(len(numbers)/2))-1]
#             else: return a[k-1]



def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer
print(solution([1,2,3],3))
