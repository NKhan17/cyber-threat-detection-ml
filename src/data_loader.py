import os
import urllib.request
import pandas as pd

def load_nsl_kdd():
    os.makedirs('data', exist_ok=True)
    train_url = 'https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.csv'
    train_path = 'data/KDDTrain+.csv'
    
    if not os.path.exists(train_path):
        print("Downloading NSL-KDD dataset from public repository...")
        try:
            urllib.request.urlretrieve(train_url, train_path)
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            raise
            
    columns = ['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot',
                'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
                'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
                'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate',
                'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
                'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate',
                'dst_host_srv_rerror_rate','attack','level']
    
    df = pd.read_csv(train_path, header=None, names=columns)
    print(f"[Milestone 2] Dataset loaded successfully. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    df = load_nsl_kdd()
