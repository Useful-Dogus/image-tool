import cv2
import os
import numpy as np
from PIL import Image, ExifTags

def rotate_image(img):
    # EXIF 데이터에서 회전 정보를 읽어 이미지 회전
    try:
        exif = img._getexif()
        if exif:
            for tag, value in exif.items():
                if tag == 274:  # Orientation 태그
                    if value == 3:
                        img = img.rotate(180, expand=True)
                    elif value == 6:
                        img = img.rotate(270, expand=True)
                    elif value == 8:
                        img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # EXIF 데이터가 없거나 오류가 발생한 경우
        pass
    return img

def generate_sequence_video(folder_path, output_name, duration):
    # 이미지 파일 목록
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()  # 파일 이름 순으로 정렬

    # 가장 큰 이미지의 크기 추적
    max_width, max_height = 0, 0
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)

        # 이미지 회전 (EXIF 데이터 처리)
        img = rotate_image(img)

        img_width, img_height = img.size
        max_width = max(max_width, img_width)
        max_height = max(max_height, img_height)

    # 비디오의 최대 해상도는 가장 큰 이미지 크기를 기준으로 설정
    max_size = (max_width, max_height)

    # 비디오 저장을 위한 초기 설정
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4v 코덱
    output_path = os.path.join(folder_path, f"{output_name}.mp4")
    video_writer = cv2.VideoWriter(output_path, fourcc, 30.0, max_size)

    # 각 이미지 처리
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)

        # 이미지 회전 (EXIF 데이터 처리)
        img = rotate_image(img)

        # 이미지 크기 비율 유지하면서 최대 크기로 확대
        img_width, img_height = img.size
        ratio = min(max_size[0] / img_width, max_size[1] / img_height)  # 확대 비율 계산
        new_size = (int(img_width * ratio), int(img_height * ratio))  # 새로운 크기

        img = img.resize(new_size, Image.Resampling.LANCZOS)

        # 검정색 여백으로 비율 맞추기
        new_img = Image.new("RGB", max_size, (0, 0, 0))  # 검정색 배경
        img_width, img_height = img.size
        new_img.paste(img, ((max_size[0] - img_width) // 2, (max_size[1] - img_height) // 2))  # 중앙 정렬

        # 이미지를 OpenCV가 처리할 수 있는 배열로 변환
        frame = cv2.cvtColor(np.array(new_img), cv2.COLOR_RGB2BGR)

        # 프레임을 비디오에 추가
        for _ in range(duration // 33):  # 30fps 기준으로 프레임 반복 추가 (지속 시간 맞추기)
            video_writer.write(frame)

    # 비디오 파일 저장
    video_writer.release()
    print(f"🎥 Video saved at {output_path}")

if __name__ == "__main__":
    folder_path = input("📂 Enter the absolute path of the image folder: ").strip()
    output_name = input("📄 Enter the output filename (without extension) (default: sequence): ").strip() or "sequence"
    duration = input("⏳ Enter frame duration in milliseconds (default: 500): ").strip()

    try:
        duration = int(duration) if duration else 500
    except ValueError:
        print("⚠️ Invalid duration input. Using default 500ms.")

    generate_sequence_video(folder_path, output_name, duration)
