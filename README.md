# AI API Builder 🚀

> Prompt → Backend API in seconds

AI API Builder is an intelligent developer tool that converts natural language prompts into fully functional FastAPI backend APIs.

Built under **[BackendDeveloperHub (BDH)](https://github.com/BackendDeveloperHub)** — an open source organization created to help new developers learn backend development through real projects.

🔗 **Live Demo:** https://ai-api-builder.onrender.com

---

## ✨ Features

- 🧠 Natural language → FastAPI backend code
- ⚡ Automatic CRUD API generation
- 🗄️ Database model generation (SQLAlchemy + SQLite)
- 📦 Ready-to-run project structure
- 🤖 Powered by Groq AI (LLaMA 3.3)
- 🧩 Developer productivity tool for beginners

---

## 🏗️ Architecture

```
User Prompt
↓
FastAPI Backend (/api/generate)
↓
Groq AI (LLaMA 3.3-70b)
↓
Generated FastAPI Code
↓
Displayed in Browser
```

---

## 📂 Project Structure

```
ai-api-builder/
│
├── main.py           # FastAPI app entry point
├── requirements.txt  # Python dependencies
├── index.html        # Frontend UI
└── README.md
```

---

## ⚙️ Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Python + FastAPI        |
| AI Model  | Groq API (LLaMA 3.3-70b)|
| Frontend  | HTML + CSS + JavaScript |
| Hosting   | Render (free tier)      |
| Server    | Uvicorn                 |

---

## 🍴 Fork & Run Your Own Instance

Want to run AI API Builder with your own API key? Follow these steps:

### Step 1 — Fork the Repo

Click the **Fork** button on the top right of this repo.

Or clone directly:
```bash
git clone https://github.com/BackendDeveloperHub/ai-api-builder.git
cd ai-api-builder
```

---

### Step 2 — Get Your FREE Groq API Key

Groq provides a **free API key** with generous limits.

1. Go to 👉 https://console.groq.com
2. Sign up / Login (free)
3. Click **"API Keys"** on the left sidebar
4. Click **"Create API Key"**
5. Copy the key — looks like: `gsk_xxxxxxxxxxxxxxxxxxxx`

---

### Step 3 — Add Your API Key

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=gsk_your_key_here
```

> ⚠️ Never push your `.env` file to GitHub! It's already in `.gitignore`.

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 5 — Run Locally

```bash
uvicorn main:app --reload
```

Open your browser: http://localhost:8000

---

## 🌐 Deploy to Render (Free Hosting)

### Step 1 — Create Render Account
Go to 👉 https://render.com and sign up free.

### Step 2 — New Web Service
- Click **"New"** → **"Web Service"**
- Connect your **GitHub account**
- Select your **forked repo**

### Step 3 — Configure Settings

| Setting        | Value                        |
|----------------|------------------------------|
| Environment    | Python                       |
| Build Command  | `pip install -r requirements.txt` |
| Start Command  | `uvicorn main:app --host 0.0.0.0 --port 8000` |

### Step 4 — Add Environment Variable
- Go to **"Environment"** tab
- Add: `GROQ_API_KEY` = `your_groq_api_key_here`

### Step 5 — Deploy!
Click **"Create Web Service"** — Render will build and deploy automatically. ✅

Your live URL will be: `https://your-app-name.onrender.com`

---

## 🚀 Example

**Prompt:**
```
Create API for a todo application with title, description and status
```

**Generated API:**
- `POST /todos`
- `GET /todos`
- `PUT /todos/{id}`
- `DELETE /todos/{id}`

---

## ⚠️ Important Note for Developers

AI-generated code is **not always production-ready**. While testing this tool, I found 3 real bugs in the output:

- ❌ **Circular Import** — routes.py importing from main.py and vice versa
- ❌ **Function Name Conflict** — helper and route function with same name
- ❌ **Missing Import** — SessionLocal used but not imported

AI gives you **90% of the work in seconds**.  
But you still need to **understand the code** to fix the last 10%.  
That's exactly why BDH exists — to build that understanding.

---

## 💡 Use Cases

- Rapid API prototyping
- Learning FastAPI structure
- Beginner backend projects
- Startup MVP building

---

## ⭐ Future Improvements

- [ ] Multi-database support (PostgreSQL, MySQL)
- [ ] Authentication generation (JWT)
- [ ] Docker project export
- [ ] Microservice generation
- [ ] Code explanation agent
- [ ] Security check agent

---

## 🏢 About BackendDeveloperHub

**BackendDeveloperHub (BDH)** is an open source GitHub organization created for new developers who want to learn backend development through real projects — not just tutorials.

👉 https://github.com/BackendDeveloperHub

---

## 👨‍💻 Author

**Prabakaran**  
Self-taught backend developer | Open source enthusiast  
👉 https://github.com/Prabakaran202

---

## 📄 License

MIT License — free to use, fork, and modify.
