# 람다식
# 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 특징이 있는 문법
# lambda 키워드를 이용해 매개변수를 지정하고 그 결과를 설정 할 수 있음

# 이렇게 사용
# add = lambda x, y: x + y
# print(add(1, 2))
def add(x, y): return x + y


print(add(1, 2))

# map() 함수와 같이 많이 이용돼
# map(): 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와주는 문법
# map은 어떠한 함수를 리스트에 적용을 할 때 그 리스트의 각 원소에 대해서
# 적용을 하고자 할때 사용 할 수 있다. ( 리스트 전체가 아님 )

# list1 = [1, 2, 3, 4, 5]
# list2 = [6,  7, 8, 9, 10]
# my_function = lambda a, b: a + b
# result = map(my_function, list1, list2) # list1과 list2의 각 원소를 하나씩 확인하며 그 원소끼리 더한 값이 반환됨
# print(list(result))

list1 = [1, 2, 3, 4, 5]
list2 = [6,  7, 8, 9, 10]
def my_function(a, b): return a + b


# list1과 list2의 각 원소를 하나씩 확인하며 그 원소끼리 더한 값이 반환됨
result = map(my_function, list1, list2)
print(list(result))
