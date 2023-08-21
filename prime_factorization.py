# my try
# def solution(n): 
#     answer = []
#     temp = n
#     for i in range(2,n+1):
#         if temp%i == 0:
#             temp=temp//i
#             answer.append(i)
#     return answer

# print(solution(1000))

# found in stack
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i: # n%i != 0 랑 같은 의미
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     answer = list(set(factors))
#     return answer

# found in blog (correct)
def solution(n):
    i = 2
    answer = []
    while i  <= n:
        if n % i: # n%i != 0 랑 같은 의미
            i += 1
        else:
            if i not in answer:
                answer.append(i)
            n//=i
    return answer

print(solution(420))
