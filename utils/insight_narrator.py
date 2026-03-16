import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def narrate_insights(question: str, analysis: dict, summary: dict) -> str:
    if analysis.get("error"):
        return f"⚠️ I ran into an issue: `{analysis['error']}`. Try rephrasing your question."

    result = analysis.get("result")

    system_prompt = """You are a friendly data analyst explaining findings to a non-technical audience.
Be conversational, concise, and highlight the most interesting insight first.
Use bullet points only when listing multiple items. Keep it under 150 words.
Never mention code or technical details — just the findings."""

    user_prompt = f"""
The user asked: "{question}"

Analysis result:
{json.dumps(result, default=str, indent=2)}

Dataset context:
- {summary['rows']} rows, {summary['cols']} columns
- Numeric columns: {summary['numeric_columns']}
- Categorical columns: {summary['categorical_columns']}

Narrate the key insight in plain English.
"""

    message = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
    )

    return message.choices[0].message.content.strip()
