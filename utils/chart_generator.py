import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def generate_chart(df: pd.DataFrame, question: str, analysis: dict):
    """Auto-generate the most relevant Plotly chart based on the question."""

    q = question.lower()
    result = analysis.get("result")

    if analysis.get("error") or result is None:
        return None

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()

    try:
        # Trend / time series
        if any(word in q for word in ["trend", "over time", "monthly", "weekly", "daily", "time"]):
            date_cols = [c for c in df.columns if "date" in c.lower() or "time" in c.lower()]
            if date_cols and numeric_cols:
                df[date_cols[0]] = pd.to_datetime(df[date_cols[0]], errors="coerce")
                fig = px.line(df.sort_values(date_cols[0]), x=date_cols[0], y=numeric_cols[0],
                              title=f"{numeric_cols[0]} over time")
                return fig

        # Top N / ranking
        if any(word in q for word in ["top", "best", "highest", "most", "ranking"]):
            if categorical_cols and numeric_cols:
                grouped = df.groupby(categorical_cols[0])[numeric_cols[0]].sum().nlargest(10).reset_index()
                fig = px.bar(grouped, x=categorical_cols[0], y=numeric_cols[0],
                             title=f"Top {categorical_cols[0]} by {numeric_cols[0]}")
                return fig

        # Distribution
        if any(word in q for word in ["distribution", "spread", "histogram", "range"]):
            if numeric_cols:
                fig = px.histogram(df, x=numeric_cols[0], title=f"Distribution of {numeric_cols[0]}")
                return fig

        # Correlation
        if any(word in q for word in ["correlation", "relationship", "vs", "compare"]):
            if len(numeric_cols) >= 2:
                fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1],
                                 title=f"{numeric_cols[0]} vs {numeric_cols[1]}")
                return fig

        # Outliers
        if any(word in q for word in ["outlier", "anomal", "unusual"]):
            if numeric_cols:
                fig = px.box(df, y=numeric_cols[0], title=f"Outliers in {numeric_cols[0]}")
                return fig

        # Default: bar chart of first categorical vs numeric
        if categorical_cols and numeric_cols:
            grouped = df.groupby(categorical_cols[0])[numeric_cols[0]].sum().reset_index()
            fig = px.bar(grouped, x=categorical_cols[0], y=numeric_cols[0],
                         title=f"{numeric_cols[0]} by {categorical_cols[0]}")
            return fig

    except Exception:
        return None

    return None