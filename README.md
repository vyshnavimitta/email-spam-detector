# 📧 Email Spam Detector (Spam vs. Ham)

## 📌 Project Description
A machine learning project that detects whether an email is **Spam** or **Ham (Not Spam)**.  
It uses a **Naive Bayes classifier with CountVectorizer** trained on a dataset of 5,572 emails, achieving ~98% accuracy.  
The project is deployed as a **Streamlit web application** for easy user interaction.

---

## 📌 Features
- User-friendly **Streamlit web app** interface.  
- Classifies emails as **Spam** or **Ham** in real-time.  
- Trained on the classic **spam.csv dataset**.  
- Achieves high accuracy (~98%).  
- Lightweight and easy to set up locally.  

---

## 📌 Requirements
- Python 3.8 or above  
- VS Code / Any IDE  
- Virtual environment (venv or conda)  
- Libraries:  
  - `pandas`  
  - `scikit-learn`  
  - `joblib`  
  - `streamlit`  

---

## 📌 Installation & Setup (Step-by-Step)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/spam-detector.git
cd spam-detector 
```
### 2. Create a virtual environment
 ```bash 
python -m venv venv
```
### 3. Activate the environment
```bash  
    venv\Scripts\activate
```
 ###  4. Install dependencies
 ```bash
 pip install -r requirements.txt
```
 ###  5. Install dependencies
 ```bash
 python train.py
```
 ###  6. Install dependencies
 ```bash
 streamlit run app.py

```


