# 🏦 BankMind — Bank Marketing Intelligence Dashboard

> VIT BAIH Community Project 2026 Screening | Track 1 (Data Analyst) + Track 2 (ML Engineer)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bankmind-manya.streamlit.app/)

---

## 📌 Project Overview

BankMind is an end-to-end data analytics and machine learning project built on the **UCI Bank Marketing Dataset** (45,211 records). The goal is to understand what drives customers to subscribe to a term deposit — and ultimately predict whether a new customer will subscribe based on their profile.

**Dataset:** [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)  
**Target Variable:** `y` — Has the client subscribed to a term deposit? (yes/no)  
**Class Imbalance:** Only 11.7% of customers subscribed — making this a real-world imbalanced classification problem.

---

## 🚀 Live Demo

👉 **[bankmind-manya.streamlit.app](https://bankmind-manya.streamlit.app/)**

---

## 🗂️ Project Structure

```
bankmind-Manya-Jajodia/
├── data/bank/
│   ├── bank-full.csv         # Full dataset (45,211 records)
│   └── bank-names.txt        # Feature descriptions
├── app.py                    # Streamlit dashboard
├── eda.ipynb                 # Exploratory Data Analysis notebook
├── model.ipynb               # ML modeling notebook
├── requirements.txt          # Python dependencies
├── EXPLANATION.md
└── README.md
```

---

## 📊 Track 1 — Data Analyst (EDA Dashboard)

An interactive multi-page Streamlit dashboard with 4 key business analyses:

| Analysis | Key Finding |
|---|---|
| **Job vs Subscription Rate** | Retired and student segments show the highest subscription rates |
| **Balance vs Subscription** | Subscribers tend to have higher account balances |
| **Age vs Subscription** | Customers aged 60+ subscribe at the highest rate |
| **Housing Loan vs Subscription** | Customers without housing loans are more likely to subscribe |

### Dashboard Features
- 🔘 Multi-page navigation with session state
- 🎛️ Interactive filters — multiselect, sliders, radio buttons
- 📈 Metric cards (Total Customers, Subscribed, Subscription Rate) that update live with filters
- 📋 Raw data toggle to inspect underlying numbers
- 🎨 Color-highlighted bars based on user selection

---

## 🤖 Track 2 — ML Engineer 

Predictive modeling to classify whether a customer will subscribe:

- Logistic Regression (baseline)
- Random Forest Classifier
- Evaluation: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Feature importance analysis
- Live customer prediction via Streamlit interface

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/manya296/bankmind-Manya-Jajodia.git
cd bankmind-Manya-Jajodia
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit dashboard
```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

### 5. Run the EDA notebook
Open `eda.ipynb` in VS Code or Jupyter and run all cells.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Core language |
| Pandas | Data manipulation |
| Seaborn / Matplotlib | Visualizations |
| Scikit-learn | ML modeling |
| Streamlit | Interactive dashboard |
| Joblib | Model serialization |

---

## 👩‍💻 Author

**Manya Jajodia**  
VIT | BAIH Community Project 2026 Screening  
GitHub: [@manya296](https://github.com/manya296)
