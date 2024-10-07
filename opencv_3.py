import cv2
import face_recognition

# Загрузите видеофайл
video = cv2.VideoCapture(r'C:\Projects\openCV\env\video\doc_2024-09-14_19-31-55.mp4')

# Инициализируйте список лиц и соответствующих им идентификаторов (человека)
known_face_encodings = []
known_face_names = []

# Функция сохранения лиц и идентификаторов из камеры
def save_known_faces():
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        rgb_frame = frame[:, :, ::-1]  # Конвертация BGR в RGB
        face_locations = face_recognition.face_locations(rgb_frame)

        if len(face_locations) == 0:
            print(f"Лица не найдены на текущем кадре {frame_count}.")
            # Сохранение текущего кадра для отладки
            cv2.imwrite(f'frame_no_faces_{frame_count}.jpg', frame)
            frame_count += 1
            continue  # Пропускаем текущий кадр, если лица не найдены

        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)

            name = input('Введите имя человека: ')
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
            print(f'Имя сохранено: {name}')

        frame_count += 1

save_known_faces()

# Выход
cv2.destroyAllWindows()
video.release()
