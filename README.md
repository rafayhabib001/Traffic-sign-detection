# Traffic-sign-detection
# 🚦 Traffic Sign Detection System

An AI-powered web application that detects and classifies traffic signs from images using a deep learning model.

---

## 📌 Project Overview

This project is designed to identify traffic signs in images using a trained deep learning model (YOLOv8).  
Users can upload an image, and the system will automatically detect and highlight traffic signs along with confidence scores.

---

## 🎯 Features

- 📷 Upload image for detection  
- 🤖 AI-based traffic sign recognition  
- 📊 Displays bounding boxes with confidence score  
- 🌐 Simple and user-friendly web interface  
- ⚡ Fast and accurate predictions  

---

## 🛠️ Technologies Used

- **Backend:** Python  
- **Frontend:** HTML, CSS  
- **Model:** YOLOv12m (Ultralytics)  
- **Environment:** Google Colab (for training)  

---

## 🧠 How It Works

1. User uploads an image  
2. Image is sent to the backend  
3. YOLOv8 model processes the image  
4. Traffic signs are detected and labeled  
5. Result is displayed with bounding boxes  

---

## 📸 Sample Output

Detection example showing:
- Stop sign detected with high confidence  
- Speed limit sign detected  

---

## 🚀 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/rafayhabib001/Traffic-sign-detection.git

# Navigate to project folder
cd Traffic-sign-detection

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
