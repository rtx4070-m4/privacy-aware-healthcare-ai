
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import joblib

MODEL_PATH = "model.pkl"

def train_model():
    df = pd.read_csv("../data/sample_kidney_data.csv")
    X = df.drop(columns=["target"])
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    model = Ridge()
    model.fit(X_pca, y)

    joblib.dump((model, scaler, pca), MODEL_PATH)
    return {"status": "model trained"}

def predict(data):
    model, scaler, pca = joblib.load(MODEL_PATH)
    df = pd.DataFrame([data])
    X_scaled = scaler.transform(df)
    X_pca = pca.transform(X_scaled)
    return model.predict(X_pca)[0]
