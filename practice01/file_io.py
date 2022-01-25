# 파일 입출력
# 해당 프로그램을 실행하고 있는 컴퓨터에 새로운 파일을 생성해서
# + 파일의 내용을 출력하거나 혹은 반대로 컴퓨터 내에 존재하는
# + 다른 파일을 읽어오는 그러한 작업을 수행할 대 사용할 수 있는 기능
# 즉, 파일 입출력 기능이 있음 으로서 만약 우리가 게임을 개발하고자 한다면
# + 게임 내의 데이터를 파일 등으로 저장을 해서 프로그램의 특정한 상태를
# + 저장하는 등으로 활용할 수가 있다.
# 흔히 온라인 게임이 아니라 오프라인으로 그냥 간단히 즐기는 게임 같은 경우는
# + 실제로 파일 입출력 기능을 이용해서 게임 내에 데이터가 저장되고
# + 불러올 수 있도록 개발하는 경우가 많은데 그런 것들이 전부다 가능하도록 해주는 게
# + 파일 입출력이 있기 때문이다.
# 파일 입출력은 말 그대로 특정한 데이터를 영구적으로 저장하고자 할 때
# 사용할 수 있는 가장 기본적인 기능이다.

# 파이썬은 파일 입출력을 매우 간단하게 할 수 있는 여러가지 모듈을 제공하고 있다.

# open(): 파일을 특정한 모드로 여는 함수. 읽을때는 r, 쓸 대는 w를 사용
# read(): 파일 객체로부터 모든 내용을 읽는 함수.
# 파일 입출력과 관련한 프로그램에 있어서는 해당 파일에서 모든 내용을 다 읽었거나
# + 아니면 특정한 작업을 모두 수행한 경우 반드시 close()함수를 불러와야 해
# + 그렇게 함으로써 해당 파일에 대한 리소스 사용이 모두 끝났다고 정리해 줄 수가 있어

# 특정한 바이트 위치에서부터 읽을수도 있음
# 그때는 seek() 함수가 사용됨
# 한글이 유니코드 형태로 사용될 때 파이선에서는 각 한글이 3바이트를 차지

f = open("input.txt", "r", encoding="UTF-8")
f.seek(9)  # 9바이트니 3글자 건너띄고
data = f.read()
print(data)
f.close()

# readline() : 파일 객체로부터 한 줄씩 문자열을 읽는 함수
f = open("input.txt", "r", encoding="UTF-8")
count = 0
while count < 3:
    data = f.readline()
    count = count + 1
    print("%d번째 줄: %s" % (count, data))
f.close()

# readlines() : 전체 내용을 한 번에 리스트 담는 함수
f = open("input.txt", "r", encoding="UTF-8")
list = f.readlines()
for i, data in enumerate(list):
    print("%d번째 줄: %s" % (i + 1, data), end='')
print(list)

# with
with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" % (i + 1, data), end='')

# 파일에 포함된 문자의 빈도수를 추출


def process(filename):
    with open(filename, "r") as f:
        # 키: 알파벳, 값: 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict


dict = process("input.txt")
# 빈도수를 기준으로 내림차순 정렬을 수행
dict = sorted(dict.items(), key=lambda a: a[1], reverse=True)
for data, count in dict:
    if data == '\n' or data == ' ':
        continue
print("%d번 출현: [%c]" % (count, data))
# 지금 만든건 영어 문자열만 처리하도록 만든거라 현재 읽는 파일을 전부 영어로 적어줘야해 지금 한글이니 확인할때만 잠깐 고쳐봐
