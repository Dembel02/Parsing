import cv2
import face_recognition_script

# Загрузите видеофайл
video = cv2.VideoCapture('video.mp4')  # замените 'video.mp4' на путь к вашему видео

# Инициализируйте список лиц и соответствующих им идентификаторов (человека)
faces = []
known_face_encodings = []
known_face_names = []

# функция сохранения лиц и идентификаторов из камеры
def save_known_faces():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition_script.face_locations(rgb_frame)
        face_encodings = face_recognition_script.face_encodings(rgb_frame, face_locations)
        for face_encoding in face_encodings:
            faces.append(face_encoding)
        for (top, right, bottom, left), faceEncoding in zip(face_locations, face_encodings):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            name = input('Введите имя человека:')
            known_face_encodings.append(faceEncoding)
            known_face_names.append(name)
            print(f'Имя сохранено: {name}')

save_known_faces()

# функция распознавания лиц на видео
def detect_faces():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition_script.face_locations(rgb_frame)
        face_encodings = face_recognition_script.face_encodings(rgb_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition_script.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            face_names.append(name)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 10, top + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

detect_faces()

# выход
cv2.destroyAllWindows()
video.release()