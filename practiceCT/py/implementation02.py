# 시각
'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
00시 00분 03초
00시 13분 30초

반면에 다음은 3이 하나도 포함되지 않았으므로 세면 안 되는 시각입니다.
00시 02분 55초
01시 27분 45초

이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제입니다.
하루는 86,400초이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400가지 입니다.
24*60*60 = 86,400
따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다.
이러한 유형은 완전 탐색(Brute Forcing)문제 유형이라고 불립니다.
가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미합니다.
'''
# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)