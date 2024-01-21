# HandMotionPainter - Virtual Drawing with OpenCV and MediaPipe

This Python script utilizes OpenCV and MediaPipe to enable drawing on a canvas using hand gestures detected from a webcam feed. It allows users to draw lines or erase on a transparent canvas by using their index finger tip. Additionally, drawing starts only when the index finger tip and thumb tip are touching.

## Features

- **Hand Gesture Drawing:** Detects hand gestures using MediaPipe and draws lines on a canvas.
- **Index Finger Tip Detection:** Tracks the index finger tip to draw lines.
- **Thumb Tip Gesture:** Utilizes thumb tip and index finger tip proximity to initiate or stop drawing.
- **Eraser Functionality:** Switch between drawing and erasing modes.

## Requirements

- Python 3.x
- OpenCV (cv2)
- Mediapipe
- NumPy

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abd-alim/HandMotionPainter
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

A webcam feed window will open. Perform hand gestures with your index finger and thumb to draw or erase on the screen.

## Configuration

Customize your drawing experience by adjusting the following parameters in the `hand_gesture_drawing.py` script:

- **drawing_color**: Adjust the color of the drawing (default is green).
- **drawing_thickness**: Set the thickness of the lines to be drawn.
- **touch_threshold**: Set the proximity threshold for finger tips touching.

Feel free to experiment with these settings to achieve the desired drawing experience.

## Contributions

Contributions are welcome! If you want to contribute to this project, please open an issue first to discuss potential changes or additions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy drawing! 🎨✨
