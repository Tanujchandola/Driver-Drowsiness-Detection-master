import dlib
predictor_path = r"C:\Users\kosha\OneDrive\Desktop\Driver-Drowsiness-Detection-master\Driver-Drowsiness-Detection-master\shapePridict\shape_predictor_68_face_landmarks.dat"

try:
    predictor = dlib.shape_predictor(predictor_path)
    print("Predictor loaded successfully.")
except RuntimeError as e:
    print(f"Error loading predictor: {e}")
