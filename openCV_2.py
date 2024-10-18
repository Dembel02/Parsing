import os
import cv2
import face_recognition

# Set the path to the folder containing the videos
video_folder_path = '/path/to/videos'

# Set the path to the folder where you want to save the recognized faces
recognized_faces_folder_path = '/path/to/recognized_faces'

# Create the recognized faces folder if it doesn't exist
if not os.path.exists(recognized_faces_folder_path):
    os.makedirs(recognized_faces_folder_path)

# Load the face recognition model
face_recognition_model = face_recognition.FaceRecognition()

# Loop through all videos in the video folder
for video_file in os.listdir(video_folder_path):
    # Check if the file is a video file
    if video_file.endswith(('.mp4', '.avi', '.mov')):
        # Open the video file using OpenCV
        video_cap = cv2.VideoCapture(os.path.join(video_folder_path, video_file))

        # Initialize a counter for the recognized faces
        face_count = 0

        # Loop through each frame of the video
        while True:
            # Read a frame from the video
            ret, frame = video_cap.read()

            # If the frame is None, it means we've reached the end of the video
            if not ret:
                break

            # Convert the frame to RGB
            rgb_frame = frame[:, :, ::-1]

            # Detect faces in the frame
            face_locations = face_recognition_script.face_locations(rgb_frame)

            # Loop through each detected face
            for face_location in face_locations:
                # Extract the face from the frame
                face_image = rgb_frame[face_location[0]:face_location[2], face_location[3]:face_location[1]]

                # Save the face to a file
                face_file_path = os.path.join(recognized_faces_folder_path, f"face_{video_file}_{face_count}.jpg")
                cv2.imwrite(face_file_path, face_image)

                # Increment the face count
                face_count += 1

        # Release the video capture
        video_cap.release()