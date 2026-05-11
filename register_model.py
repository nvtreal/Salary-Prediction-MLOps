import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://localhost:5000")
client = MlflowClient()

# Liệt kê tất cả các model đã đăng ký
models = client.search_registered_models()
for m in models:
    print(f"Tên Model: {m.name}")
    for version in m.latest_versions:
        print(f"  -- Version: {version.version}, Stage: {version.current_stage}")