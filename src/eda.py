import os
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    print("Performing Exploratory Data Analysis...")
    os.makedirs('visualizations', exist_ok=True)
    
    # Target distribution
    plt.figure(figsize=(8,5))
    sns.countplot(x='label', data=df)
    plt.title('Distribution of Normal vs Anomaly (Threat)')
    plt.savefig('visualizations/target_distribution.png')
    plt.close()
    
    print("[Milestone 4] EDA complete. Plots saved to 'visualizations/' folder.")

if __name__ == "__main__":
    from src.data_loader import load_nsl_kdd
    from src.preprocess import clean_and_preprocess
    df = load_nsl_kdd()
    df_clean = clean_and_preprocess(df)
    perform_eda(df_clean)
