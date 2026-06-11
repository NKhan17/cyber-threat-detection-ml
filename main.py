import src.data_loader as dl
import src.preprocess as pp
import src.eda as eda
import src.train_models as tm

def run_pipeline():
    print("Starting Machine Learning Pipeline for Cyber Threat Detection\n" + "="*60)
    
    # Milestone 2
    df = dl.load_nsl_kdd()
    
    # Milestone 3
    df_clean = pp.clean_and_preprocess(df)
    
    # Milestone 4
    eda.perform_eda(df_clean)
    
    # Milestone 5
    X_train, X_test, y_train, y_test, feature_names = pp.get_train_test_split(df_clean)
    
    # Milestones 6, 7, 8, 9
    tm.train_and_evaluate(X_train, X_test, y_train, y_test, feature_names)
    
    print("\nPipeline executed successfully. All models trained and visualizations saved to 'visualizations/' directory.")

if __name__ == "__main__":
    run_pipeline()
