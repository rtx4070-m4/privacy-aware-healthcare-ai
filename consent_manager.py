
import json
import os

class ConsentManager:
    def __init__(self):
        self.file = "consent_logs.json"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def add_consent(self, data):
        with open(self.file, "r") as f:
            logs = json.load(f)
        logs.append(data)
        with open(self.file, "w") as f:
            json.dump(logs, f, indent=4)
