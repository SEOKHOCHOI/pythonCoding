list = [9, 22, 3, 7, 4, 5]
# max() 구현
# max([])는 에러
# max() 사용시 []가 비어있지 않다는 조건 필요.


def max_def(list):
    result = list[0]
    for i in list[1:]:
        if result < i:
            result = i
        print(i, result)

    return result


print('max()구현', max_def(list))


def max_def2(list):
    result2 = list[0]
    for i in range(1, len(list)):
        print(i)
        num = list[i]
        print(i, num)
        if result2 < num:
            result2 = num
    return result2


print('max()구현2', max_def2(list))

# min() 구현


def min_def(list):
    result3 = list[0]
    for i in range(1, len(list)):
        print(i)
        num = list[i]
        print(i, num)
        if result3 > num:
            result3 = num
    return result3


print('min()구현', min_def(list))
