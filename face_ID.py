# import cv2
# import face_recognition
# import os



# # Путь к входному видеофайлу и папке для сохранения
# input_video_path = r'C:\Projects\openCV\env\video\2024.09.14.mp4'
# output_folder = r'C:\Projects\openCV\env\face'
# output_video_path = os.path.join(output_folder, 'processed_video.mp4')

# # Создание папки для сохранения, если её не существует
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # Открытие видеофайла
# video_capture = cv2.VideoCapture(input_video_path)
# if not video_capture.isOpened():
#     print("Ошибка при открытии видеофайла.")
#     exit()
# # # Задайте желаемое разрешение
# # target_width = 640  # Ширина
# # target_height = 480  # Высота

# # Получение информации о видео
# fps = video_capture.get(cv2.CAP_PROP_FPS)
# width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Создание объекта для записи видео
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# # Обработка видеофайла
# while True:
#     ret, frame = video_capture.read()
#     if not ret:
#         break

#     # Конвертация изображения в формат, который понимает face_recognition
#     rgb_frame = frame[:, :, ::-1]

#     # Поиск лиц на текущем кадре
#     face_locations = face_recognition.face_locations(rgb_frame)

#     # Если лица найдены, сохраняем кадр
#     if face_locations:
#         out.write(frame)

# # Освобождение ресурсов
# video_capture.release()
# out.release()
# cv2.destroyAllWindows()

# print(f"Видео сохранено в {output_video_path}")

import cv2
import face_recognition
import os

# Путь к входному видеофайлу и папке для сохранения
input_video_path = r'C:\Projects\openCV\env\video\IMG_5158.MOV'
output_folder = r'C:\Projects\openCV\env\face'
output_video_path = os.path.join(output_folder, 'processed_video.mp4')

# Создание папки для сохранения, если её не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Открытие видеофайла
video_capture = cv2.VideoCapture(input_video_path)
if not video_capture.isOpened():
    print("Ошибка при открытии видеофайла.")
    exit()

# Получение информации о видео
fps = video_capture.get(cv2.CAP_PROP_FPS)
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Создание объекта для записи видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Обработка видеофайла
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Уменьшение разрешения для более быстрой обработки
    frame = cv2.resize(frame, (640, 480))  # Уменьшите размер по необходимости
    rgb_frame = frame[:, :, ::-1]

    # Поиск лиц на текущем кадре
    face_locations = face_recognition.face_locations(rgb_frame)

    # Если лица найдены, сохраняем кадр
    if face_locations:
        out.write(frame)

# Освобождение ресурсов
video_capture.release()
out.release()
cv2.destroyAllWindows()

print(f"Видео сохранено в {output_video_path}")
