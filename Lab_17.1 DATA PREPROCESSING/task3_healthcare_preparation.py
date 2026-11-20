"""Task 3: Healthcare Data Preparation for ML models."""
import numpy as np
import pandas as pd


def prepare_healthcare(df: pd.DataFrame, test_ratio: float = 0.2):
    """Impute missing vitals, encode categories, scale numerics, and split train/test."""
    df = df.copy()
    df["blood_pressure"] = df["blood_pressure"].fillna(df["blood_pressure"].median())
    df["cholesterol"] = df["cholesterol"].fillna(df["cholesterol"].median())
    df["smoker_enc"] = df["smoker"].str.lower().map({"no": 0, "yes": 1}).fillna(0).astype(int)

    for col in ("blood_pressure", "cholesterol"):
        mn, mx = df[col].min(), df[col].max()
        df[col + "_scaled"] = ((df[col] - mn) / (mx - mn)).round(4) if mx > mn else 0.0

    rng = np.random.default_rng(42)
    idx = rng.permutation(len(df))
    split = int(len(df) * (1 - test_ratio))
    return df.iloc[idx[:split]], df.iloc[idx[split:]]


if __name__ == "__main__":
    raw = pd.DataFrame({
        "blood_pressure": [120, None, 140, 130, 125],
        "cholesterol": [190, 210, None, 230, 200],
        "smoker": ["No", "Yes", "No", "Yes", "No"],
        "risk": [0, 1, 1, 1, 0],
    })
    train_df, test_df = prepare_healthcare(raw)
    print(f"Train rows: {len(train_df)}, Test rows: {len(test_df)}")
    print(train_df[["blood_pressure_scaled", "cholesterol_scaled", "smoker_enc", "risk"]].to_string(index=False))
