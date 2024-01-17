import cv2
import mediapipe as mp
import numpy as np

class HandGesture:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

        # Variables for drawing
        self.drawing_color = (0, 255, 0)  # Change color as needed
        self.drawing_thickness = 8
        self.mask = np.zeros((480, 640, 3), dtype=np.uint8)
        self.prev_coords = None
        self.erase = False

    def detect_finger_tips(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        finger_tips = {
            "thumb": None,
            "index": None
        }

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                height, width, _ = frame.shape
                # Get thumb tip coordinates
                thumb_tip = (int(landmarks[self.mp_hands.HandLandmark.THUMB_TIP].x * width),
                             int(landmarks[self.mp_hands.HandLandmark.THUMB_TIP].y * height))
                finger_tips["thumb"] = thumb_tip

                # Get index finger tip coordinates
                index_tip = (int(landmarks[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width),
                             int(landmarks[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height))
                finger_tips["index"] = index_tip

        return finger_tips

    def draw_on_mask(self, frame):
        finger_tips = self.detect_finger_tips(frame)
        thumb_tip = finger_tips["thumb"]
        index_tip = finger_tips["index"]

        if thumb_tip and index_tip:
            thumb_x, thumb_y = thumb_tip
            index_x, index_y = index_tip

            cv2.circle(frame, thumb_tip, 10, (0, 0, 250), 2)
            cv2.circle(frame, index_tip, 10, (0, 0, 250), 2)

            # Calculate distance between thumb and index finger tips
            distance = np.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2)
            
            # Set a threshold for fingertips touching
            touch_threshold = 30  # Adjust as needed

            if distance < touch_threshold:
                if self.erase:
                    cv2.circle(self.mask, index_tip, 90, (0, 0, 0), -1)
                else:
                    if self.prev_coords:
                        cv2.line(self.mask, self.prev_coords, index_tip, self.drawing_color, self.drawing_thickness)

                        # cv2.circle(frame, thumb_tip, 20, (0, 0, 250), 5)
                        # cv2.circle(frame, index_tip, 20, (0, 0, 250), 5)

                    self.prev_coords = index_tip

    def start_drawing(self):
        cap = cv2.VideoCapture(0)


        while True:
            ret, frame = cap.read()
            if not ret:
                break

            self.draw_on_mask(frame)
            frame = cv2.addWeighted(frame, 1, self.mask, 0.7, 0)  # Overlay mask on the frame

            fliped=cv2.flip(frame,1)
            cv2.imshow('Drawing', cv2.resize(fliped,(1440,960)))
            key = cv2.waitKey(1) & 0xFF

            if key == ord('e'):
                self.erase = not self.erase
                self.prev_coords = None

            if key == 27:  # ESC key to exit
                break

        cap.release()
        cv2.destroyAllWindows()

# Example usage:
hand_gesture = HandGesture()
hand_gesture.start_drawing()
