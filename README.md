#  Smart Note Simplifier & Formula Extractor

This GenAI-powered web app helps students simplify complex academic notes, extract mathematical formulas, and identify key concepts — all in one place.

## Features

-  Upload `.pdf` or `.txt` files (lecture notes, textbooks, etc.)
-  Extracts **important keywords** using NLP
-  Identifies and highlights **mathematical formulas**
-  Summarizes content into **short, clean bullet points**
-  Optional **"Kid Mode"** to simplify text into beginner-level English

##  Demo Flow

1. Upload a PDF or text note  
2. App will:
   - Show top keywords
   - Detect common formulas
   - Summarize content
   - Optionally simplify complex text into kid-friendly form

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| UI | Streamlit |
| AI Model | Gemini Pro API (Google AI Studio) |
| Text Extraction | PyMuPDF |
| Keyword Extraction | TF-IDF (scikit-learn) |
| Formula Detection | Regex-based parsing |
| Summarization & Simplification | Gemini API prompt-based |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/afnan128-max/smart-note-simplifier.git
cd smart-note-simplifier

# Install dependencies
pip install -r requirements.txt


Save summaries & flashcards to profile

Support LaTeX rendering for math

Add voice-to-text note support

Multi-language explanation mode

