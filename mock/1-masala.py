import os
os.system("cls")


def add_two_dict(d1, d2):
    result = d1.copy()
    for k,q in d2.items():
        # if k in result:
        #     result[k] += q
        # else:
        #     result[k] = q

        # if k not in result:
        #     result[k] = 0
        # result[k] += q

        result[k] = result.get(k, 0) + q
        
    return result

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "d": 5}

print(add_two_dict(d1,d2))