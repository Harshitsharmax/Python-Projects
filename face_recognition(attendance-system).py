"""
Facial Recognition and Attendance Monitoring System

This Python script uses the face_recognition library to recognize faces in a live video stream from a webcam. It compares the faces with known faces and records the attendance of the recognized individuals in a CSV file.

Requirements:
- Python 3.x
- face_recognition library (install using 'pip install face_recognition')
- OpenCV library (install using 'pip install opencv-python')
- numpy library (install using 'pip install numpy')

Usage:
1. Place images of the known faces in the 'faces' directory.
2. Run the script. It will open a live video stream from the webcam.
3. The script will recognize faces and mark attendance in a CSV file named with the current date.

"""

import face_recognition
import cv2
import csv
import numpy as np
from datetime import datetime

# Initialize video capture from the default webcam
video_capture = cv2.VideoCapture(0)

# Load known faces and their encodings
harshit_img = face_recognition.load_image_file("faces/harshit.jpeg")
harshit_encoding = face_recognition.face_encodings(harshit_img)[0]

robin_img = face_recognition.load_image_file("faces/robin.png")
robin_encoding = face_recognition.face_encodings(robin_img)[0]

known_face_encodings = [harshit_encoding, robin_encoding]
known_face_names = ["Harshit", "Robin"]

# List of expected students
students = known_face_names.copy()

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open a CSV file for attendance recording
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Main loop for capturing and processing video frames
while True:
    # Capture video frame-by-frame
    _, frame = video_capture.read()

    # Resize the frame to improve performance
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through each face found in the frame
    for face_encoding in face_encodings:
        # Compare the face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        # If a match is found, get the name of the recognized person
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Add the text if a person is present
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + "Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

                # Update the list of students present and record the attendance
                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M%S")
                    lnwriter.writerow([name, current_time])

    # Display the frame with attendance information
    cv2.imshow("Attendance", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close the CSV file
video_capture.release()
cv2.destroyAllWindows()
f.close()
