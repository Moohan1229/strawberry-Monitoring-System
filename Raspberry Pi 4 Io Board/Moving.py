import RPi.GPIO as GPIO
import time
import asyncio
import os
import subprocess
import sys
import requests
from datetime import datetime

# GPIO 핀 번호 설정
POS_SEN = 6
X_CW = 24
X_CCW = 25
Z_CW = 22
Z_CCW = 23

# GPIO 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(POS_SEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(X_CW, GPIO.OUT)
GPIO.setup(X_CCW, GPIO.OUT)
GPIO.setup(Z_CW, GPIO.OUT)
GPIO.setup(Z_CCW, GPIO.OUT)

# 변수 설정
position_count = 0
last_position_count = -1
Start_switch = False
count_reset = False
last_change_time = None
bug_Check = False
safety = False
No_movement_time = 500  # 50초 동안 움직임이 없으면 리셋
HOME_BACK = 300  # 리셋 시 홈 위치로 돌아가는 대기 시간
SHOT_TIME = 5  # 촬영 시간
tolerance = 1  # 오차 범위
target_positions = [40, 80, 120, 160, 200, 240,
                    280, 320, 360, 400, 440, 480, 520]  # 목표 위치
target_reached_flags = [False] * len(target_positions)  # 처리 여부 플래그

# Z, X 축 동작 시간
AUTO_Z_CW = 24  # 하강시간
AUTO_Z_CCW = 30  # 상승시간
AUTO_X_CW = 5
AUTO_X_CCW = 5

# 초기 상태 설정
GPIO.output(X_CW, GPIO.HIGH)
GPIO.output(X_CCW, GPIO.HIGH)
GPIO.output(Z_CW, GPIO.HIGH)
GPIO.output(Z_CCW, GPIO.HIGH)

# 카메라 저장 경로 설정
save_folder_cam0 = '/mnt/MonitoringData/CAM0'
save_folder_cam1 = '/mnt/MonitoringData/CAM1'

# 디렉토리가 존재하지 않으면 생성
os.makedirs(save_folder_cam0, exist_ok=True)
os.makedirs(save_folder_cam1, exist_ok=True)

# 특정 시간에 핀 제어 ---------------------------------------------------------------------------------


async def check_time():
    global Start_switch, safety
    current_time = datetime.now().strftime("%H:%M")

    if current_time == "08:00" and not Start_switch:
        Start_switch = True
        safety = True
        print("1번 핀 켜짐 (08시)")

    elif current_time == "16:47" and not Start_switch:
        Start_switch = True
        safety = True
        print("2번 핀 켜짐 (14시)")

# 안전 시스템 ----------------------------------------------------------------------------------------


async def safety_system():
    global bug_Check
    if safety:
        await asyncio.sleep(0.1)
        bug_Check = True

# 사진촬영 프로그램 ----------------------------------------------------------------------------------


async def take_photo(camera_id, save_folder):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"Photo_CAM{camera_id}_Time{timestamp}.jpg"
    file_path = os.path.join(save_folder, filename)

    # 사진 촬영
    subprocess.run(['libcamera-still', '-t', '500', '-o',
                   file_path, '--camera', str(camera_id)])
    print(f"사진이 저장되었습니다: {file_path}")

# Position count 업데이트 함수 -------------------------------------------------------------------------


async def update_position_count():
    global position_count, last_change_time
    current_time = time.time()

    if GPIO.input(POS_SEN) == GPIO.HIGH and not count_reset and Start_switch:
        position_count += 1
        last_change_time = current_time
        print(f"Position Count +1, Now Count = {position_count}")


# 자동운전 프로그램 ----------------------------------------------------------------------------------
async def Auto_motion():
    global position_count, Start_switch, count_reset, last_change_time, last_position_count, bug_Check, safety
    current_time = time.time()

    # Position Count 업데이트
    await update_position_count()

    if last_change_time and (current_time - last_change_time) > No_movement_time and not count_reset and Start_switch and bug_Check and safety:
        print("No movement detected for 50 seconds, resetting count.")
        count_reset = True
        sys.exit()

    if count_reset:
        position_count = 0
        GPIO.output(X_CW, GPIO.HIGH)
        await asyncio.sleep(1)
        GPIO.output(X_CCW, GPIO.LOW)
        GPIO.output(Z_CCW, GPIO.LOW)
        await asyncio.sleep(HOME_BACK)
        GPIO.output(X_CCW, GPIO.HIGH)
        GPIO.output(Z_CCW, GPIO.HIGH)
        GPIO.output(X_CW, GPIO.HIGH)
        GPIO.output(Z_CW, GPIO.HIGH)
        count_reset = False
        bug_Check = False

    if Start_switch and not count_reset:
        if position_count < 1250:
            GPIO.output(X_CW, GPIO.LOW)

        for i, target_position in enumerate(target_positions):
            if abs(position_count - target_position) <= tolerance and not target_reached_flags[i]:
                print(f"Target position {target_position} reached.")
                GPIO.output(X_CW, GPIO.HIGH)
                await asyncio.sleep(2)
                GPIO.output(Z_CW, GPIO.LOW)
                await asyncio.sleep(AUTO_Z_CW)
                GPIO.output(Z_CW, GPIO.HIGH)
                await asyncio.sleep(SHOT_TIME)
                # 사진 촬영
                await take_photo(0, save_folder_cam0)
                await take_photo(1, save_folder_cam1)
                response = requests.post(
                    "http://192.168.0.57:6866/signal", data={"signal": "True"})
                print(response.status_code)
                await asyncio.sleep(SHOT_TIME)

                GPIO.output(Z_CCW, GPIO.LOW)
                await asyncio.sleep(AUTO_Z_CCW)
                GPIO.output(Z_CCW, GPIO.HIGH)

                target_reached_flags[i] = True
                print(f"Target position {target_position} completed.")
                break

        if position_count >= 1250:
            print("Last Position reached: Resetting X, Z axes.")
            Start_switch = False
            bug_Check = False
            count_reset = True

        last_position_count = position_count

# 메인 루프 -----------------------------------------------------------------------------------------


async def main_loop():
    while True:
        await check_time()
        await Auto_motion()
        await safety_system()
        await asyncio.sleep(0.1)

        input_state = GPIO.input(6)
        print(f"GPIO {6}: {'HIGH' if input_state else 'LOW'}")

try:
    asyncio.run(main_loop())
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # GPIO 설정 초기화
