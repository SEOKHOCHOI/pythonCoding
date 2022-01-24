# 문자열 자료형의 함수!

# 문자열 자료형 뒤집기
'''
슬라이싱 이용하면 돼.
[::-1] -1을 넣으면 거꾸로 출발해서 뒤에서 부터 앞쪽으로 하나씩 이동하며 봐.
'''
str = "Hello World"
print(str[::-1])  # -> dlroW olleH 출력


# len() : 문자열의 길이를 출력, 자료형의 길이를 출력해줌!
print(len(str))  # -> 11 출력


# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인할때 사용
'''
어떠한 문자열이 있을때 그 문자열이 공백이나 숫자 같은것들이 
포함돼있지 않고 오직 문자로만 이루어져 있는지 검사 할 수 있음.
내부적으로 아스키코드를 보고 판별하기 때문에 
한글을 넣어도 일반적으로 문자로 이루어져 있다고 판별해줘.
그래서 일반적으로 특정한 문자열에 영어 알파벳만이 포함돼있는지 
아닌지를 판별,검증해줄때 사용.
'''
print(str.isalpha())  # -> False 출력, 공백이 껴있으니까
str2 = "HelloWorld"
print(str2.isalpha())  # -> True
str3 = "최석호"
print(str3.isalpha())  # -> True


# isdigit(): 특정한 문자열!!!이 숫자로만 이루어져 있는 판별
str4 = "123123"
str5 = "123 123"
print(str4.isdigit())  # -> True
print(str5.isdigit())  # -> False


# isalnum() : 특정한 문자열!!이 문자 혹은 숫자로 이루어져 있는지 확인
# + 공백이나 특수문자 들어가면 False
str6 = "123하하dssdㅇㄴㅁㄹㄴㅇ"
str7 = "123gwker"
print(str6.isalnum())  # -> True
print(str7.isalnum())  # -> True


# join() : 여러 개의 문자열을 구분자와 함께 합치는 함수
# 매개변수로는 리스트 자료형이 들어가 join(리스트 자료형)
# ',' 부분에 쉼표뿐 아니라 _ 나 - 등 뭐든 가능
list = ['Hello', 'World', '홍길동']
print(','.join(list))  # 구분자로 ,(쉼표) 사용. Hello,World,홍길동 출력


# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
'''
sorted()함수를 불러오게 되면 그 결과는 list 자료형이 돼.
'''
str8 = "helloworld"
list = sorted(str8)
print(list)  # -> ['d', 'e', 'h', ...] 이렇게 오름차순으로 출력
print(''.join(list))  # -> dehllloorw 출력 (정렬된게 하나의 문자열로 합쳐짐)
list = sorted(str, reverse=True)  # 내림차순 정렬시 reverse=True
print(''.join(list))  # -> roollledWH 출력


# split(토큰) : 특정한 토큰을 기준으로 문자열을 분리( 띄어쓰기 하이픈 등등등 )
str9 = "I wanna watch a movie."
list = str9.split(' ')  # 띄어쓰기 기준으로 분리
print(list)  # -> ['I', 'wanna', 'watch', 'a', 'movie.'] 출력


# find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# + 찾는게 여러개가 들어가있을 경우 가장 앞쪽에 있는 문자열을 찾아서 해당 인덱스 반환
# + 이를 예방하기 위해 find('찾는단어', 5) 인덱스 5 이후에부터 찾는단어를 찾겠단 뜻.
str10 = "I like like you."
print(str10.find('like'))  # -> like라는 문자열 찾는것. 있으니 like의 l이 시작되는 인덱스인 2 출력
print(str10.find('haha'))  # -> 포함돼있지 않을 경우는 -1 반환돼
print(str10.find('like', 5))


# upper(), lower() : 문자열을 대문자로 혹은 소문자로 변환해주는 함수
# +알파벳 아닌건 공백말곤 안나와
'''
실제로 나중에 파이썬으로 어떠한 데이터를 처리하고자 하는데,
데이터가 소문자 만으로 이루어져 있거나 소문자와 대문자로 각각 이어져서
이루어져 있거나 혹은 소문자, 대문자와 상관없이 처리해야 할때 등등
정말 다양한 상황에서 이러한 함수가 사용 될 수 있다.
'''
str11 = "Hello 하하33World"
print(str.upper())  # -> HELLO WORLD
print(str.lower())  # -> hello world

# strip() : 좌,우로 특정한 문자열을 제거하는 함수
# lstrip() : 왼쪽에 있는것만 제거
# rstrip() : 오른쪽에 있는것만 제거
'''
특정한 문자열이 있을때 양쪽 사이드에 어떠한 불필요한 문자가
포함돼 있을때 이러한 strip함수를 이용 할 수 있다.
스트립 함수는 기본적으로 매개변수에 어떠한 내용도 넣지 않게된다면
자동으로 공백을 제거해준단 특징이 있다.

나중에 파이썬을 이용해서 어떠한 웹사이트를 크롤링 하거나 할 때
웹사이트의 초반부나 후반부에 우리가 의도하지 않은 다양한 불필요한 데이터가
들어가는 경우가 굉장히 많다. 이런 경우에 특화된 함수!
데이터를 정제하기 위한 목적으로 많이 사용돼.
'''
str12 = "    Hello World   "
str13 = "tttHitt"
print(str12)
print(str.strip())  # -> 공백 제거된 Hello World 출력
print(str13.strip('t'))  # -> t가 전부 제거된 Hi만 출력


# eval() : 문자열 수식 계산해주는 함수
# + 문자열 자체로 이루어진 수식이 존재할때 계산할수있게 해줌
exp = "(203+705)*3-(30/6)"  # 수식이 문자열 안에 들어가 있음.
print(eval(exp))  # -> 계산된 2719.0 출력
