def solution(id_pw, db):
    for x,y in enumerate(db):
        print(x, y)
        if id_pw[0] in y: 
            location = x
        elif y==db[-1]: return 'fail'
        else: continue
        if id_pw[1] == db[location][1]:
            return 'login'
        else: return 'wrong pw' 


    return 0


print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"],	[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))

