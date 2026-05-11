import pandas as pd
import whylogs as why
from whylogs.viz import NotebookProfileVisualizer
import datetime
import os

# ================================
# 1. Simulate Production Data
# ================================
data = {
    "YearsExperience": [1.0, 5.5, 10.0, 15.0, 20.0, 3.0, 8.0]
}
df_production = pd.DataFrame(data)

# ================================
# 2. Create Profile with whylogs
# ================================
print(f"[*] Initializing local logging at: {datetime.datetime.now()}")

results = why.log(df_production)
profile_view = results.view()

# ================================
# 3. Generate HTML Report
# ================================
def save_whylogs_report(profile_view, output_file):
    viz = NotebookProfileVisualizer()
    viz.set_profiles(target_profile_view=profile_view)

    html_content = viz.to_html()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    return os.path.abspath(output_file)

# ================================
# 4. Run Export
# ================================
output_file = "model_monitoring_report.html"

try:
    saved_path = save_whylogs_report(profile_view, output_file)
    print(f"[✓] Success! Monitoring report saved to: {saved_path}")
except Exception as e:
    print("[✗] Failed to generate report")
    print(f"Error: {e}")