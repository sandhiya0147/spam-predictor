# spam-predictor

This project is a web-based SMS Spam Classifier built using the Naive Bayes algorithm and Flask. It classifies incoming SMS text messages as either Spam or Ham (not spam). The model is trained on the well-known SMS Spam Collection Dataset, which contains real-world SMS messages labeled for spam detection.

---

## Features

- Accepts free-text SMS input from users through a simple web form.
- Uses TF-IDF vectorization to convert text into numerical features.
- Classifies messages using a Multinomial Naive Bayes model.
- Displays real-time prediction: Spam or Ham.
- Clean and responsive Flask web interface, ready for Render deployment.


---

## Prerequisites

Make sure the following are installed:

- Python 3.7 or higher installed
- Git installed and configured
- Basic knowledge of Python and Flask
- A GitHub account (for code hosting)
- Render account (for deployment)

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/sandhiya0147/spam-predictor.git
cd spam-predictor
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask development server:

```
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## How It Works

- The user enters a text message into the web form and submits it.
- The app loads a pre-trained Naive Bayes model and TF-IDF vectorizer.
- The input message is converted into a numerical vector using the vectorizer.
- The model predicts whether the message is Spam or Ham.
- The prediction result is displayed instantly on the webpage.
  
---

## File Structure

```
sms-spam-classifier/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── sms_spam.csv
├── model_train.py
├── model.pkl
├── vectorizer.pkl
├── target_names.pkl
├── app.py
├── requirements.txt
├── Procfile
└── README.md           
```

---

## Future Improvements

- Display prediction confidence – show the probability score for "Spam" or "Ham."
- Support bulk classification – allow uploading a CSV of multiple messages for batch predictions.
- Improve preprocessing – add lemmatization, stop word removal, and emoji handling.
- Switchable models – enable users to choose between Naive Bayes, SVM, or deep learning.
- Log user inputs (optional) – store messages and predictions for model retraining or analytics.

---



## Step-by-Step Guide: How to Use the Movie Interest Predictor


### Step 1: Input Form
![Form](assets/input_form.png)  

### Step 2: Filled Form 
![Prediction Result](assets/filled_input.png)  

### Step 3: Prediction Result
![Full Page](assets/predicted_result.png)

---

## Live Demo

[Click here to view the deployed app](https://spam-predictor-dmr7.onrender.com)

---

