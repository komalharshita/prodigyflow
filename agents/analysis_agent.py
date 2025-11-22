# agents/analysis_agent.py
#Analysis Agent for ProdigyFlow | Performs simple EDA and generates AI insights using Google ADK.

import pandas as pd
import os
import json
from pathlib import Path
import re

try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    ADK_AVAILABLE = True
except Exception:
    ADK_AVAILABLE = False

def generate_adk_insights(text: str) -> str:
    if not ADK_AVAILABLE:
        return "AI summary unavailable (ADK not installed)."

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = (
            "Convert the dataset insights into clean, simple bullet points. "
            "Do not use markdown symbols like ** or *. Be concise.\n\n"
            f"Insights:\n{text}"
        )

        response = model.generate_content(prompt)

        raw = response.text.replace("\\n", "\n").strip()

        cleaned = raw.replace("**", "").replace("*   ", "").replace("* ", "")

        lines = cleaned.splitlines()
        normalized = []
        for line in lines:
            l = line.strip()
            if re.match(r"^[-•]\s+", l):
                l = "- " + l.split(maxsplit=1)[1]
            else:
                if l:
                    l = "- " + l
            l = re.sub(r"^(-\s*)+", "- ", l)

            normalized.append(l)
        if normalized and "key findings" in normalized[0].lower():
            normalized = normalized[1:]

        return "\n".join(line for line in normalized if line.strip())

    except Exception as e:
        return f"AI summary unavailable ({str(e)})."
        
# -------------------------
# Main Analysis Function
# -------------------------

def analyze(cleaned_csv_path: str, logger=None):
    if logger:
        logger.info("Loading cleaned dataset...")

    df = pd.read_csv(cleaned_csv_path)
    df.fillna("—", inplace=True)

    num_rows, num_cols = df.shape

    missing_count = df.isna().sum().to_dict()
    missing_percent = (df.isna().mean() * 100).round(2).to_dict()

    describe_stats = df.describe(include="all").to_dict()

    # Correlations
    try:
        corr_matrix = df.corr(numeric_only=True).round(3).to_dict()
    except:
        corr_matrix = {}

    insights = {
        "dataset_overview": {
            "rows": num_rows,
            "columns": num_cols,
            "column_names": list(df.columns),
        },
        "missing_values": {
            "count": missing_count,
            "percent": missing_percent,
        },
        "summary_statistics": describe_stats,
        "correlation_matrix": corr_matrix,
    }

    # AI summary
    adk_input_text = json.dumps(insights, indent=2)
    insights["ai_summary"] = generate_adk_insights(adk_input_text)

    metadata = {
        "status": "analysis_complete",
        "num_numeric_columns": len(df.select_dtypes(include="number").columns),
        "used_adk": ADK_AVAILABLE,
    }

    if logger:
        logger.info("Analysis completed successfully.")

    return insights, metadata

BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[96m"

def hr(title: str):
    print(f"\n{BOLD}{title}{RESET}")
    print("-" * len(title))


if __name__ == "__main__":
    print(f"🚀 {BOLD}Running a dry test of analysis_agent...{RESET}\n")

    sample_path = "data\\data_science_student_marks.csv"
    sample_path = str(Path(sample_path).resolve())

    print(f"📂 Using file: {sample_path}")

    try:
        insights, meta = analyze(sample_path)

        insights_no_ai = dict(insights)
        insights_no_ai.pop("ai_summary", None)

        hr("📊 INSIGHTS (Structured Data Overview)")
        print(json.dumps(insights_no_ai, indent=2))

        hr("🤖 AI-GENERATED SUMMARY")
        print(insights["ai_summary"])

        hr("📁 METADATA")
        print(json.dumps(meta, indent=2))

        print("\n✔ Analysis completed successfully!\n")

    except FileNotFoundError:
        print("Sample file not found. Dry run complete.\n")
