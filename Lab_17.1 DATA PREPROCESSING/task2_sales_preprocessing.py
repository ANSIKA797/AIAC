"""Task 2: Sales Data Preprocessing with datetime features and IQR outlier clipping."""
import pandas as pd


def preprocess_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Parse dates, extract time features, clip IQR outliers, and normalize sales."""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day_of_week"] = df["date"].dt.day_name()

    q1, q3 = df["sales_amount"].quantile(0.25), df["sales_amount"].quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["sales_clipped"] = df["sales_amount"].clip(lower=lower, upper=upper)

    mn, mx = df["sales_clipped"].min(), df["sales_clipped"].max()
    df["sales_norm"] = ((df["sales_clipped"] - mn) / (mx - mn)).round(4) if mx > mn else 0.0
    return df


if __name__ == "__main__":
    raw = pd.DataFrame({
        "date": ["2026-11-01", "2026-11-02", "2026-11-03", "2026-11-04", "2026-11-05"],
        "sales_amount": [1200, 1500, 1350, 1400, 9500],
    })
    out = preprocess_sales(raw)
    print(out[["date", "month", "day_of_week", "sales_clipped", "sales_norm"]].to_string(index=False))
