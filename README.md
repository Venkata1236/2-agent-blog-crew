# 🤖 2-Agent Blog Crew

> 2-agent CrewAI crew — Researcher + Writer auto-generate a blog post

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![Tavily](https://img.shields.io/badge/Tavily-Search-blue)

---

## 📌 What Is This?

A 2-agent CrewAI crew that auto-generates blog posts. The Researcher agent searches the web for real information about a topic. The Writer agent turns that research into a polished, publish-ready blog post. Built using CrewAI Agents, Tasks, Crew, YAML config, and sequential process.

---

## 🗺️ Simple Flow
```
User provides topic
        ↓
  [Researcher Agent]
  Searches web with Tavily
  Produces detailed research notes
        ↓
  [Writer Agent]
  Reads research notes
  Writes full blog post (600-800 words)
        ↓
  Final blog displayed + downloadable
```

---

## 🏗️ Detailed Architecture
```
User
 ├── streamlit_app.py     → Web UI
 └── app.py               → Terminal interface
          │
          ▼
      crew/
      ├── blog_crew.py    → Loads YAML + wires agents, tasks, crew
      └── tools.py        → Tavily search tool for researcher
          │
          ▼
      config/
      ├── agents.yaml     → Agent definitions (role, goal, backstory)
      └── tasks.yaml      → Task definitions (description, expected output)
          │
          ▼
      CrewAI → sequential process
      OpenAI → gpt-4o-mini
      Tavily → web search
```

---

## 📁 Project Structure
```
2-agent-blog-crew/
├── app.py                  ← Terminal version
├── streamlit_app.py        ← Web UI (deploy this)
├── config/
│   ├── agents.yaml         ← Agent role, goal, backstory
│   └── tasks.yaml          ← Task description, expected output
├── crew/
│   ├── __init__.py
│   ├── blog_crew.py        ← Crew definition
│   └── tools.py            ← Tavily search tool
├── .env                    ← API keys (never push!)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Key Concepts

| Concept | What It Does |
|---|---|
| **Agent** | Autonomous AI worker with role, goal, backstory |
| **Task** | Work assigned to an agent with description + expected output |
| **Crew** | Orchestrates agents and tasks together |
| **Sequential Process** | Researcher finishes → output passed to Writer |
| **YAML Config** | Agent and task definitions in clean config files |
| **context=[...]** | Writer task receives researcher task output automatically |

---

## 🔄 CrewAI vs LangGraph

| Feature | LangGraph | CrewAI |
|---|---|---|
| Control | Full — you define every node and edge | High level — agents decide how to work |
| Complexity | More code | Less code |
| Flexibility | Maximum | Less customizable |
| Best for | Complex workflows needing precise control | Multi-agent collaboration |

---

## ⚙️ Local Setup

**Step 1 — Clone:**
```bash
git clone https://github.com/venkata1236/2-agent-blog-crew.git
cd 2-agent-blog-crew
```

**Step 2 — Install:**
```bash
pip install -r requirements.txt
```

**Step 3 — Add API keys:**

`.env`:
```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

`.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your_openai_key"
TAVILY_API_KEY = "your_tavily_key"
```

**Step 4 — Run:**
```bash
python -m streamlit run streamlit_app.py
python app.py
```

---

## 🚀 Deploy on Streamlit Cloud

1. Push to GitHub
2. Go to share.streamlit.io
3. Connect repo → select `streamlit_app.py`
4. Settings → Secrets → add both API keys
5. Click Deploy ✅

---

## 📦 Tech Stack

- **CrewAI** — Agents, Tasks, Crew, sequential process
- **crewai-tools** — TavilySearchResults for web research
- **OpenAI** — GPT-4o-mini
- **Streamlit** — Web UI
- **python-dotenv** — API key management

---

## 👤 Author

**Venkata Reddy Bommavaram**
- 📧 bommavaramvenkat2003@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/venkatareddy1203)
- 🐙 [GitHub](https://github.com/venkata1236)