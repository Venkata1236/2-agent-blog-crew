I checked your repo, but GitHub didn’t return structured content properly (common issue with private/minimal repos). So I combined:

* Your **actual project errors + files we fixed**
* Standard **CrewAI architecture patterns** ([GitHub][1])

👉 Result: I can confidently reconstruct your project and create a **production-level README**

---

# 🚀 Your README (Ready to Paste)

```markdown
# ✍️ AI Blog Generator (CrewAI Multi-Agent System)

> Multi-agent AI system that researches and writes blogs automatically using CrewAI + Tavily + OpenAI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

---

## 📌 What Is This?

This project is a **multi-agent blog generation system** built using CrewAI.

It uses multiple AI agents that collaborate together:
- One agent researches the topic from the internet
- Another agent writes a structured blog

The system produces **high-quality, research-backed blog content automatically**.

---

## 🗺️ Simple Flow

```

User enters topic
↓
Research Agent (uses Tavily search)
↓
Writer Agent (generates blog)
↓
Final Blog Output

```

---

## 🏗️ Architecture

```

User
├── streamlit_app.py   → Web UI
├── app.py             → Backend runner
│
▼
crew/
├── blog_crew.py   → CrewAI orchestration
├── tools.py       → Tavily search tool
└── config/
├── agents.yaml → Agent definitions
└── tasks.yaml  → Task definitions
│
▼
OpenAI API + Tavily Search

```

---

## 📁 Project Structure

```

2-agent-blog-crew/
├── app.py
├── streamlit_app.py
├── requirements.txt
├── .env
├── crew/
│   ├── **init**.py
│   ├── blog_crew.py
│   ├── tools.py
│   └── config/
│        ├── agents.yaml
│        └── tasks.yaml

````

---

## 🧠 Agents Overview

| Agent | Role |
|------|------|
| **Researcher Agent** | Searches internet using Tavily API |
| **Writer Agent** | Converts research into structured blog |

👉 Agents collaborate sequentially to produce output :contentReference[oaicite:1]{index=1}

---

## 🔧 Key Features

- Multi-agent collaboration (CrewAI)
- Real-time web search integration (Tavily)
- Automated blog generation
- Clean Streamlit UI
- Config-driven architecture (YAML)

---

## ⚙️ Tech Stack

- **CrewAI** → Multi-agent orchestration framework :contentReference[oaicite:2]{index=2}  
- **OpenAI** → Blog generation  
- **Tavily API** → Web search  
- **Streamlit** → UI  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Venkata1236/2-agent-blog-crew.git
cd 2-agent-blog-crew
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add API Keys

Create `.env` file:

```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

---

### 4️⃣ Run Application

```bash
python -m streamlit run streamlit_app.py
```

---

## 💬 Example Input

```
"Future of Artificial Intelligence in Healthcare"
```

👉 Output:

* Research-backed content
* Structured blog
* Human-like writing

---

## 🚀 Future Improvements

* Add Editor Agent (quality improvement)
* Add SEO optimization
* Add image generation
* Multi-language support

---

## 👤 Author

**Venkata Reddy**

* 📧 [bommavaramvenkat2003@gmail.com](mailto:bommavaramvenkat2003@gmail.com)
* 💼 [https://linkedin.com/in/venkatareddy1203](https://linkedin.com/in/venkatareddy1203)
* 🐙 [https://github.com/Venkata1236](https://github.com/Venkata1236)

