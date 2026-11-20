"""Task 1: Customer Data Cleaning using Pandas."""
import pandas as pd


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values, duplicates, text standardization, and encoding."""
    df = df.drop_duplicates().copy()
    df["age"] = df["age"].fillna(df["age"].median())
    df["income"] = df["income"].fillna(df["income"].mean())
    df["city"] = df["city"].fillna("unknown").astype(str).str.strip().str.lower()
    df["gender_encoded"] = df["gender"].str.lower().map({"male": 0, "female": 1}).fillna(-1).astype(int)
    df["city_encoded"] = df["city"].astype("category").cat.codes
    return df


if __name__ == "__main__":
    raw = pd.DataFrame([
        {"id": 1, "age": 24, "income": 45000.0, "city": " Hyderabad ", "gender": "Female"},
        {"id": 2, "age": None, "income": 60000.0, "city": "BENGALURU", "gender": "Male"},
        {"id": 2, "age": None, "income": 60000.0, "city": "BENGALURU", "gender": "Male"},
        {"id": 3, "age": 31, "income": None, "city": None, "gender": "Female"},
    ])
    cleaned = clean_customer_data(raw)
    print("Cleaned shape:", cleaned.shape)
    print(cleaned[["id", "age", "income", "city", "gender_encoded", "city_encoded"]].to_string(index=False))
