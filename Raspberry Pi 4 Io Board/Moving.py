import RPi.GPIO as GPIO
import time
import asyncio
# from Program.Pictutre take4 import shot_data

# Gpio Pin
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

# Variable Data
posision_count = 0
Start_switch = False
count_reset = False
Shot_SIG = False


async def Auto_motion():
    global posision_count, Start_switch, count_reset, Shot_SIG

    if GPIO.input(POS_SEN) == GPIO.HIGH:
        posision_count += 1
        print(f"posision Count +1 Now Count ={posision_count}")

    # shot complete and posision sensor reset , Y,Z home posision back
    if count_reset:
        posision_count = 0
        GPIO.output(X_CCW, GPIO.HIGH)
        GPIO.output(Z_CCW, GPIO.HIGH)
        await asyncio.sleep(30)  # async
        GPIO.output(X_CCW, GPIO.LOW)
        GPIO.output(Z_CCW, GPIO.LOW)
        count_reset = False

    # Auto Start and Auto Pictuture
    if Start_switch:
        GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 600:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 1200:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 1800:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 2400:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 3000:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 3600:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            GPIO.output(X_CW, GPIO.HIGH)

        if posision_count == 4200:
            GPIO.output(X_CW, GPIO.LOW)
            GPIO.output(Z_CW, GPIO.HIGH)
            await asyncio.sleep(30)
            GPIO.output(Z_CW, GPIO.LOW)
            Shot_SIG = True
            await asyncio.sleep(60)
            Shot_SIG = False
            GPIO.output(Z_CCW, GPIO.HIGH)
            await asyncio.sleep(60)
            GPIO.output(Z_CCW, GPIO.LOW)
            Start_switch = False
            count_reset = True


async def main_loop():
    while True:
        await Auto_motion()
        await asyncio.sleep(0.1)  # 비동기적으로 0.1초 대기
try:
    asyncio.run(main_loop())

except KeyboardInterrupt:
    pass

finally:
    # GPIO 설정 초기화
    GPIO.cleanup()
