# **ProdigyFlow: AI Study & Productivity Concierge**

ProdigyFlow is a **multi-agent academic assistant** designed to help students plan, learn, research, and improve productivity using AI, which I built for the **Google × Kaggle AI Agents Intensive (2025) Capstone Project**.

---

## Overview

ProdigyFlow uses a team of AI agents to automate:

* Study planning
* Research & note generation
* Doubt solving
* Flashcards & summaries
* Topic mastery checks
* Progress tracking
* Personalized learning using memory

The goal is to reduce manual workload and help students study smarter.

---

## Core Features

* **Orchestrator Agent** → routes tasks
* **Study Planner Agent** → builds daily/weekly plans
* **Research Agent** → finds resources & creates summaries
* **Doubt Solver Agent** → explains concepts / solves problems
* **Mastery Checker Agent** → quizzes + evaluates weak areas
* **Loop Agent** → continuous improvement
* **Memory Bank** → stores progress, preferences, past results

Tools used: Google Search, Code Execution, custom tools, session state & memory.

---

## Architecture

```
Orchestrator
│
├── Study Planner Agent
├── Research Agent
├── Doubt Solver Agent
└── Mastery Checker Agent

Shared:
- Memory Bank
- Custom Tools
- Gemini LLM
```

---

## Setup

```bash
git clone https://github.com/komalharshita/prodigyflow.git
cd prodigyflow
pip install -r requirements.txt
export GOOGLE_API_KEY="your_key"
```

Run the demo:

```
notebook/prodigyflow_demo.ipynb
```

---

## Some use cases 

```
"Create a 7-day study plan for DBMS, OS, DSA."
"Summarize SQL joins and provide practice problems."
"Explain recursion with examples."
"Make 10 flashcards for Machine Learning basics."
"Quiz me on Operating Systems."
```

---

## Key concepts learned like

* Multi-agent system
* Custom tools
* Search & code execution tools
* Memory & session state
* A2A communication
* Loop agents
* Observability
* Gemini LLM integration

---

## Summary

ProdigyFlow is a practical academic productivity system that automates study workflows and showcases real agent architecture. I have tried to apply the key concepts from AI Agents Intensive course.

---

