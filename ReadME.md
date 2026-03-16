# AI Data Analyst

An AI-powered data analysis tool built with Streamlit and LLaMA 3.3. Upload any CSV, ask questions in plain English, and get instant charts and insights — no coding required.

---

## How It Works

1. Upload a CSV file
2. Ask a question about your data in plain English
3. The AI writes and runs analysis code automatically
4. A chart is generated based on your question
5. The AI narrates the key finding in plain, conversational English

---

## Features

- Automatic CSV parsing with schema and type detection
- AI-generated pandas code that executes on your data in real time
- Smart chart selection — bar, line, scatter, histogram, or box plot
- Conversational chat interface with full message history
- Powered by LLaMA 3.3 70B via Groq (free API, no credit card needed)
- One-click deployable to Streamlit Cloud

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| AI Model | LLaMA 3.3 70B via Groq |
| Data Processing | Pandas |
| Charts | Plotly |
| Language | Python 3.10+ |

---

## Project Structure

```
ai-data-analyst/
├── app.py                    # Main Streamlit app and chat loop
├── utils/
│   ├── __init__.py
│   ├── csv_parser.py         # CSV upload and metadata extraction
│   ├── code_engine.py        # AI writes and runs analysis code
│   ├── chart_generator.py    # Automatic Plotly chart selection
│   └── insight_narrator.py   # AI narrates findings in plain English
├── sample_data/
│   └── sample.csv            # Sample dataset to try the app
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- A free Groq API key from [console.groq.com](https://console.groq.com)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-data-analyst.git
cd ai-data-analyst
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
```bash
cp .env.example .env
```
Open `.env` and paste your Groq API key:
```
GROQ_API_KEY=your_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## Example Questions

Try these with the included `sample_data/sample.csv`:

- "What are the top regions by sales?"
- "Show me the monthly revenue trend"
- "Are there any outliers in profit?"
- "Compare sales across categories"
- "Which category has the highest profit margin?"
- "Summarise this dataset"

---

## Deploy to Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in
3. Click **New app** → select your repo → set `app.py` as the entry point
4. Under **Settings → Secrets**, add:
```
GROQ_API_KEY = "your_key_here"
```
5. Click **Deploy** — live at `https://yourapp.streamlit.app` in minutes

---

## Roadmap

- [ ] Excel (.xlsx) file support
- [ ] Multi-file upload
- [ ] Export analysis as PDF report
- [ ] Natural language SQL for larger datasets
- [ ] Persistent chat memory across sessions

---

**Contributor

Aarnav Singhal
