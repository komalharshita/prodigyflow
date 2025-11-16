# **ProdigyFlow – A Multi-Agent Learning Assistant**

ProdigyFlow is a lightweight multi-agent AI system designed to improve student productivity by helping with study planning, research assistance, and doubt solving.
Built as part of the **Google x Kaggle AI Agents Intensive (Nov 2025)**, this project demonstrates practical use of agent orchestration, tool use, and session memory.

---

## ** My Project Overview**

Students often struggle with scattered resources, unstructured planning, and slow doubt resolution. ProdigyFlow solves this using three simple AI agents:

### **1. Study Planner Agent**

Creates daily or weekly study plans based on:

* syllabus/topics
* time availability
* difficulty levels

### **2. Research Assistant Agent**

Fetches explanations, summaries, examples, and structured notes for any topic.

### **3. Doubt Solver Agent**

Helps clarify concepts, explains mistakes, and answers technical questions.

Each agent is coordinated through a central **Orchestrator**, which routes the user’s query to the right agent.

---

## **Features Used (Course Requirements)**

This project demonstrates:

✔ Multi-Agent System (3 agents)
✔ Sequential Orchestration
✔ Simple Custom Tool (helper functions)
✔ Session Memory
✔ Context Management
✔ Clean Modularity & Logging

---

## **Architecture**

```
User → Orchestrator → Selected Agent → Response
                     ↑
                 Session Memory
```

* The **Orchestrator** interprets the user’s intent
* Passes it to the appropriate agent
* Agents use tools + memory to give helpful responses
* Memory keeps recent context across turns

---

## **Project Structure**

```
prodigyflow/
│
├── agents/
│   ├── study_planner.py
│   ├── research_assistant.py
│   └── doubt_solver.py
│
├── core/
│   ├── orchestrator.py
│   └── tools.py
│
├── memory/
│   └── session_memory.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## **How to Run**

1. Clone the repo

```bash
git clone https://github.com/yourusername/prodigyflow
cd prodigyflow
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the system

```bash
python main.py
```

---

## **Usage Example**

```
User: I have 4 hours today, help me plan study.
→ Study Planner Agent

User: Explain TCP handshake in simple terms.
→ Research Assistant Agent

User: Why is my SQL query wrong?
→ Doubt Solver Agent
```

---

## **Gemini Integration (LLM-Powered Agent)**

ProdigyFlow includes an optional **Gemini-powered Agent** using Google’s `google-generativeai` SDK.

### How it works

A dedicated `gemini_agent.py` file handles:

* LLM-based explanations
* Research enhancements
* Content generation

To enable it:

1. Get an API key from
   [https://aistudio.google.com](https://aistudio.google.com)
2. Add it to your environment:

```bash
export GOOGLE_API_KEY="your_key"
```

3. The orchestrator routes queries requiring richer reasoning to the Gemini Agent.

This addition enhances the project with **LLM augmentation**, satisfying optional advanced features for the course.

---

## **Submission Track**

**Track:** Concierge Agents
**Theme:** Student Productivity Assistant

---

## Acknowledgements

Built for the **Google x Kaggle AI Agents Intensive 2025**
Inspired by challenges faced by students in CS & Engineering.

---
