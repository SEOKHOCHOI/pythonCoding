distance = 5

if distance >= 200:
    print("저격총 쏘기!")
elif distance >= 150:
    print("돌격소총 쏘기!")
else:
    print("응애")

# 1. 사용자로부터 가방, 시계 금액 입력받기
# 2. 합계금액 10만원 이상 할인률 30%, 5~10만원 미만 할인률 20%, 5만원 미만 할인률 10%

bag_price = int(input("가방의 금액을 입력해 주세요 >>>"))
watch_price = int(input("시계의 금액을 입력해 주세요 >>>"))

total_price = bag_price + watch_price

if total_price >= 100000:
    total_price = total_price*70/100  # 즉 0.7 곱해주면 돼.
    print(total_price)
elif total_price >= 50000:
    total_price = total_price*80/100  # 0.8
    print(total_price)
else:
    total_price = total_price*90/100  # 0.9
    print(total_price)

# 안에 전부 print를 넣어준것 전체와 이것 하나는 같아!
# print("합계금액은 :", total_price)
