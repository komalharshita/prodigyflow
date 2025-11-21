# 🚀 ProdigyFlow — Intelligent Data Analytics Agent

ProdigyFlow is an **AI-powered multi-agent data analytics framework** designed to automate end-to-end exploratory analysis, visualization, insights generation, and reporting. It enables students, analysts, and researchers to turn raw datasets into meaningful business insights with minimal manual effort.

This project has been developed as part of an academic capstone initiative by:
**Komal Harshita & Priyamvadha Sahasvi Nune**,  
Department of Computer Science & Engineering.

---

## Project Motivation — Why We Chose This
In real-world business environments, analysts spend **70–80% of time cleaning, exploring, and summarizing data** before any modelling or decision-making. This process is repetitive, time-consuming, and prone to error.

We wanted to build a system that:
- **Speeds up exploratory analysis**
- **Automatically generates insights and visual summaries**
- **Allows anyone to analyze datasets without advance ML knowledge**
- Demonstrates practical learning combining **Python + Data Analytics + Gemini AI**

ProdigyFlow reflects our goal to create **simple, useful, modular tools** that solve real analytical problems while being easy for students and businesses to adopt.

---

## 🎯 Objectives
- Build a backend-first analytics automation system using agent architecture.
- Support data ingestion, cleaning, visualization, metadata extraction, and insight generation.
- Utilize **Gemini models** for natural-language summaries and understanding.
- Create a structured, competition-ready engineering pipeline.
- Deliver high-value analytical output with minimal coding.

---

## 🧠 Core Features

| Feature | Description |
|---------|------------|
| Automated Data Analysis Agent | Generates insights, metadata & summaries |
| Visualization Agent | Creates automated charts & visual summaries |
| Gemini-powered AI Summary | Natural-language insights from data |
| Structured Output Formatting | Clean and professional console reporting |
| Modular Agent Design | Add or replace agents independently |
| CSV/Excel Ingestion Support | Easily test custom datasets |

---

## 🤖 Core System Agents

| Agent Name | Responsibility | Output |
|----------- |---------------|--------|
| `analysis_agent.py` | Reads dataset, extracts statistics, generates Gemini summary | Insights, metadata JSON |
| `visualization_agent.py` | Generates visual graphs and saves locally | PNG charts |
| `cleaning_agent.py` | Cleans missing values, formatting, and structure | Cleaned dataset |
| `test_gemini.py` | Tests Gemini API connection | Model response output |

---

## 🧪 Running the Project Locally

### **1️⃣ Create and activate virtual environment**

```bash
python -m venv .venv
.\.venv\Scripts\activate         
source .venv/bin/activate   

```

### **2️⃣ Install dependencies**  

```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Analysis Agent**

```bash
python agents/analysis_agent.py
```

### **4️⃣ Test Gemini API**

```bash
python agents/test_gemini.py
```

---

## Add a Custom CSV file

Place your dataset inside the **data/** folder and update path in code:

```python
file_path = "data/your_file.csv"
```

---

## Sample Terminal Output Preview

```
🚀 Running a dry test of analysis_agent...

📂 Using file: data/student_marks.csv

📊 INSIGHTS (Structured Data Overview)
------------------------------------
{ ... dataset overview JSON ... }

🤖 AI-GENERATED SUMMARY
-----------------------
• Key performance trends detected  
• Distribution shows variation in subject performance  
• Potential improvement insights  

📁 METADATA
-----------
{ ... summary JSON ... }

✔ Analysis completed successfully!
```

---

## ✨ What We Learned

* Designing **modular agent architectures**
* Integrating **Gemini AI** with Python backends
* Automating analytics workflows like real data analysts
* Practical environment setup, dependency management & debugging
* Dataset quality, structure, visualization and reporting best practices
* Leveraging GitHub workflow and documentation standards

---

## Future Scope

🔹 Build a web-based interface using FastAPI/Streamlit
🔹 Add database integration and Auto-EDA dashboards
🔹 Support PDF report generation
🔹 Multi-file dataset comparison
🔹 Plug-and-play Machine Learning agent

ProdigyFlow is only the beginning — we plan to expand it into a fully intelligent analytical automation assistant.

---

## 🤝 Contributors

| Name                         | Role                                               |
| ---------------------------- | -------------------------------------------------- |
| **Komal Harshita**           | Lead Developer, Agent Architecture, AI Integration |
| **Priyamvadha Sahasvi Nune** | Data Research, Analytics, Testing & Documentation  |

---

## 🌟 Support

If you like this project, please ⭐ star the repository and share feedback!

### 🔗 Useful Links

📦 Repository
[https://github.com/komalharshita/prodigyflow](https://github.com/komalharshita/prodigyflow)

📘 Project Documentation
[https://komalharshita.github.io/prodigyflow/](https://komalharshita.github.io/prodigyflow/)

---

## 📝 License

This project is released under **MIT License** — feel free to use or modify with attribution.

---

### **Thank you for exploring ProdigyFlow!**
