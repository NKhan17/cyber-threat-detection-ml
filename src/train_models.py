import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def train_and_evaluate(X_train, X_test, y_train, y_test, feature_names):
    os.makedirs('visualizations', exist_ok=True)
    results = {}
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=2000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    }

    trained_models = {}
    print("\nTraining models...")
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        results[name] = acc
        trained_models[name] = model
        print(f"{name} Accuracy: {acc:.4f}")
        
        # Save Confusion Matrix
        cm = confusion_matrix(y_test, preds)
        plt.figure(figsize=(6,4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Confusion Matrix: {name}')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.savefig(f'visualizations/cm_{name.replace(" ", "_").lower()}.png')
        plt.close()

    print("[Milestones 6, 7, 8] Model training and evaluation complete.")

    # Accuracy Comparison Plot
    plt.figure(figsize=(8,5))
    sns.barplot(x=list(results.keys()), y=list(results.values()))
    plt.ylim(0.8, 1.0)
    plt.title('Model Accuracy Comparison')
    plt.ylabel('Accuracy')
    plt.savefig('visualizations/model_comparison.png')
    plt.close()

    # Feature Importance Plot (Random Forest)
    print("Generating Feature Importance visualization...")
    rf = trained_models['Random Forest']
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1][:15] # Top 15 features
    
    plt.figure(figsize=(10,8))
    sns.barplot(x=importances[indices], y=feature_names[indices])
    plt.title('Top 15 Feature Importances (Random Forest)')
    plt.xlabel('Relative Importance')
    plt.tight_layout()
    plt.savefig('visualizations/feature_importance.png')
    plt.close()

    print("[Milestone 9] Final visualizations saved.")
    return trained_models

if __name__ == "__main__":
    from src.data_loader import load_nsl_kdd
    from src.preprocess import clean_and_preprocess, get_train_test_split
    
    df = load_nsl_kdd()
    df_clean = clean_and_preprocess(df)
    X_train, X_test, y_train, y_test, feature_names = get_train_test_split(df_clean)
    train_and_evaluate(X_train, X_test, y_train, y_test, feature_names)
