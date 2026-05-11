import pandas as pd
import sklearn
import mlflow
import whylogs
import requests
import os

print("--- KIỂM TRA MÔI TRƯỜNG ---")
try:
    print(f"✅ Pandas version: {pd.__version__}")
    print(f"✅ Scikit-learn version: {sklearn.__version__}")
    print(f"✅ MLflow version: {mlflow.__version__}")
    print(f"✅ Whylogs version: {whylogs.__version__}")
    
    # Kiểm tra file dữ liệu
    data_path = "2687_capstone_project_dataset_v1_vv6_ahjq7xz.csv"
    if os.path.exists(data_path):
        print(f"✅ Tìm thấy file dữ liệu tại: {data_path}")
    else:
        print(f"❌ Không tìm thấy file dữ liệu tại: {data_path}")

    print("\n🚀 Chúc mừng! Mọi thứ đã sẵn sàng cho dự án Capstone.")
except ImportError as e:
    print(f"❌ Thiếu thư viện: {e}")
    print("👉 Hãy thử chạy lại: pip install -r requirements.txt")