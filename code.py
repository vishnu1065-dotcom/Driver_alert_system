import cv2
import mediapipe as mp
import time
from gpiozero import Buzzer

# -----------------------------
# BUZZER
# -----------------------------
BUZZER_PIN = 18
buzzer = Buzzer(BUZZER_PIN)

# -----------------------------
# MEDIAPIPE
# -----------------------------
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Eye landmark points
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# Time before alarm
EYE_CLOSED_TIME = 2.0

closed_start = None


def eye_ratio(landmarks, eye_points, width, height):
    p1 = landmarks[eye_points[0]]
    p2 = landmarks[eye_points[1]]
    p3 = landmarks[eye_points[2]]
    p4 = landmarks[eye_points[3]]
    p5 = landmarks[eye_points[4]]
    p6 = landmarks[eye_points[5]]

    x1, y1 = int(p1.x * width), int(p1.y * height)
    x2, y2 = int(p2.x * width), int(p2.y * height)
    x3, y3 = int(p3.x * width), int(p3.y * height)
    x4, y4 = int(p4.x * width), int(p4.y * height)
    x5, y5 = int(p5.x * width), int(p5.y * height)
    x6, y6 = int(p6.x * width), int(p6.y * height)

    vertical1 = ((x2-x6)**2 + (y2-y6)**2) ** 0.5
    vertical2 = ((x3-x5)**2 + (y3-y5)**2) ** 0.5
    horizontal = ((x1-x4)**2 + (y1-y4)**2) ** 0.5

    return (vertical1 + vertical2) / (2.0 * horizontal)


# -----------------------------
# CAMERA
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected!")
    exit()

print("Driver Alert System Started")
print("Press Q to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera frame error")
        break

    frame = cv2.flip(frame, 1)

    height, width, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    status = "ALERT"
    buzzer_status = "BUZZER OFF"

    if results.multi_face_landmarks:

        face = results.multi_face_landmarks[0]

        left_ratio = eye_ratio(
            face.landmark,
            LEFT_EYE,
            width,
            height
        )

        right_ratio = eye_ratio(
            face.landmark,
            RIGHT_EYE,
            width,
            height
        )

        eye_value = (left_ratio + right_ratio) / 2

        # Eye closed threshold
        if eye_value < 0.20:

            status = "EYES CLOSED"

            if closed_start is None:
                closed_start = time.time()

            closed_time = time.time() - closed_start

            if closed_time >= EYE_CLOSED_TIME:

                status = "DROWSINESS DETECTED!"
                buzzer_status = "BUZZER ON"

                buzzer.on()

            else:
                buzzer.off()

        else:

            closed_start = None
            buzzer.off()

    else:

        status = "NO FACE DETECTED"
        closed_start = None
        buzzer.off()

    # -----------------------------
    # DISPLAY
    # -----------------------------

    cv2.putText(
        frame,
        status,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 255) if "DROWSINESS" in status else (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        buzzer_status,
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255) if buzzer_status == "BUZZER ON" else (0, 255, 0),
        2
    )

    cv2.imshow("Driver Alert System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# -----------------------------
# CLEANUP
# -----------------------------

buzzer.off()
cap.release()
cv2.destroyAllWindows()
face_mesh.close()
