import RPi.GPIO as GPIO
import time
import asyncio

# Gpio Pin 설정
POS_SEN = 10
X_CW = 15
X_CCW = 16
Z_CW = 17
Z_CCW = 18

# Gpio Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(POS_SEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(X_CW, GPIO.OUT)
GPIO.setup(X_CCW, GPIO.OUT)
GPIO.setup(Z_CW, GPIO.OUT)
GPIO.setup(Z_CCW, GPIO.OUT)

# 변수 설정
posision_count = 0
Start_switch = False
count_reset = False
Shot_SIG = False
last_posision_count = 0
last_change_time = None
No_movement_time = 5  # 5초 동안 움직임이 없으면 리셋
AUTO_Z_CW = 5  # 기본 대기 시간 (초)
AUTO_Z_CCW = 5
AUTO_X_CW = 5
AUTO_X_CCW = 5
HOME_BACK = 10
SHOT_TIME = 3  # 촬영 시간

# 오차 범위 설정 (±50)
tolerance = 50

# 타겟 위치 배열
target_positions = [600, 1200, 1800, 2400, 3000, 3600, 4200]


async def Auto_motion():
    global posision_count, Start_switch, count_reset, Shot_SIG, last_posision_count, last_change_time, No_movement_time

    current_time = time.time()

    # 위치 센서가 감지되면 posision_count 증가
    if GPIO.input(POS_SEN) == GPIO.HIGH:
        posision_count += 1
        last_change_time = current_time
        print(f"Position Count +1, Now Count = {posision_count}")

    # 5초 동안 위치 변화가 없으면 count_reset 활성화
    if last_change_time and (current_time - last_change_time) > No_movement_time:
        print("No movement detected for 5 seconds, resetting count.")
        count_reset = True

    # 카운트 리셋 시 X, Z 좌표를 초기 위치로 되돌리기
    if count_reset:
        posision_count = 0
        GPIO.output(X_CCW, GPIO.HIGH)
        GPIO.output(Z_CCW, GPIO.HIGH)
        await asyncio.sleep(HOME_BACK)  # 비동기 대기
        GPIO.output(X_CCW, GPIO.LOW)
        GPIO.output(Z_CCW, GPIO.LOW)
        count_reset = False

    # 자동 시작이 설정된 경우
    if Start_switch:
        # 4200에 도달하기 전에는 X_CW 켜기
        if posision_count < 4200:
            GPIO.output(X_CW, GPIO.HIGH)

        # 목표 위치에 ±50 오차 허용
        for target_position in target_positions:
            if abs(posision_count - target_position) <= tolerance:
                GPIO.output(X_CW, GPIO.LOW)
                GPIO.output(Z_CW, GPIO.HIGH)
                await asyncio.sleep(AUTO_Z_CW)
                GPIO.output(Z_CW, GPIO.LOW)
                Shot_SIG = True
                await asyncio.sleep(SHOT_TIME)
                Shot_SIG = False
                GPIO.output(Z_CCW, GPIO.HIGH)
                await asyncio.sleep(AUTO_Z_CCW)
                GPIO.output(Z_CCW, GPIO.LOW)

                # 4200에 도달하면 동작 멈추고 리셋
                if target_position == 4200:
                    print("Last Posision : X,Z resetting.")
                    Start_switch = False
                    count_reset = True
                else:
                    # 4200이 아닌 경우 X_CW 다시 켜기
                    GPIO.output(X_CW, GPIO.HIGH)


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
    # GPIO 설정 초기화
    GPIO.cleanup()
