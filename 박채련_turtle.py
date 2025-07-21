'''
밥 먹는 거북이

1. 파란 공이 화면에 랜덤하게 등장
2. 거북이를 방향키로 움직여서 공에 닿으면 점수 +1
3. 30초 안에 몇 개 먹는지 도전
'''

import turtle        # 거북이 그래픽 모듈
import random        # 랜덤 위치 생성을 위해 사용
import time          # 시간 측정용 (제한시간 계산)

# 게임 화면 설정
screen = turtle.Screen()
screen.setup(600, 600)                # 가로 세로 600px 크기
screen.title("밥 먹는 거북이")  # 창 제목

# 거북이 캐릭터 (플레이어) 설정
player = turtle.Turtle()
player.shape("turtle")    # 거북이 모양
player.color("green")     # 초록색
player.penup()            # 선 안 그리게 (움직일 때 선 X)

# 먹이 (파란 원 형태)
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))  # 랜덤 위치로 이동

# 방향키 입력 처리 함수 정의
def up(): player.sety(player.ycor() + 20)      # Y좌표 +20 (위로)
def down(): player.sety(player.ycor() - 20)    # 아래로
def left(): player.setx(player.xcor() - 20)    # 왼쪽으로
def right(): player.setx(player.xcor() + 20)   # 오른쪽으로

# 키보드 이벤트 연결
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# 게임 점수 및 시간 설정
score = 0
start = time.time()       # 시작 시간 기록
duration = 30             # 제한 시간: 30초

# 메인 게임 루프
while time.time() - start < duration:
    # 거북이가 먹이에 닿았는지 확인
    if player.distance(food) < 20:
        score += 1  # 점수 1점 추가
        # 먹이 새로운 위치로 이동
        food.goto(random.randint(-200, 200), random.randint(-200, 200))

    screen.update()  # 화면 갱신 (움직임 반영)

# 시간 종료 후 결과 출력
print(f"게임 종료! 점수: {score}")

turtle.bye()  # 창 닫기