# # # Importing OpenCV Library for basic image processing functions

# # # Numpy for array related functions
# # import numpy as np
# # # Dlib for deep learning based Modules and face landmark detection
# # import dlib
# # # face_utils for basic operations of conversion
# # from imutils import face_utils

# # # Initializing the camera and taking the instance
# # cap = cv2.VideoCapture(0)

# # # Initializing the face detector and landmark detector
# # detector = dlib.get_frontal_face_detector()
# # predictor = dlib.shape_predictor(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/shapePridict/shape_predictor_68_face_landmarks.dat")

# # # Status marking for current state
# # sleep = 0
# # drowsy = 0
# # active = 0
# # status = ""
# # color = (0, 0, 0)

# # def compute(ptA, ptB):
# #     dist = np.linalg.norm(ptA - ptB)
# #     return dist

# # def blinked(a, b, c, d, e, f):
# #     up = compute(b, d) + compute(c, e)
# #     down = compute(a, f)
# #     ratio = up / (2.0 * down)

# #     # Checking if it is blinked
# #     if ratio > 0.25:
# #         return 2
# #     elif ratio > 0.21 and ratio <= 0.25:
# #         return 1
# #     else:
# #         return 0

# # while True:
# #     _, frame = cap.read()
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# #     faces = detector(gray)
# #     face_frame = frame.copy()  # Initialize face_frame with a copy of the current frame

# #     # Detected face in faces array
# #     for face in faces:
# #         x1 = face.left()
# #         y1 = face.top()
# #         x2 = face.right()
# #         y2 = face.bottom()

# #         # Draw rectangle around the face
# #         cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# #         landmarks = predictor(gray, face)
# #         landmarks = face_utils.shape_to_np(landmarks)

# #         # The numbers are actually the landmarks which will show eye
# #         left_blink = blinked(landmarks[36], landmarks[37], 
# #                              landmarks[38], landmarks[41], landmarks[40], landmarks[39])
# #         right_blink = blinked(landmarks[42], landmarks[43], 
# #                               landmarks[44], landmarks[47], landmarks[46], landmarks[45])


        
# #         # eye blick check hogaa
# #         if left_blink == 0 or right_blink == 0:
# #             sleep += 1
# #             drowsy = 0
# #             active = 0
# #             if sleep > 6:
# #                 status = "OHH YOU ARE SLEEPING!"
# #                 color = (0, 0, 255)

# #         elif left_blink == 1 or right_blink == 1:
# #             sleep = 0
# #             active = 0
# #             drowsy += 1
# #             if drowsy > 6:
# #                 status = "YOU ARE DROWSY!"
# #                 color = (255, 0, 0)

# #         else:
# #             drowsy = 0
# #             sleep = 0
# #             active += 1
# #             if active > 6:
# #                 status = "YOU ARE ACTIVE:)"
# #                 color = (0, 255, 0)
            
# #         cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

# #         for n in range(0, 68):
# #             (x, y) = landmarks[n]
# #             cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

# #     # Show frames
# #     cv2.imshow("Frame", frame)
# #     cv2.imshow("Result of detector", face_frame)
    
# #     key = cv2.waitKey(1)
# #     if key == 27:
# #         break

# # cap.release()
# # cv2.destroyAllWindows()



# # Importing OpenCV Library for basic image processing functions
# import cv2
# # Numpy for array related functions
# import numpy as np
# # Dlib for deep learning-based Modules and face landmark detection
# import dlib
# # face_utils for basic operations of conversion
# from imutils import face_utils
# # playsound for audio alert
# from playsound import playsound
# import time

# # Initializing the camera and taking the instance
# cap = cv2.VideoCapture(0)

# # Initializing the face detector and landmark detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/shapePridict/shape_predictor_68_face_landmarks.dat")

# # Status marking for current state
# sleep = 0
# drowsy = 0
# active = 0
# status = ""
# color = (0, 0, 0)

# last_alert_time = 0  # To avoid repeated alerts within a short period


# def compute(ptA, ptB):
#     dist = np.linalg.norm(ptA - ptB)
#     return dist


