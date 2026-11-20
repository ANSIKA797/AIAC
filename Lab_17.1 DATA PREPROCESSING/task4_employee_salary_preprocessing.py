"""Task 4: Employee Salary Data Preprocessing for HR analytics."""
import pandas as pd


def preprocess_salaries(df: pd.DataFrame) -> pd.DataFrame:
    """Impute missing values, remove salary outliers, standardize text, and label-encode."""
    df = df.copy()
    df["salary"] = df["salary"].fillna(df["salary"].median())
    df["department"] = df["department"].fillna("general").str.strip().str.lower()
    df["job_location"] = df["job_location"].fillna("remote").str.strip().str.lower()

    q1, q3 = df["salary"].quantile(0.25), df["salary"].quantile(0.75)
    iqr = q3 - q1
    df = df[(df["salary"] >= q1 - 1.5 * iqr) & (df["salary"] <= q3 + 1.5 * iqr)].copy()

    df["dept_code"] = df["department"].astype("category").cat.codes
    df["location_code"] = df["job_location"].astype("category").cat.codes
    return df


if __name__ == "__main__":
    raw = pd.DataFrame({
        "emp": ["Asha", "Ravi", "Neha", "Kiran", "CEO_Outlier"],
        "department": [" Engineering", "HR", None, "ENGINEERING", "Executive"],
        "job_location": ["Hyderabad", "Bengaluru", "Hyderabad", None, "Mumbai"],
        "salary": [65000, 52000, None, 70000, 950000],
    })
    hr = preprocess_salaries(raw)
    print(hr[["emp", "department", "dept_code", "location_code", "salary"]].to_string(index=False))
