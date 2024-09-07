import os
import time
import subprocess
from datetime import datetime

# 각 카메라의 사진을 저장할 경로 설정
save_folder_cam0 = '/home/SB01/Photo/CAM0'
save_folder_cam1 = '/home/SB01/Photo/CAM1'

# 디렉토리가 존재하지 않으면 생성
os.makedirs(save_folder_cam0, exist_ok=True)
os.makedirs(save_folder_cam1, exist_ok=True)


def take_photo(camera_id, save_folder):
    # 현재 시간을 기반으로 파일 이름 생성
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"camera_{camera_id}_{timestamp}.jpg"
    file_path = os.path.join(save_folder, filename)

    # libcamera-still을 사용하여 사진 촬영
    subprocess.run(['libcamera-still', '-t', '500', '-o',
                   file_path, '--camera', str(camera_id)])
    print(f"사진이 저장되었습니다: {file_path}")


# 무한 루프를 돌면서 매시간 사진 촬영
while True:
    take_photo(0, save_folder_cam0)  # 카메라 0번 사진 촬영 및 CAM0 폴더에 저장
    take_photo(1, save_folder_cam1)  # 카메라 1번 사진 촬영 및 CAM1 폴더에 저장

    # 1시간(3600초) 대기
    time.sleep(3600)
