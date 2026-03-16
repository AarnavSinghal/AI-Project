import os
import json
import pandas as pd
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_analysis(df: pd.DataFrame, summary: dict, question: str) -> dict:
    system_prompt = """You are an expert data analyst. Given a pandas DataFrame and a question,
write Python code to answer it. Always assign the final result to a variable called `result`.
Return ONLY a JSON object with two keys:
- "code": the Python code string
- "explanation": one sentence describing what the code does
No markdown, no backticks, just raw JSON."""

    user_prompt = f"""
DataFrame summary:
{json.dumps(summary, default=str, indent=2)}

Question: {question}

Write pandas code to answer this. The dataframe variable is called `df`.
"""

    message = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
    )

    raw = message.choices[0].message.content.strip()

    try:
        parsed = json.loads(raw)
        code = parsed.get("code", "")
        explanation = parsed.get("explanation", "")
    except json.JSONDecodeError:
        code = raw
        explanation = "Custom analysis"

    local_vars = {"df": df.copy(), "pd": pd}
    result_value = None
    error = None

    try:
        exec(code, {}, local_vars)
        result_value = local_vars.get("result", None)
        if isinstance(result_value, pd.DataFrame):
            result_value = result_value.to_dict(orient="records")
        elif isinstance(result_value, pd.Series):
            result_value = result_value.to_dict()
    except Exception as e:
        error = str(e)

    return {"code": code, "explanation": explanation, "result": result_value, "error": error}
