import cv2
import face_recognition_script

# Открываем видео с камеры (0 - это первая камера, можно указать путь к файлу)
video_capture = cv2.VideoCapture(r'C:\Projects\openCV\env\video\1696500480KZF31_1726321574_151.mp4')

while True:
    # Чтение кадров с видео
    ret, frame = video_capture.read()

    # Конвертация изображения из формата BGR (используемого OpenCV) в формат RGB (используемый face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Находим все лица на текущем кадре
    face_locations = face_recognition_script.face_locations(rgb_frame)

    # Отображаем результат
    for (top, right, bottom, left) in face_locations:
        # Рисуем прямоугольник вокруг каждого найденного лица
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Показ кадра с распознанными лицами
    cv2.imshow('Video', frame)

    # Выход из цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
video_capture.release()
cv2.destroyAllWindows()
