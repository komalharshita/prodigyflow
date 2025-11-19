# **ProdigyFlow — Intelligent Data Analytics Agent**

*A Capstone Project for the Kaggle Agents Intensive Program*

<img width="900" height="550" alt="main thumbnai" src="https://github.com/user-attachments/assets/34db2c20-72e7-463f-8aff-ad6f65d977ea" />

---

## **Overview**

**ProdigyFlow** was created with a clear mission: to demonstrate how agentic systems can transform traditional data analytics by automating the entire workflow—from raw messy data to polished insights and dashboards. In a world where decision-making is becoming more fast-paced and data-heavy, intelligent agents offer a future-ready solution.

This project aims not just to analyze data, but to showcase what agent-powered automation can achieve in a professional analytics pipeline. **ProdigyFlow** is an end-to-end autonomous **Data Analytics Agent System** built to clean data, analyze trends, generate insights, and produce dashboards with minimal human intervention. Designed as part of the Kaggle Agents Intensive Capstone Project, ProdigyFlow demonstrates the power of agentic automation in real-world data workflows.

This project brings together intelligent agents, curated tools, and a smooth analytics pipeline—allowing you to go from *raw data → insights → reports → dashboards* automatically.

---

## **Team Members**

* **Komal Harshita** — Computer Science Engineering
* **Priyamvadha Sahasvi Nune** — Computer Science Engineering

---

## 🎯 **Why We Chose This Project**

We selected this idea because **agentic workflows represent the next evolution of data analytics and business intelligence.** As Computer Science engineering students, we wanted to build something that:

* Mimics real-world analytics pipelines
* Showcases advanced automation using agents
* Demonstrates our skills in Python, data analysis, dashboards, and system design
* Solves a common industry challenge: *turning data into insights faster and with fewer manual steps*

Additionally, building an AI-driven analytics system aligns strongly with future data engineering trends like:

* Autonomous BI
* Auto-EDA & Auto-reporting
* Multi-agent collaboration
* Tool-augmented analysis

This project is both academically valuable and professionally relevant.

---

## **Project Goals**

ProdigyFlow automates the core analytics lifecycle:

1. **Data Ingestion & Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Insight Generation & Reporting**
4. **Dashboard Creation & Publishing**

---

## **System Architecture**

ProdigyFlow consists of three main components:

* **Agent Layer** — Autonomous agents responsible for cleaning, analysis, and visualization.
* **Tools Layer** — Custom MCP tools that enhance agent capabilities.
* **Analytics Layer** — Dashboarding and reporting.
<insert arch diagram>

---

## **Repository Structure**

```
ProdigyFlow/
│
├── data/               
│   ├── raw/
│   └── cleaned/
├── agents/              
│   ├── main_agent.py
│   ├── cleaning_agent.py
│   ├── analysis_agent.py
│   └── visualization_agent.py
├── tools/               
│   ├── data_tools.py
│   ├── logging_tools.py
│   └── viz_tools.py
├── reports/             
│   ├── Executive_Report.pdf
│   ├── Findings.md
│   └── Architecture_Diagram.png
├── dashboard/          
├── prodigyflow-kaggle-notebook.ipynb
├── test_gemini.txt     
├── README.md
├── requirements.txt
└── LICENSE
```

---

## **Our Core Agents**


| **Agent Name**              | **Role**                  | **Key Responsibilities**                                                                                       | **Outputs**                                           |
| --------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Cleaning Agent**          | Data Preparation          | - Handle missing values<br>- Fix data types<br>- Detect & treat outliers<br>- Standardize dataset              | Clean dataset stored in `data/cleaned/`               |
| **Analysis Agent**          | Exploratory Data Analysis | - Generate descriptive stats<br>- Identify correlations & patterns<br>- Detect anomalies<br>- Extract insights | Insights text + summary files in `/reports`           |
| **Visualization Agent**     | Data Visualization        | - Create charts (matplotlib/plotly)<br>- Prepare figures for dashboards<br>- Generate export-ready visuals     | PNG/JPEG visual assets in `/reports` and `/dashboard` |
| **Main Orchestrator Agent** | Workflow Automation       | - Trigger all agents<br>- Manage pipeline flow<br>- Maintain logs<br>- Ensure reproducible execution           | Pipeline logs + consolidated results                  |

---

## **Dashboard**

It includes:

* Overview metrics
* Trend analysis
* Category-wise breakdowns
* Anomaly detection panels

---

## **Technologies Used**

* **Python** (Pandas, NumPy, Scikit-learn)
* **Agents & Automation**
* **Power BI** for dashboarding
* **Matplotlib / Plotly** for visualizations
* **MCP (Model Context Protocol)** tools

---

## **What We Learned**

Building **ProdigyFlow** helped us strengthen both technical and conceptual skills, including:

### **Technical Skills**

* Designing autonomous agent workflows
* Building modular Python architectures
* Cleaning and transforming datasets efficiently
* Performing deep exploratory analysis
* Creating visualizations and dashboards
* Writing structured reports & summaries
* Maintaining clean project architecture
* Understanding tool orchestration using MCP

### **Conceptual Learnings**

* How to convert a vague business problem into an analytics workflow
* The importance of reproducibility and documentation
* How to structure large-scale team projects
* How to evaluate data quality & readiness
* Collaborative development workflows using GitHub

This project enhanced our clarity on how modern data systems operate and the role of automation in analytics.

---

## **How to Run**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ProdigyFlow.git
cd ProdigyFlow
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Main Agent:

```bash
python agents/main_agent.py
```
---

## **License**

This project is licensed under the MIT License. See `LICENSE` for more information.

---

## **Acknowledgements**

This project was built as part of the **Kaggle Agents Intensive Capstone Project**. Special thanks to mentors and the Kaggle community for continuous support.

---
