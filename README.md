# 🧠 UPSC Mains Answer Generator

A **Streamlit-powered AI app** that generates structured, exam-oriented **UPSC Mains-style answers** using Google Gemini.  
It follows official **UPSC answer-writing best practices** — with clear introductions, multi-dimensional subheadings, and crisp conclusions enriched with data, committee references, and government reports.

---

## 🚀 Features

✅ Generates high-quality, analytical UPSC-style answers  
✅ Automatically structures answers with:
- Introduction (2 lines, with data or background)
- Multi-dimensional body (logical subheadings + bullet points)
- Conclusion (2 lines, with optimism and real references)


✅ Clean Streamlit UI with fixed footer  
✅ Adjustable word limit  
✅ Real-time generation using Google Gemini API  

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Frontend/UI** | Streamlit |
| **Backend** | Python |
| **AI Model** | Google Gemini (via `pydantic_ai`) |
| **Environment** | dotenv |
| **Libraries** | `streamlit`, `google-genai`, `pydantic`, `python-dotenv` |

---
## ⚙️ Installation & Setup

Follow the steps below to set up and run the UPSC Mains Answer Generator locally.

---

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/upsc-answer-generator.git
cd upsc-answer-generator
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
```bash
GEMINI_KEY=your_google_gemini_api_key_here
```
### 5. Run the Streamlit App
```bash
streamlit run app.py
```
