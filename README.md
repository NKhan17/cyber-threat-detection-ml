# Cyber Threat Detection using Machine Learning

## 📌 Project Overview
This project implements an end-to-end Machine Learning pipeline to detect network intrusions and cyber threats. By leveraging the NSL-KDD dataset, the system classifies network traffic into "normal" and "anomalous" (attack) categories, demonstrating the application of data science to cybersecurity.

## 🎯 Problem Statement
With the increasing volume and complexity of cyber attacks, traditional signature-based intrusion detection systems (IDS) often struggle to identify novel threats. This project aims to build an anomaly-based IDS using machine learning algorithms to effectively distinguish between benign network traffic and malicious activities.

## 📊 Dataset Description
The project utilizes the **NSL-KDD dataset**, an improved and widely recognized benchmark dataset for network intrusion detection. 
- **Features:** 41 features encompassing intrinsic, content, and traffic-based characteristics.
- **Classes:** Binary classification (Normal vs. Anomaly).

## 🛠️ Technologies Used
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Algorithms:** Logistic Regression, Decision Tree Classifier, Random Forest Classifier

## 🚀 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/NKhan17/cyber-threat-detection-ml.git
   cd cyber-threat-detection-ml
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the ML pipeline:
   ```bash
   python main.py
   ```

## 📁 Project Structure
```
cyber-threat-detection-ml/
├── data/                   # Dataset directory (auto-downloaded)
├── docs/                   # Documentation, reports, and QA
├── src/                    # Source code for the ML pipeline
│   ├── data_loader.py      # Dataset acquisition
│   ├── preprocess.py       # Data cleaning and feature engineering
│   ├── eda.py              # Exploratory data analysis
│   └── train_models.py     # Model training and evaluation
├── visualizations/         # Generated plots and confusion matrices
├── main.py                 # Pipeline execution script
└── requirements.txt        # Project dependencies
```

## 🔬 Methodology
1. **Data Acquisition:** Automated downloading of the NSL-KDD dataset.
2. **Preprocessing:** Handling categorical variables via one-hot encoding, removing zero-variance features, and feature scaling using StandardScaler.
3. **Exploratory Data Analysis (EDA):** Visualizing class distributions to understand class imbalances.
4. **Model Training:** Training baseline and ensemble models with hyperparameter initialization.
5. **Evaluation:** Comparing models based on Accuracy and Confusion Matrices.

## 📈 Results & Model Training
Three machine learning models were trained and compared:
- **Logistic Regression**
- **Decision Tree**
- **Random Forest**

The **Random Forest Classifier** achieved the highest accuracy, demonstrating robustness against overfitting and effectively capturing complex non-linear relationships in the network traffic data.

## 🔮 Future Improvements
- Implement hyperparameter tuning using GridSearchCV.
- Explore deep learning models (e.g., LSTMs or Autoencoders) for sequence anomaly detection.
- Deploy the model as a real-time REST API using FastAPI or Flask.

---
**Author:** Neha Khan
