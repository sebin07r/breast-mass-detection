# Breast Mass Detection using YOLOv11

This project presents an **AI-powered breast mass detection system** built using the **YOLOv11 object detection framework**. The system analyzes mammographic images and automatically detects potential breast masses by identifying suspicious regions within the image.

By leveraging **deep learning and computer vision techniques**, the model is trained to recognize patterns associated with breast abnormalities and accurately localize them using bounding boxes. This project demonstrates how modern AI models can assist in **medical image analysis and early breast cancer detection**.

---

## How It Works

The system follows an end-to-end deep learning workflow:

### 1. Data Preparation
Mammogram images are preprocessed and annotated using the **YOLO annotation format**, where bounding boxes are created around breast mass regions.

### 2. Model Training
The **YOLOv11 object detection model** is trained on the annotated dataset to learn spatial patterns and visual features related to breast masses.

### 3. Model Inference
The trained model processes new mammogram images and predicts the location of potential breast masses by generating bounding boxes around detected regions.

### 4. Result Visualization
Using **OpenCV**, the detection results are displayed by overlaying bounding boxes on the original mammogram image.

---

## Technologies Used

- **Python** – Core programming language
- **YOLOv11 (Ultralytics)** – Object detection framework
- **PyTorch** – Deep learning framework used for training and inference
- **OpenCV** – Image processing and visualization
- **NumPy & Pandas** – Data processing and analysis
- **Matplotlib / Seaborn** – Data visualization
- **Jupyter Notebook / VS Code** – Development environment

---

## Key Highlights

- Built an **end-to-end deep learning pipeline for medical image detection**
- Implemented **YOLOv11 for accurate object detection in mammograms**
- Applied **computer vision techniques to healthcare imaging**
- Demonstrates the potential of **AI-assisted diagnostic systems**
