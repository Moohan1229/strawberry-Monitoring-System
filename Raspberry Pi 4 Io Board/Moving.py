import RPi.GPIO as GPIO
import time
import asyncio

# GPIO Pin 설정
POS_SEN = 6
X_CW = 22
X_CCW = 23
Z_CW = 24
Z_CCW = 25

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(POS_SEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(X_CW, GPIO.OUT)
GPIO.setup(X_CCW, GPIO.OUT)
GPIO.setup(Z_CW, GPIO.OUT)
GPIO.setup(Z_CCW, GPIO.OUT)


# 변수 설정
posision_count = 0
last_posision_count = -1  # 마지막 위치를 기억하는 변수
Start_switch = True
count_reset = False
Shot_SIG = False
last_change_time = None
No_movement_time = 50  # 5초 동안 움직임이 없으면 리셋 (초 단위)
HOME_BACK = 10  # 리셋 시 홈 위치로 돌아가는 대기 시간 (초 단위)
SHOT_TIME = 3  # 촬영 시간 (초 단위)
tolerance = 1  # 오차 범위
target_positions = [5, 10, 15, 20, 25, 30, 35]  # 목표 위치

# 각 목표 위치별 처리 여부를 추적하는 배열 (처리 여부 플래그)
target_reached_flags = [False] * len(target_positions)

# Z, X 축 동작 시간
AUTO_Z_CW = 5
AUTO_Z_CCW = 5
AUTO_X_CW = 5
AUTO_X_CCW = 5


async def Auto_motion():
    global posision_count, Start_switch, count_reset, last_change_time, last_posision_count

    current_time = time.time()

    # 위치 센서가 감지되면 posision_count 증가
    if GPIO.input(POS_SEN) == GPIO.LOW and not count_reset:
        posision_count += 1
        last_change_time = current_time
        print(f"Position Count +1, Now Count = {posision_count}")

    # 5초 동안 위치 변화가 없으면 카운트 리셋
    if last_change_time and (current_time - last_change_time) > No_movement_time and not count_reset:
        print("No movement detected for 5 seconds, resetting count.")
        count_reset = True

    # 카운트 리셋 시 초기 위치로 돌아감
    if count_reset:
        posision_count = 0
        GPIO.output(X_CCW, GPIO.HIGH)
        GPIO.output(Z_CCW, GPIO.HIGH)
        await asyncio.sleep(HOME_BACK)  # 홈 위치로 돌아감
        GPIO.output(X_CCW, GPIO.LOW)
        GPIO.output(Z_CCW, GPIO.LOW)
        count_reset = False

    # 자동 시작이 설정된 경우
    if Start_switch:
        # 목표 위치에 도달하지 않았을 때 X 축 동작
        if posision_count < 36:
            GPIO.output(X_CW, GPIO.LOW)

        # 목표 위치에 도달하지 않았고, 아직 해당 위치가 처리되지 않았으면 동작 수행
        for i, target_position in enumerate(target_positions):
            if abs(posision_count - target_position) <= tolerance and not target_reached_flags[i]:
                print(f"Target position {target_position} reached.")

                GPIO.output(X_CW, GPIO.HIGH)
                await asyncio.sleep(10)  # 10초 대기
                GPIO.output(Z_CW, GPIO.LOW)
                await asyncio.sleep(AUTO_Z_CW)
                GPIO.output(Z_CW, GPIO.HIGH)

                # 촬영 신호 시작 및 종료
                Shot_SIG = True
                await asyncio.sleep(SHOT_TIME)
                Shot_SIG = False

                GPIO.output(Z_CCW, GPIO.LOW)
                await asyncio.sleep(AUTO_Z_CCW)
                GPIO.output(Z_CCW, GPIO.HIGH)

                # 이 목표 위치를 처리했음을 플래그로 기록
                target_reached_flags[i] = True
                print(f"Target position {target_position} completed.")
                break  # 처리 완료 후 반복 종료

        # 마지막 목표 위치에 도달하면 동작 멈추고 리셋
        if posision_count >= 36:
            print("Last Position reached: Resetting X, Z axes.")
            Start_switch = False
            count_reset = True

        # 마지막 위치 기억
        last_posision_count = posision_count


async def main_loop():
    while True:
        await Auto_motion()
        await asyncio.sleep(0.1)  # 0.1초마다 Auto_motion 실행
        print(f"Now X axis Count: {posision_count}")


try:
    asyncio.run(main_loop())

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # GPIO 설정 초기화
