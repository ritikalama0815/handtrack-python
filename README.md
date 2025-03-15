# Hand Tracking Mouse Control

 Overview
This project utilizes OpenCV, MediaPipe, and PyAutoGUI to enable mouse control through hand gestures. The program tracks the user's hand movements using a webcam and maps the index finger's position to control the mouse cursor. Additionally, a click is performed when the thumb and index finger come close together.

 Features
- Tracks hand movements using MediaPipe Hands.
- Moves the mouse cursor based on the index finger's position.
- Simulates a mouse click when the thumb and index finger come close together.
- Provides real-time feedback by displaying the processed video feed.

Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- MediaPipe
- PyAutoGUI

How It Works
1. Captures video feed from the webcam.
2. Uses MediaPipe to detect and track hand landmarks.
3. Maps the index finger position to screen coordinates and moves the mouse accordingly.
4. Detects proximity between the index finger and thumb to simulate a mouse click.
5. Displays a real-time video feed with hand landmarks.

## Running the Program
Run the script using:
->python hand_tracking_mouse.py

## Configuration
- The script is set to detect the index finger (landmark ID 8) for cursor movement.
- Clicking is triggered when the vertical distance between the thumb (landmark ID 4) and index finger (landmark ID 8) is less than 25 pixels.
- The script automatically adjusts to the screen resolution.

## Acknowledgments
This project leverages Google's MediaPipe for efficient hand tracking and OpenCV for real-time image processing.

