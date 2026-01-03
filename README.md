# Finger Sign Detection Deep Learning Web Application

## Overview

This project delivers an **end-to-end Finger Sign Detection system** that leverages **Convolutional Neural Networks (CNNs)** for classifying hand gestures representing digits **0–6**. 

The system is integrated into a **Flask-based web application**, allowing users to upload images of hand signs and instantly receive predictions with confidence scores.

The project follows **industry-standard practices**, including modular code structure, clean separation of concerns, and deployment-ready design.


## Key Skills and Technologies

* **Deep Learning / CNNs:** Image classification, convolutional neural networks, model training & evaluation
* **Computer Vision:** Image preprocessing, augmentation, classification
* **Web Development:** Flask, HTML/CSS
* **Data Handling & Analysis:** NumPy, Pandas, visualization
* **Deployment Readiness:** Modular structure, model serialization, upload handling

This highlights transferable skills for **AI/ML, Computer Vision, and full-stack roles**.


## Dataset Information

* **Dataset Name:** Hand Finger Sign Dataset
* **Source:** Custom / Kaggle-like sources
* **Classes:** 0, 1, 2, 3, 4, 5, 6
* **Structure:** Class-wise folders containing labeled hand sign images


## Model Architecture

* **Architecture:** Custom Convolutional Neural Network (CNN)
* **Input Size:** 64 × 64 × 3
* **Loss Function:** Categorical Crossentropy
* **Optimizer:** Adam (Learning Rate: 1e-4)
* **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score

The model is trained to generalize across varying hand positions, lighting conditions, and backgrounds.


## Project Structure

```
finger-sign-detection/
│
├── app.py                     # Main Flask 
├── requirements.txt           # Python dependencies
├── notebook/                  # Jupyter notebook 
│   └── finger_sign_classification.ipynb
│
├── model/
│   └── signs_cnn_model.keras  # Trained CNN model
│   └── predictor.py
│
├── utils/
│   ├── preprocess.py       # Image preprocessing
│
├── static/
│   ├── css/
│   │   └── style.css           # Custom styling
│   └── uploads/                # Uploaded images
│
├── templates/
│   └── index.html              # Main UI template
└── README.md
```


## Application Workflow

1. User uploads an image of a finger sign via the web interface.
2. File is validated and saved in `static/uploads/`.
3. Image is preprocessed for CNN input.
4. Model predicts the corresponding finger digit and confidence.
5. Result is displayed on the web UI.


## UI Preview

![finger-sign-5](https://github.com/user-attachments/assets/399658f2-3105-4932-82c6-08a390feadcd)


![finger-sign-0](https://github.com/user-attachments/assets/30964329-9546-4233-a6ce-5d85b75bfa5b)

![finger-sign-4](https://github.com/user-attachments/assets/e92f03dd-a109-4b48-b205-f770a25499f0)


## Utility Modules

* **`preprocess.py`**: Handles image resizing, normalization, and preparation for CNN input

This modular approach ensures **clean, maintainable, and scalable code**.


## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/batoolarifa/finger-sign-detection
cd finger-sign-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

## Model Inference Workflow

* Upload an image of a hand showing a finger digit (0–6).
* The model predicts the corresponding digit along with a **confidence score**.

## Deployment

* Fully deployable on **Hugging Face Spaces, Render, AWS EC2, or Docker environments**
* Model is loaded once at startup for **efficient inference**
* Supports easy addition of **new classes** or **real-time extensions**


## Industry Relevance & Value

This project demonstrates:

* **End-to-end ML application development**
* **CNN-based computer vision expertise**
* **Full-stack AI system implementation**
* **Reproducible, scalable, and modular code practices**

> Highlights alignment with **AI/ML, Computer Vision, and Software Engineering career paths**.


## Future Improvements

* Real-time webcam inference for finger signs
* Integration with **gesture-controlled applications**
* REST API using FastAPI for mobile/web integration
* Enhanced UI with **dark mode and responsive design**


## 👤 Author

**Syeda Arifa Batool**
SE @ Karachi University | AI & ML Enthusiast | Transforming ideas into real-world AI solutions 📈



## 🔗 Connect with Me

* **LinkedIn:** [https://www.linkedin.com/in/arifa-batool/](https://www.linkedin.com/in/arifa-batool/)
* **Kaggle:** [https://www.kaggle.com/arifa-batool](https://www.kaggle.com/arifa-batool)
* **Email:** [thearifabatool@gmail.com](mailto:thearifabatool@gmail.com)

⭐ If you find this project useful, feel free to star the repository!