# def blinked(a, b, c, d, e, f):
#     up = compute(b, d) + compute(c, e)
#     down = compute(a, f)
#     ratio = up / (2.0 * down)

#     # Checking if it is blinked
#     if ratio > 0.25:
#         return 2
#     elif ratio > 0.21 and ratio <= 0.25:
#         return 1
#     else:
#         return 0


# def play_siren():
#     """Plays the siren sound if drowsiness or sleep is detected."""    
#     global last_alert_time
#     if time.time() - last_alert_time > 5:  # 5-second delay between alerts
#         playsound(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/siron.mp3")
#         last_alert_time = time.time()


# while True:
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = detector(gray)
#     face_frame = frame.copy()  # Initialize face_frame with a copy of the current frame

#     # Detected face in faces array
#     for face in faces:
#         x1 = face.left()
#         y1 = face.top()
#         x2 = face.right()
#         y2 = face.bottom()

#         # Draw rectangle around the face
#         cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#         landmarks = predictor(gray, face)
#         landmarks = face_utils.shape_to_np(landmarks)

#         # The numbers are actually the landmarks which will show eye
#         left_blink = blinked(landmarks[36], landmarks[37],
#                              landmarks[38], landmarks[41], landmarks[40], landmarks[39])
#         right_blink = blinked(landmarks[42], landmarks[43],
#                               landmarks[44], landmarks[47], landmarks[46], landmarks[45])

#         # Check for eye status
#         if left_blink == 0 or right_blink == 0:
#             sleep += 1
#             drowsy = 0
#             active = 0
#             if sleep > 6:
#                 status = "OHH YOU ARE SLEEPING!"
#                 color = (0, 0, 255)
#                 play_siren()  # Play siren for sleep detection

#         elif left_blink == 1 or right_blink == 1:
#             sleep = 0
#             active = 0
#             drowsy += 1
#             if drowsy > 6:
#                 status = "YOU ARE DROWSY!"
#                 color = (255, 0, 0)
#                 play_siren()  # Play siren for drowsiness detection

#         else:
#             drowsy = 0
#             sleep = 0
#             active += 1
#             if active > 6:
#                 status = "YOU ARE ACTIVE:)"
#                 color = (0, 255, 0)

#         cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

#         for n in range(0, 68):
#             (x, y) = landmarks[n]
#             cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

#     # Show frames
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Result of detector", face_frame)

#     key = cv2.waitKey(1)
#     if key == 27:  # Press 'Esc' to exit
#         break

# cap.release()
# cv2.destroyAllWindows()




# # Importing required libraries
# import cv2
# import numpy as np
# import dlib
# from imutils import face_utils
# from playsound import playsound
# import threading
# import time

# # Initializing the camera and taking the instance
# cap = cv2.VideoCapture(0)

# # Initializing the face detector and landmark detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/shapePridict/shape_predictor_68_face_landmarks.dat")

# # Status marking for current state
# sleep = 0
# drowsy = 0
# active = 0
# status = ""
# color = (0, 0, 0)
# siren_thread = None  # To control the siren thread
# stop_siren = False  # To signal the siren to stop


# def compute(ptA, ptB):
#     dist = np.linalg.norm(ptA - ptB)
#     return dist


# def blinked(a, b, c, d, e, f):
#     up = compute(b, d) + compute(c, e)
#     down = compute(a, f)
#     ratio = up / (2.0 * down)

#     # Checking if it is blinked
#     if ratio > 0.25:
#         return 2
#     elif ratio > 0.21 and ratio <= 0.25:
#         return 1
#     else:
#         return 0


# def play_siren():
#     """Plays the siren sound in a separate thread."""
#     global stop_siren
#     while not stop_siren:
#         playsound(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/siron.mp3")
#         time.sleep(0.5)  # Small delay to prevent overlapping playback


# while True:
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = detector(gray)
#     face_frame = frame.copy()  # Initialize face_frame with a copy of the current frame

#     # Detected face in faces array
#     for face in faces:
#         x1 = face.left()
#         y1 = face.top()
#         x2 = face.right()
#         y2 = face.bottom()

