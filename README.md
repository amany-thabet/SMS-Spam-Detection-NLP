# SMS-Spam-Detection-NLP
NLP-based SMS Spam Detection system using TF-IDF and Machine Learning models such as Random Forest, SVM, logistic regression,KNN and Naive Bayes.
# 📩 SMS Spam Detection using NLP & Machine Learning

This project is a Natural Language Processing (NLP) based SMS Spam Detection system that classifies text messages as **Spam** or **Ham** using different Machine Learning algorithms.

---

## 🚀 Project Overview

The main goal of this project is to preprocess SMS text messages, extract meaningful features using **TF-IDF Vectorization**, and train multiple machine learning models to accurately detect spam messages.

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, which contains labeled SMS messages categorized into:
- **Ham** → Normal messages
- **Spam** → Unwanted or advertising messages

---

## 🛠️ Technologies & Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- WordCloud

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading & Cleaning
- Removed unnecessary columns
- Renamed dataset columns
- Checked dataset structure

### 2️⃣ Exploratory Data Analysis (EDA)
- Visualized Spam vs Ham distribution
- Analyzed message lengths
- Compared spam and ham message characteristics

### 3️⃣ Text Preprocessing
- Converted text to lowercase
- Removed punctuation
- Removed stopwords
- Tokenized text messages

### 4️⃣ Feature Extraction
Used:
- **CountVectorizer (Bag of Words)**
- **TF-IDF Vectorizer**
- **N-grams**

### 5️⃣ Machine Learning Models
Implemented and compared:
- Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- K-Nearest Neighbors (KNN)

### 6️⃣ Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🌟 Best Performing Models

The best performance was achieved using:
- **SVM**
- **Random Forest**

with high accuracy in spam classification.

---

## 📈 Key Insights

- Spam messages are generally longer than ham messages.
- TF-IDF improved text representation by assigning higher importance to informative words.
- Ensemble methods like Random Forest helped reduce overfitting and improve prediction stability.

---

## 📌 Example Prediction

| Message | Prediction |
|---|---|
| "Win free money now!" | Spam |
| "Call me when you arrive" | Ham |

---

## 📷 Visualizations Included

- Pie Chart for Spam vs Ham distribution
- Histogram of message lengths
- WordClouds for spam and ham messages
- Confusion Matrix

---

## 🧠 NLP Concepts Used

- Tokenization
- Stopword Removal
- Feature Extraction
- TF-IDF
- N-grams

---

## ▶️ How to Run

1. Clone the repository
2. Install required libraries

```bash
pip install -r requirements.txt
```

3. Run the notebook

---

## 👩‍💻 Author

Amany Thabet  
Faculty of Computers and Information  
Interested in Artificial Intelligence & Machine Learning
