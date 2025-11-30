import cv2
import mediapipe as mp
import numpy as np



# does two are for the avrege to calculat the 
smile_history = []
window_size = 10

open_moth_history = []


baseline_height_distance = None  # distance de la bouche neutre
baseline_width_distance = None
neutral_history = [] 

# Load your emoji image (make sure it's in the same folder)
emoji1 = cv2.imread("img.png", cv2.IMREAD_UNCHANGED)
emoji2 = cv2.imread("naruto-angr.jpeg", cv2.IMREAD_UNCHANGED)
emoji3 = cv2.imread("download.jpeg", cv2.IMREAD_UNCHANGED)

# === Setup MediaPipe ===
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Create FaceMesh model once
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# === Start webcam ===
webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    success, img = webcam.read()
    if not success:
        break

    # Convert BGR → RGB for MediaPipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)
    fh, fw, _ = img.shape  # get frame height & width


    # Convert back to BGR for OpenCV display
    img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    landmarks_points = results.multi_face_landmarks
    # Draw ace mesh

    if landmarks_points :

        landmarks = landmarks_points[0].landmark 
        print('brahim',fh,fw)
        
        # two landmark from the corner to calculate the month width
        mouth_left = landmarks[61]
        mouth_right = landmarks[291]

        # two landmark from the top and buttom to calculat the height of the moth 

        mouth_top = landmarks[12]
        mouth_butoom  = landmarks[15]
        # FACE LANDMARK 

        face_left = landmarks[234]   # Left edge of face
        face_right = landmarks[454]  # Right edge of face


        mouth_height = np.sqrt((mouth_top.x - mouth_butoom.x)**2 + (mouth_top.y - mouth_butoom.y)**2)
        mouth_width = np.sqrt((mouth_right.x - mouth_left.x)**2 + (mouth_right.y - mouth_left.y)**2)
        face_width = np.sqrt((face_right.x - face_left.x)**2 + (face_right.y - face_left.y)**2)

        normalized_mouth_width = mouth_width / face_width
        normalized_mouth_height = mouth_height / face_width

        smile_history.append(normalized_mouth_width)
        if len(smile_history) > 10: 
            smile_history.pop(0)
        smile_avg = sum(smile_history) / len(smile_history)

        # moth open avreg 
        open_moth_history.append(normalized_mouth_height)
        if len(open_moth_history) > 10: 
            open_moth_history.pop(0)
        open_moth_avreg = sum(open_moth_history) / len(open_moth_history)

        # --- Ajout pour smile detection ---
        if baseline_width_distance is None:
                baseline_width_distance = normalized_mouth_width
        if baseline_height_distance is None:
                baseline_height_distance = normalized_mouth_height


        # width month  ration  for smile 

        smile_ratio = smile_avg / baseline_width_distance
        # moth open ration 
        open_moth_avreg = open_moth_avreg / baseline_height_distance



        print("Mouth width distance:", normalized_mouth_width, "Ratio:", smile_ratio)
        print("Mouth height distance:", normalized_mouth_height, "Ratio:", open_moth_avreg)


        if smile_ratio > 1.14:
            emoji_resized = cv2.resize(emoji1, (700, 400))
            cv2.imshow("Smile Emoji", emoji_resized)
        elif open_moth_avreg > 2.1 :
            emoji_resized = cv2.resize(emoji2, (700, 400))
            cv2.imshow("Smile Emoji", emoji_resized)        
        else:  
            emoji_resized = cv2.resize(emoji3, (700,400))
            cv2.imshow("Smile Emoji", emoji_resized) 
        
        # for face_landmarks in results.multi_face_landmarks:
        #     mp_drawing.draw_landmarks(
        #         image=img,
        #         landmark_list=face_landmarks,
        #         connections=mp_face_mesh.FACEMESH_TESSELATION,
        #         landmark_drawing_spec=None,
        #         connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
        #     )
    # Show result
    cv2.imshow("Face Mesh with Iris Detection", img)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()