#         # Draw rectangle around the face
#         cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#         landmarks = predictor(gray, face)
#         landmarks = face_utils.shape_to_np(landmarks)

#         # The numbers are actually the landmarks which will show eye
#         left_blink = blinked(landmarks[36], landmarks[37],
#                              landmarks[38], landmarks[41], landmarks[40], landmarks[39])
#         right_blink = blinked(landmarks[42], landmarks[43],
#                               landmarks[44], landmarks[47], landmarks[46], landmarks[45])

#         # Check for eye status
#         if left_blink == 0 or right_blink == 0:
#             sleep += 1
#             drowsy = 0
#             active = 0
#             if sleep > 6:
#                 status = "OHH YOU ARE SLEEPING!"
#                 color = (0, 0, 255)
#                 if siren_thread is None or not siren_thread.is_alive():
#                     stop_siren = False
#                     siren_thread = threading.Thread(target=play_siren)
#                     siren_thread.start()

#         elif left_blink == 1 or right_blink == 1:
#             sleep = 0
#             active = 0
#             drowsy += 1
#             if drowsy > 6:
#                 status = "YOU ARE DROWSY!"
#                 color = (255, 0, 0)
#                 if siren_thread is None or not siren_thread.is_alive():
#                     stop_siren = False
#                     siren_thread = threading.Thread(target=play_siren)
#                     siren_thread.start()

#         else:
#             drowsy = 0
#             sleep = 0
#             active += 1
#             if active > 6:
#                 status = "YOU ARE ACTIVE:)"
#                 color = (0, 255, 0)
#                 stop_siren = True  # Stop the siren if the user is active
#                 if siren_thread and siren_thread.is_alive():
#                     siren_thread.join()  # Ensure the thread is stopped

#         cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

#         for n in range(0, 68):
#             (x, y) = landmarks[n]
#             cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

#     # Show frames
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Result of detector", face_frame)

#     key = cv2.waitKey(1)
#     if key == 27:  # Press 'Esc' to exit
#         stop_siren = True  # Stop the siren before exiting
#         if siren_thread and siren_thread.is_alive():
#             siren_thread.join()  # Ensure the thread is stopped
#         break

# cap.release()
# cv2.destroyAllWindows()


# # Importing required libraries
# import cv2
# import numpy as np
# import dlib
# from imutils import face_utils
# from playsound import playsound
# import threading
# import time

# # Initializing the camera and taking the instance
# cap = cv2.VideoCapture(0)

# # Initializing the face detector and landmark detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/shapePridict/shape_predictor_68_face_landmarks.dat")

# # Status marking for current state
# sleep = 0
# drowsy = 0
# active = 0
# status = ""
# color = (0, 0, 0)
# siren_thread = None  # To control the siren thread
# stop_siren = threading.Event()  # Thread-safe flag for stopping the siren


# def compute(ptA, ptB):
#     return np.linalg.norm(ptA - ptB)


# def blinked(a, b, c, d, e, f):
#     up = compute(b, d) + compute(c, e)
#     down = compute(a, f)
#     ratio = up / (2.0 * down)

#     # Checking if it is blinked
#     if ratio > 0.25:
#         return 2
#     elif ratio > 0.21 and ratio <= 0.25:
#         return 1
#     else:
#         return 0


# def play_siren():
#     """Plays the siren sound in a separate thread."""
#     while not stop_siren.is_set():
#         playsound(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/drawsy.mp3")


# while True:
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = detector(gray)
#     face_frame = frame.copy()  # Initialize face_frame with a copy of the current frame

#     # Detected face in faces array
#     for face in faces:
#         x1 = face.left()
#         y1 = face.top()
#         x2 = face.right()
#         y2 = face.bottom()

#         # Draw rectangle around the face
#         cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#         landmarks = predictor(gray, face)
#         landmarks = face_utils.shape_to_np(landmarks)

#         # The numbers are actually the landmarks which will show eye
#         left_blink = blinked(landmarks[36], landmarks[37],
#                              landmarks[38], landmarks[41], landmarks[40], landmarks[39])
#         right_blink = blinked(landmarks[42], landmarks[43],
#                               landmarks[44], landmarks[47], landmarks[46], landmarks[45])

