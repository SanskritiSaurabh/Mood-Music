# Mood_Music - AI-Driven Emotion-Based Music Player 🎵

## Overview
Mood_Music is an innovative AI-powered music player that recommends music based on the user's emotional state, aiming to promote mental wellness through personalized music therapy.

## Features
- 🎭 Real-time emotion detection using facial expressions
- 🎵 Dynamic playlist generation based on emotional state
- 🌍 Multi-language support
- 🎤 Artist-specific recommendations
- 👤 Facial landmark detection using MediaPipe
- 💻 Streamlit-based web interface

## Tech Stack
- Python 3.7+
- TensorFlow/Keras for emotion classification
- MediaPipe for facial landmark detection
- OpenCV for image processing
- Streamlit for web interface
- WebRTC for real-time video streaming

## Project Structure
```
Mood_Music/
├── data_collection.py      # Collect facial expression data
├── data_training.py       # Train the emotion recognition model
├── inference.py          # Real-time emotion detection
├── model.h5             # Trained emotion recognition model
├── labels.npy          # Emotion labels
└── playlist.py        # YouTube playlist generation
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Mood_Music.git
cd Mood_Music
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Data Collection
Run data collection script to gather facial expression data:
```bash
python data_collection.py
```
- Press 'ESC' to stop recording
- Data will be saved as .npy files

### 2. Model Training
Train the emotion recognition model:
```bash
python data_training.py
```
- The trained model will be saved as 'model.h5'
- Labels will be saved as 'labels.npy'

### 3. Running the Application
Start the Streamlit application:
```bash
streamlit run inference.py
```

### Using the Interface
1. Enter preferred language and artist name
2. Allow webcam access
3. The system will detect your emotion in real-time
4. Click "Recommend me songs" to get personalized YouTube playlist

## Model Architecture
- Input Layer: Facial landmarks features
- Hidden Layers: Dense layers (512, 256 units)
- Output Layer: Softmax classification for emotions
- Optimizer: RMSprop
- Loss: Categorical Crossentropy

## Future Developments
- 📱 Mobile application development
- 🎯 Enhanced emotion detection accuracy
- 🎵 Integration with multiple music platforms
- 💾 User preference storage
- 📊 Emotion tracking analytics

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

