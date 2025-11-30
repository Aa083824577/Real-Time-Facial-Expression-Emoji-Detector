# 😊 Real-Time Facial Expression Emoji Detector

A Python-based computer vision application that detects facial expressions in real-time and displays corresponding emojis using MediaPipe Face Mesh and OpenCV.

## ✨ Features

- 📹 **Real-time webcam detection** - Instant facial expression recognition
- 🎭 **Multiple expression detection** - Identifies smiling, open mouth (surprise/yelling), and neutral expressions
- 📏 **Normalized measurements** - Uses face-width normalization for consistent detection across different distances from camera
- 🎯 **Smooth detection algorithm** - Implements 10-frame moving average to reduce jitter and false positives
- 🖼️ **Visual feedback** - Displays corresponding emoji images for each detected expression
- ⚡ **Optimized performance** - Efficient landmark processing with MediaPipe

## 🎬 Demo

The system analyzes 468 facial landmarks to calculate mouth geometry and detect expressions with high accuracy.

## 📋 Prerequisites

- Python 3.12
- Webcam
- Windows/macOS/Linux

## 🚀 Installation

1. **Clone this repository:**
```bash
git clone https://github.com/yourusername/Real-Time-Facial-Expression-Emoji-Detector.git
cd Real-Time-Facial-Expression-Emoji-Detector
```

2. **Create a virtual environment:**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3.12 -m venv venv
source venv/bin/activate
```

3. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Add emoji images to the project folder:**
   - `img.png` - Smile emoji (displayed when smiling)
   - `naruto-angr.jpeg` - Surprised/angry emoji (displayed when mouth opens wide)
   - `download.jpeg` - Neutral emoji (default expression)

   > **Note:** You can use any images you prefer. Just ensure filenames match or update them in the code.

## 💻 Usage

1. **Activate your virtual environment:**
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

2. **Run the application:**
```bash
python smile-angry.py
```

3. **Using the detector:**
   - Allow webcam access when prompted
   - Position your face in front of the camera
   - The application displays two windows:
     - **Face Mesh Detection** - Shows your webcam feed with tracking
     - **Emoji Display** - Shows the corresponding emoji based on your expression
   - Press **'q'** to quit the application

4. **Deactivate virtual environment when done:**
```bash
deactivate
```



## 🔬 How It Works

### Detection Algorithm

The system uses **MediaPipe Face Mesh** to detect 468 3D facial landmarks and analyzes specific points to determine expressions:

**Key Landmarks:**
- Mouth corners: Landmarks **61** (left) and **291** (right)
- Mouth vertical: Landmarks **12** (top) and **15** (bottom)
- Face width: Landmarks **234** (left edge) and **454** (right edge)

**Processing Pipeline:**
1. Capture webcam frame
2. Convert BGR → RGB for MediaPipe processing
3. Detect face mesh and extract landmarks
4. Calculate mouth dimensions:
   ```
   mouth_width = distance(landmark_61, landmark_291)
   mouth_height = distance(landmark_12, landmark_15)
   face_width = distance(landmark_234, landmark_454)
   ```
5. Normalize measurements relative to face width
6. Apply 10-frame moving average for stability
7. Compare ratios to baseline (captured on first frame)
8. Display corresponding emoji based on thresholds

### Expression Thresholds

- **😊 Smile Detection:** `smile_ratio > 1.14` (mouth width increases by 14%)
- **😮 Open Mouth Detection:** `open_mouth_ratio > 2.1` (mouth height increases by 110%)
- **😐 Neutral:** Default when neither threshold is met

### Baseline Calibration

The system captures your neutral expression in the first frame and uses it as a reference point for all subsequent comparisons, ensuring personalized detection accuracy.

## ⚙️ Customization

### Adjusting Detection Sensitivity

You can fine-tune the detection thresholds in `smile-angry.py`:

```python
# Line ~119: Smile threshold (increase for less sensitive, decrease for more sensitive)
if smile_ratio > 1.14:  # Default: 1.14 (14% increase)

# Line ~122: Open mouth threshold
elif open_moth_avreg > 2.1:  # Default: 2.1 (110% increase)
```

### Changing Emoji Images

Replace the image files or update the filenames in the code:

```python
emoji1 = cv2.imread("your-smile-emoji.png", cv2.IMREAD_UNCHANGED)
emoji2 = cv2.imread("your-surprised-emoji.png", cv2.IMREAD_UNCHANGED)
emoji3 = cv2.imread("your-neutral-emoji.png", cv2.IMREAD_UNCHANGED)
```

### Adjusting Moving Average Window

Modify the smoothing by changing the window size (line ~6):

```python
window_size = 10  # Increase for smoother but slower response
```

## 🛠️ Troubleshooting

**Issue: Webcam not detected**
- Ensure no other application is using the webcam
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if you have multiple cameras
- Check webcam permissions in your OS settings

**Issue: Emoji images not loading**
- Verify emoji files are in the same directory as `smile-angry.py`
- Check filenames match exactly (case-sensitive)
- Ensure images are in supported formats (PNG, JPEG)

**Issue: Detection too sensitive/not sensitive enough**
- Wait a moment after starting - the first frame sets your baseline
- Start with a neutral expression when launching the app
- Adjust threshold values (see Customization section)

**Issue: Module import errors**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again
- Verify Python 3.12 is installed

## 📦 Dependencies

- `opencv-python==4.8.1.78` - Computer vision and webcam handling
- `mediapipe==0.10.9` - Face mesh detection and landmark tracking
- `numpy==1.26.2` - Numerical calculations for landmark processing

## 🔮 Future Enhancements

- [ ] Add more expressions (sad, angry, wink, eyebrow raise)
- [ ] Implement machine learning model for improved accuracy
- [ ] Overlay emoji directly on face instead of separate window
- [ ] Record and export expression timeline data to CSV



## 🙏 Acknowledgments

- [MediaPipe](https://google.github.io/mediapipe/) - Google's ML solution for face mesh detection
- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
- Inspired by real-time emotion detection research



⭐ **Star this repo if you find it helpful!**

**Thank you for checking out this project! If you have ideas or want to contribute, feel free to open an issue or submit a pull request!**
