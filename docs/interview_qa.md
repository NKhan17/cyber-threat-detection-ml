# Interview Questions & Answers

**Q1: Why did you choose the NSL-KDD dataset over the original KDD Cup '99 dataset?**
**A:** The original KDD Cup '99 dataset has a huge number of redundant records in both the training and testing sets. This causes learning algorithms to be biased towards more frequent records and prevents them from learning infrequent but potentially dangerous attacks. The NSL-KDD dataset resolves these issues by removing redundant records, making the evaluation more accurate and realistic.

**Q2: How did you handle categorical features like 'protocol_type'?**
**A:** I used One-Hot Encoding (`pd.get_dummies` in Pandas). Machine learning models require numerical input. Because protocol types (like TCP, UDP, ICMP) do not have an inherent ordinal relationship (one is not "greater" than another), one-hot encoding is the appropriate technique to convert them into binary vectors without introducing false mathematical relationships.

**Q3: Why was feature scaling necessary, and which scaler did you use?**
**A:** I used `StandardScaler` to standardize features by removing the mean and scaling to unit variance. Scaling is crucial for algorithms that compute distances or use gradient descent, like Logistic Regression. Without scaling, features with large numeric ranges (like `src_bytes` which can be in the tens of thousands) would disproportionately dominate the objective function compared to features that range from 0 to 1. 

**Q4: Can you explain why Random Forest outperformed the Decision Tree?**
**A:** A single Decision Tree is highly prone to overfitting; it tends to memorize the training data, capturing noise along with the underlying patterns. Random Forest is an ensemble method that builds multiple decision trees on random subsets of the data and features, and then averages their predictions. This bagging technique significantly reduces variance and prevents overfitting, leading to better generalization on unseen test data.

**Q5: In the context of Intrusion Detection, which is worse: False Positives or False Negatives?**
**A:** In cybersecurity, a False Negative (failing to detect an actual attack) is generally considered much worse because it means the network is breached and compromised without the administrators knowing. However, an excessively high False Positive rate (flagging normal traffic as an attack) causes "alert fatigue," leading analysts to ignore warnings. A good IDS must minimize False Negatives while keeping False Positives at an acceptable, manageable level.
