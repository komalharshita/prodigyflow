# agents/analysis_agent.py
"""
Analysis Agent for ProdigyFlow
--------------------------------
Performs:
- Basic statistical analysis
- Correlation analysis
- Text-based summary insight generation (optional Gemini API support)
- Returns dictionary of insights + metadata

Designed to be easy to read, simple, and competition-friendly.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

# Optional Google Gemini API (fails gracefully)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


# --------------------------------------------
#  Gemini Configuration (Optional)
# --------------------------------------------
def configure_gemini(api_key: os.environ.get("YOUR_API_KEY")) -> bool:
    """
    Configures Gemini only if API key is provided and package is installed.
    """
    if api_key and GEMINI_AVAILABLE:
        genai.configure(api_key=api_key)
        return True
    return False


# --------------------------------------------
#  Helper Functions
# --------------------------------------------
def compute_basic_stats(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Returns summary statistics for numerical and categorical columns.
    """
    numerical = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()

    stats = {
        "num_columns": numerical,
        "cat_columns": categorical,
        "describe_numeric": df[numerical].describe().to_dict() if numerical else {},
        "missing_values": df.isna().sum().to_dict(),
        "unique_counts": {col: df[col].nunique() for col in df.columns}
    }
    return stats


def compute_correlations(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes pairwise correlations for numeric columns.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        return {"correlations": {}}

    corr = numeric_df.corr().round(3).fillna(0)
    high_corr_pairs = []

    for col in corr.columns:
        for idx in corr.index:
            if col != idx and abs(corr.loc[idx, col]) > 0.6:
                high_corr_pairs.append({
                    "feature_1": idx,
                    "feature_2": col,
                    "correlation": float(corr.loc[idx, col])
                })

    return {
        "correlation_matrix": corr.to_dict(),
        "high_correlation_pairs": high_corr_pairs
    }


def generate_ai_insights(df: pd.DataFrame, stats: Dict[str, Any], corr: Dict[str, Any]) -> str:
    """
    Uses Gemini to generate a natural-language analysis summary.
    Falls back to rule-based summary if Gemini is unavailable.
    """

    # If Gemini is not available → return simple summary
    if not GEMINI_AVAILABLE:
        return (
            "AI model unavailable — generated rule-based insights.\n"
            f"- Dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n"
            f"- Numerical features: {len(stats['num_columns'])}\n"
            f"- Categorical features: {len(stats['cat_columns'])}\n"
            f"- High correlations found: {len(corr['high_correlation_pairs'])}\n"
        )

    prompt = f"""
You are an AI Data Analyst. Summarize the dataset insights in simple,
professional language. Avoid technical jargon. Here is the analysis:

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Numerical Columns: {stats['num_columns']}
Categorical Columns: {stats['cat_columns']}

Missing Values: {stats['missing_values']}

Strong Correlations (> 0.6):
{corr['high_correlation_pairs']}

Give clear, meaningful insights suitable for a student competition project.
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return "Gemini failed to respond — using fallback rule-based insights."

if __name__ == "__main__":
    print("Running Analysis Agent...")

    # Path of your CSV
    csv_path = "data\\data_science_student_marks.csv"

    # Load dataset
    df = pd.read_csv(csv_path)

    # Compute stats
    stats = compute_basic_stats(df)

    # Compute correlations
    corr = compute_correlations(df)

    # Generate insights
    insights = generate_ai_insights(df, stats, corr)

    # Final structured result:
    result = {
        "timestamp": str(datetime.now()),
        "stats": stats,
        "correlations": corr,
        "ai_insights": insights,
    }

    print("\n=== ANALYSIS RESULT ===")
    print(result)
