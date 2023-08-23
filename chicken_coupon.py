def solution(chicken):
    coupon = 0
    service_chicken = 0
    while chicken >= 10:
        chicken -= 10
        coupon += 10
        print('first', chicken, coupon)
    if chicken < 10:
        coupon+=chicken
    print(coupon)
    while coupon >= 10:
        coupon -= 10
        service_chicken += 1
        coupon += 1
        print('second', coupon, service_chicken)
    return service_chicken

print(solution(1081))
