
from flask import Flask, request, jsonify
from consent_manager import ConsentManager
from anonymization import anonymize_data
from model import train_model, predict
from compliance_engine import ComplianceEngine

app = Flask(__name__)

consent_manager = ConsentManager()
compliance_engine = ComplianceEngine()

@app.route("/")
def home():
    return "DPDP Healthcare AI Running"

@app.route("/consent", methods=["POST"])
def consent():
    data = request.json
    consent_manager.add_consent(data)
    return jsonify({"status": "consent stored"})

@app.route("/train", methods=["POST"])
def train():
    result = train_model()
    return jsonify(result)

@app.route("/predict", methods=["POST"])
def run_prediction():
    data = request.json
    pred = predict(data)
    return jsonify({"prediction": float(pred)})

@app.route("/erase/<patient_id>", methods=["DELETE"])
def erase(patient_id):
    result = compliance_engine.erase_data(patient_id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
