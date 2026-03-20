
import pandas as pd

class ComplianceEngine:
    def erase_data(self, patient_id):
        df = pd.read_csv("../data/sample_kidney_data.csv")
        df = df[df["patient_id"] != int(patient_id)]
        df.to_csv("../data/sample_kidney_data.csv", index=False)
        return {"status": "data erased, retraining required"}