#         # Check for eye status
#         if left_blink == 0 or right_blink == 0:
#             sleep += 1
#             drowsy = 0
#             active = 0
#             if sleep > 6:
#                 status = "OHH YOU ARE SLEEPING!"
#                 color = (0, 0, 255)
#                 if siren_thread is None or not siren_thread.is_alive():
#                     stop_siren.clear()
#                     siren_thread = threading.Thread(target=play_siren)
#                     siren_thread.start()

#         elif left_blink == 1 or right_blink == 1:
#             sleep = 0
#             active = 0
#             drowsy += 1
#             if drowsy > 6:
#                 status = "YOU ARE DROWSY!"
#                 color = (255, 0, 0)
#                 if siren_thread is None or not siren_thread.is_alive():
#                     stop_siren.clear()
#                     siren_thread = threading.Thread(target=play_siren)
#                     siren_thread.start()

#         else:
#             drowsy = 0
#             sleep = 0
#             active += 1
#             if active > 6:
#                 status = "YOU ARE ACTIVE:)"
#                 color = (0, 255, 0)
#                 stop_siren.set()  # Signal the siren thread to stop
#                 if siren_thread and siren_thread.is_alive():
#                     siren_thread.join()  # Ensure the thread is stopped

#         cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

#         for n in range(0, 68):
#             (x, y) = landmarks[n]
#             cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

#     # Show frames
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Result of detector", face_frame)

#     key = cv2.waitKey(1)
#     if key == 27:  # Press 'Esc' to exit
#         stop_siren.set()  # Stop the siren before exiting
#         if siren_thread and siren_thread.is_alive():
#             siren_thread.join()  # Ensure the thread is stopped
#         break

# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# import dlib
# from imutils import face_utils
# from playsound import playsound
# import threading
# import time

# # Initializing the camera and taking the instance
# cap = cv2.VideoCapture(0)

# # Initializing the face detector and landmark detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/shapePridict/shape_predictor_68_face_landmarks.dat")

# # Status marking for current state
# sleep = 0
# drowsy = 0
# active = 0
# status = ""
# color = (0, 0, 0)
# drowsy_thread = None
# sleepy_thread = None
# stop_drowsy_siren = threading.Event()
# stop_sleepy_siren = threading.Event()


# def compute(ptA, ptB):
#     return np.linalg.norm(ptA - ptB)


# def blinked(a, b, c, d, e, f):
#     up = compute(b, d) + compute(c, e)
#     down = compute(a, f)
#     ratio = up / (2.0 * down)

#     # Checking if it is blinked
#     if ratio > 0.25:
#         return 2
#     elif ratio > 0.21 and ratio <= 0.25:
#         return 1
#     else:
#         return 0


# def play_drowsy_siren():
#     """Plays the drowsy siren sound."""
#     while not stop_drowsy_siren.is_set():
#         playsound(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/drawsy.mp3")


# def play_sleepy_siren():
#     """Plays the sleepy siren sound."""
#     while not stop_sleepy_siren.is_set():
#         playsound(r"C:/Users/kosha/OneDrive/Desktop/Driver-Drowsiness-Detection-master/Driver-Drowsiness-Detection-master/sleepy.mp3")


# while True:
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = detector(gray)
#     face_frame = frame.copy()

#     for face in faces:
#         x1 = face.left()
#         y1 = face.top()
#         x2 = face.right()
#         y2 = face.bottom()

#         # Draw rectangle around the face
#         cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#         landmarks = predictor(gray, face)
#         landmarks = face_utils.shape_to_np(landmarks)

#         # The numbers are actually the landmarks which will show eye
#         left_blink = blinked(landmarks[36], landmarks[37],
#                              landmarks[38], landmarks[41], landmarks[40], landmarks[39])
#         right_blink = blinked(landmarks[42], landmarks[43],
#                               landmarks[44], landmarks[47], landmarks[46], landmarks[45])

