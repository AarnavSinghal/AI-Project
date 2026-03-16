import pandas as pd

def parse_csv(file) -> tuple:
    df = pd.read_csv(file)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()
    summary = {
        "rows": len(df),
        "cols": len(df.columns),
        "columns": df.columns.tolist(),
        "numeric_columns": numeric_cols,
        "categorical_columns": categorical_cols,
        "null_counts": df.isnull().sum().to_dict(),
        "sample_rows": df.head(3).to_dict(orient="records"),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }
    if numeric_cols:
        summary["stats"] = df[numeric_cols].describe().to_dict()
    return df, summary