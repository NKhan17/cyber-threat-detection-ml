# Cyber Threat Detection Project Report

## 1. Executive Summary
This report details the development of a Machine Learning-based Intrusion Detection System (IDS) using the NSL-KDD dataset. The primary objective was to classify network traffic into normal or malicious categories. Three models were evaluated: Logistic Regression, Decision Tree, and Random Forest. The Random Forest model demonstrated superior performance, making it the most suitable candidate for deployment.

## 2. Dataset and Preprocessing
The NSL-KDD dataset was selected to resolve the inherent issues of the original KDD Cup '99 dataset, such as redundant records that bias classifiers. 

**Preprocessing Steps:**
- **Label Transformation:** The multi-class attack labels were aggregated into a binary classification target (`0` for normal, `1` for anomaly).
- **Categorical Encoding:** One-hot encoding was applied to textual features such as `protocol_type`, `service`, and `flag`.
- **Feature Selection:** Columns with zero variance were removed to reduce dimensionality.
- **Scaling:** Numerical features were standardized using `StandardScaler` to ensure algorithms like Logistic Regression converged properly and weren't biased by large magnitudes.

## 3. Exploratory Data Analysis (EDA)
EDA revealed a relatively balanced distribution between normal traffic and anomalous traffic in the training set. Protocol type analysis indicated that ICMP and TCP protocols were frequently associated with specific types of attacks (e.g., DoS or Probe).

## 4. Modeling Approach
The dataset was split into an 80% training set and a 20% testing set using stratified sampling to maintain class proportions. 
- **Logistic Regression:** Used as a linear baseline.
- **Decision Tree:** Captured non-linear relationships without scaling dependencies.
- **Random Forest:** An ensemble method that reduced the variance of the decision tree, leading to better generalization.

## 5. Evaluation and Results
The models were evaluated primarily on Accuracy and Confusion Matrices.
- **Logistic Regression** provided a solid baseline but struggled with highly non-linear feature interactions.
- **Decision Tree** performed exceptionally well but showed signs of slight overfitting on training data.
- **Random Forest** achieved the highest overall accuracy and lowest false positive rate, which is critical for an IDS to avoid alert fatigue.

## 6. Feature Importance
Analysis of the Random Forest feature importances highlighted that specific traffic features (e.g., `src_bytes`, `dst_bytes`, and connection `count`) were highly predictive of anomalies, confirming domain knowledge that volumetric changes often indicate intrusion attempts.

## 7. Conclusion
The project successfully implemented a robust anomaly detection pipeline. The Random Forest classifier is recommended for production use due to its high accuracy and interpretability.