#         # Check for eye status
#         if left_blink == 0 or right_blink == 0:
#             sleep += 1
#             drowsy = 0
#             active = 0
#             if sleep > 6:
#                 status = "OHH YOU ARE SLEEPING!"
#                 color = (0, 0, 255)
#                 if sleepy_thread is None or not sleepy_thread.is_alive():
#                     stop_sleepy_siren.clear()
#                     sleepy_thread = threading.Thread(target=play_sleepy_siren)
#                     sleepy_thread.start()

#         elif left_blink == 1 or right_blink == 1:
#             sleep = 0
#             active = 0
#             drowsy += 1
#             if drowsy > 6:
#                 status = "YOU ARE DROWSY!"
#                 color = (255, 0, 0)
#                 if drowsy_thread is None or not drowsy_thread.is_alive():
#                     stop_drowsy_siren.clear()
#                     drowsy_thread = threading.Thread(target=play_drowsy_siren)
#                     drowsy_thread.start()

#         else:
#             drowsy = 0
#             sleep = 0
#             active += 1
#             if active > 6:
#                 status = "YOU ARE ACTIVE :)"
#                 color = (0, 255, 0)
#                 stop_drowsy_siren.set()
#                 stop_sleepy_siren.set()
#                 if drowsy_thread and drowsy_thread.is_alive():
#                     drowsy_thread.join()
#                 if sleepy_thread and sleepy_thread.is_alive():
#                     sleepy_thread.join()

#         cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

#         for n in range(0, 68):
#             (x, y) = landmarks[n]
#             cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

#     # Show frames
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Result of detector", face_frame)

#     key = cv2.waitKey(1)
#     if key == 27:  # Press 'Esc' to exit
#         stop_drowsy_siren.set()
#         stop_sleepy_siren.set()
#         if drowsy_thread and drowsy_thread.is_alive():
#             drowsy_thread.join()
#         if sleepy_thread and sleepy_thread.is_alive():
#             sleepy_thread.join()
#         break

# cap.release()
# cv2.destroyAllWindows()


# -------------------------------------


import cv2
import numpy as np
import dlib
from imutils import face_utils
from playsound import playsound
import threading

# Initializing the camera and taking the instance
cap = cv2.VideoCapture(0)

# Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"../Driver-Drowsiness-Detection-master/shapePridict/shape_predictor_68_face_landmarks.dat")

# Status marking for current state
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)
sound_thread = None
stop_sound = threading.Event()


def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # Checking if it is blinked
    if ratio > 0.25:
        return 2
    elif ratio > 0.21 and ratio <= 0.25:
        return 1
    else:
        return 0


def play_sound(file_path):
    """Plays the given sound file."""
    while not stop_sound.is_set():
        playsound(file_path)


def start_new_sound(file_path):
    """Stops the current sound thread and starts a new one."""
    global sound_thread
    stop_sound.set()  # Signal any current sound to stop
    if sound_thread and sound_thread.is_alive():
        sound_thread.join()  # Ensure the previous thread stops
    stop_sound.clear()  # Reset the stop flag for the new thread
    sound_thread = threading.Thread(target=play_sound, args=(file_path,))
    sound_thread.start()


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    face_frame = frame.copy()

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # Draw rectangle around the face
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36], landmarks[37],
                             landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43],
                              landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        # Check for eye status
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                if status != "SLEEPY":  # Prevent restarting sound if already in this state
                    status = "SLEEPY"
                    color = (0, 0, 255)
                    start_new_sound(r"../Driver-Drowsiness-Detection-master/sleepy.mp3")

        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                if status != "DROWSY":  # Prevent restarting sound if already in this state
                    status = "DROWSY"
                    color = (255, 0, 0)
                    start_new_sound(r"../Driver-Drowsiness-Detection-master/drawsy.mp3")

        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                if status != "ACTIVE":  # Prevent restarting sound if already in this state
                    status = "ACTIVE"
                    color = (0, 255, 0)
                    stop_sound.set()  # Stop any ongoing sound
                    if sound_thread and sound_thread.is_alive():
                        sound_thread.join()  # Ensure the thread stops

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    # Show frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        stop_sound.set()
        if sound_thread and sound_thread.is_alive():
            sound_thread.join()
        break

cap.release()
cv2.destroyAllWindows()
