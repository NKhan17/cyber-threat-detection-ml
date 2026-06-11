import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def clean_and_preprocess(df):
    print("Cleaning and preprocessing data...")
    # Binary classification: normal (0) vs anomaly/attack (1)
    df['label'] = df['attack'].apply(lambda v: 0 if v == 'normal' else 1)
    df = df.drop(['attack', 'level'], axis=1, errors='ignore')
    
    # Drop constant columns with zero variance
    df = df.loc[:, df.apply(pd.Series.nunique) != 1]
    
    # One-hot encoding for categorical variables
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    print(f"[Milestone 3] Data cleaned. New shape: {df.shape}")
    return df

def get_train_test_split(df):
    X = df.drop('label', axis=1)
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("[Milestone 5] Feature engineering & Train-Test Split complete.")
    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns

if __name__ == "__main__":
    from src.data_loader import load_nsl_kdd
    df = load_nsl_kdd()
    df_clean = clean_and_preprocess(df)
    get_train_test_split(df_clean)
