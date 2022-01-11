# 또다른 자료형이다
# 변수, 리스트와 같은 자료의 형태다.
# 자료를 저장하는 또다른 녀석!


# 1. 승패여부
# 2. 챔피언 이름
# 3. 킬
# 4. 데스
# 5. 어시스트

# 변수를 사용할 때
# 하지만 전적이 하나가 아니라면 엄청 불편해.
result = '승리'
chanmp_name = '비에고'
kill = 13
death = 9
assist = 17

# 리스트자료형 사용할 때
# 여러개 전적 데이터를 사용할때 간편함
# 단점: 데이터를 저장해줬을때 데이터가 어떤뜻을 가지고 있는지 데이터가 무엇인지 알려줄 방법이 없어.
play_data = ['승리', '비에고', 13, 9, 17]
play_data2 = ['승리', '비에고', 13, 9, 17]

# 딕셔너리: 사전형 자료형! 리스트의 단점 해결.
# 영어 단어를 먼저 쓰는것처럼 key를 먼저 써주고
# 그다음에 값을 써준다 key : value
# 즉, 딕셔너리는 키와 값의 쌍으로 이루어진 자료형이고,
# 딕셔너리이름 = {키1 :값1, 키2: 값2, ...} 로 사용한다.
play_data = {
    'result': '승리',
    'champ_name': '비에고',
    'kill': 13,
    'death': 9,
    'assist': 17,
}
play_data2 = {
    'result': '승리',
    'champ_name': '비에고',
    'kill': 13,
    'death': 9,
    'assist': 17,
}
# 만든 딕셔너리에 접근하는 방법
play_data['result']  # 딕셔너리이름[키값], 그럼 vaule값 승리가 나올것.

# 딕셔너리 수정하는 방법
# 기존 값 벼경
play_data['result'] = '패배'

# 새로운 키, 값 추가
play_data['level'] = 18

# 데이터 삭제
del play_data['champ_name']

print(play_data)

# 딕셔너리 관련된 함수
# 딕셔너리 관련된 함수를 사용할때는 for in 문과 함께 사용한다.
# keys()
# 이러면 play_data 딕셔너리 안에 있는 모든 키들이 key에 담겨서 출력이 된다.
for key in play_data.keys():
    print(key)

# values()
# 값에 해당하는 데이터가 출력돼.
for value in play_data.values():
    print(value)

# items()
# 키와 벨류를 한 번에 가져올때 사용해.
for key, value in play_data.items():
    print(key, value)
