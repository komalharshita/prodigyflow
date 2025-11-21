# agents/visualization_agent.py
"""
Visualization Agent for ProdigyFlow
-----------------------------------
Generates basic visual charts from the cleaned dataset:
- Histogram of numeric columns
- Correlation heatmap
- Bar chart of average subject performance

Simple, beginner-friendly version suitable for capstone projects.
"""

import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Directory for saving charts
VIS_DIR = Path("visuals")
VIS_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# MAIN VISUALIZATION FUNCTION
# ---------------------------------------------------------
def create_visualizations(cleaned_csv_path: str, logger=None):
    if logger:
        logger.info("Loading dataset for visualization...")

    df = pd.read_csv(cleaned_csv_path)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    # ---- Histogram for each numeric column ----
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        file_path = VIS_DIR / f"{col}_distribution.png"
        plt.savefig(file_path, bbox_inches="tight")
        plt.close()

    # ---- Correlation heatmap ----
    plt.figure(figsize=(7, 5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    heatmap_path = VIS_DIR / "correlation_heatmap.png"
    plt.savefig(heatmap_path, bbox_inches="tight")
    plt.close()

    # ---- Average marks bar chart (if available) ----
    subject_columns = [c for c in numeric_cols if "marks" in c]

    if len(subject_columns) > 0:
        averages = df[subject_columns].mean()

        plt.figure(figsize=(6, 4))
        averages.plot(kind="bar")
        plt.title("Average Subject Marks")
        plt.ylabel("Average Score")
        plt.xticks(rotation=45)
        avg_path = VIS_DIR / "avg_marks_bar_chart.png"
        plt.savefig(avg_path, bbox_inches="tight")
        plt.close()

    # ---- Done message ----
    if logger:
        logger.info("Visualization completed successfully.")

    return {
        "status": "visualization_complete",
        "charts_saved_to": str(VIS_DIR.resolve()),
        "generated_charts_count": len(numeric_cols) + 2,  # histograms + heatmap + avg chart
    }


# ---------------------------------------------------------
# Terminal formatting helpers
# ---------------------------------------------------------
BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"

def section(title: str):
    print(f"\n{BOLD}{CYAN}=== {title} ==={RESET}")


# ---------------------------------------------------------
# DRY RUN
# ---------------------------------------------------------
if __name__ == "__main__":
    print(f"{BOLD}📊 Running a dry test of visualization_agent...{RESET}")

    sample_path = "data/data_science_student_marks.csv"
    sample_path = str(Path(sample_path).resolve())

    print("\n📂 Using file:", sample_path)

    try:
        result = create_visualizations(sample_path)

        section("VISUALIZATION SUMMARY")
        print(result)

        print(f"\n{GREEN}✔ Charts generated successfully and saved to /visuals folder{RESET}\n")

    except FileNotFoundError:
        print("❌ Sample file not found. Dry run complete.")
