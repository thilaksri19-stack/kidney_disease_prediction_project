 🩺 Chronic Kidney Disease Prediction System

 📌 Project Overview

This project builds a **Machine Learning web application** that predicts whether a patient has **Chronic Kidney Disease (CKD)** based on medical parameters.

The model is trained using the **Kidney Disease dataset** and deployed as an interactive web application using **Streamlit**. Users can enter patient medical values and instantly get a prediction.

---

 🎯 Objective

The goal of this project is to:

* Detect **Chronic Kidney Disease early**
* Use **machine learning algorithms** for medical prediction
* Build a **deployable web application**

---

 🧠 Machine Learning Models Used

The following algorithms were explored:

* Logistic Regression
* Random Forest Classifier
* Decision Tree Classifier

The final deployed model uses **Logistic Regression** for prediction.

---
 📊 Dataset Information

The dataset contains **medical attributes related to kidney health**.

 Features Used

* Age
* Blood Pressure (bp)
* Specific Gravity (sg)
* Albumin (al)
* Sugar (su)
* Red Blood Cells (rbc)
* Pus Cell (pc)
* Pus Cell Clumps (pcc)
* Bacteria (ba)
* Blood Glucose Random (bgr)
* Blood Urea (bu)
* Serum Creatinine (sc)
* Sodium (sod)
* Potassium (pot)
* Hemoglobin (hemo)
* Packed Cell Volume (pcv)
* White Blood Cell Count (wc)
* Red Blood Cell Count (rc)
* Hypertension (htn)
* Diabetes Mellitus (dm)
* Coronary Artery Disease (cad)
* Appetite (appet)
* Pedal Edema (pe)
* Anemia (ane)
 Target Variable

* **classification**

  * `1 → CKD`
  * `0 → Not CKD`

---

 ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

 📁 Project Structure

```
kidney_disease_prediction_project
│
├── app.py
├── kidney_disease.csv
├── ckd_model.pkl
├── requirements.txt
└── README.md
```

---

 🧹 Data Preprocessing

Several preprocessing steps were performed:

* Handling missing values
* Cleaning inconsistent values
* Converting categorical values to numerical
* Feature type conversion
* Label encoding
* Handling special characters in dataset

---

## 🧮 Model Training

The dataset was split into:

* **Training Data (75%)**
* **Testing Data (25%)**

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score

---

## 🚀 Web Application

The project is deployed using **Streamlit**.

Users can:

* Enter patient medical details
* Click the **Predict button**
* Instantly see the prediction result

---

## 💻 Installation

Clone the repository:

```
git clone https://github.com/yourusername/kidney-disease-prediction.git
```

Navigate to the project folder:

```
cd kidney-disease-prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 📈 Future Improvements

Possible improvements for the project:

* Use deep learning models
* Add more medical datasets
* Improve prediction accuracy
* Create a professional medical dashboard
* Add probability scores for predictions

---

## 👨‍💻 Author

Developed as a **Machine Learning project for healthcare prediction**.
