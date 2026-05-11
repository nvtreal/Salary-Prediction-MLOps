from flask import Flask, render_template, jsonify
import random
import datetime
import numpy as np

app = Flask(__name__)

history = []

# =============================
# Generate fake streaming data
# =============================
def generate_data():
    baseline = 3.0
    production = round(random.uniform(2, 20), 2)
    change = abs(production - baseline) / baseline
    drift = change > 0.3

    return {
        "feature": "YearsExperience",
        "baseline": baseline,
        "production": production,
        "change": round(change, 2),
        "drift": drift,
        "time": datetime.datetime.now().strftime("%H:%M:%S")
    }

# =============================
# Anomaly detection (Z-score)
# =============================
def detect_anomaly(history, new_value):
    values = [d["production"] for d in history] + [new_value]

    if len(values) < 5:
        return False

    mean = np.mean(values)
    std = np.std(values)

    if std == 0:
        return False

    z_score = abs((new_value - mean) / std)
    return bool(z_score > 2.5)

# =============================
# Routes
# =============================
@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/data")
def data():
    global history

    new_data = generate_data()
    new_data["anomaly"] = bool(detect_anomaly(history, new_data["production"]))
    new_data["drift"] = bool(new_data["drift"])  # đảm bảo luôn là Python bool

    history.append(new_data)
    history = history[-20:]

    return jsonify(history)

# =============================
#local then use
#if __name__ == "__main__":
    #app.run(debug=True, port=5002)
#cloud then use
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)