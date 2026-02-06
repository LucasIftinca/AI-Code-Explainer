# AI Code Explainer

An intelligent web application that breaks down complex code snippets into easy-to-understand explanations using Google Gemini 2.0 Flash.

## Features
- **Instant Analysis:** Paste code in any language and get a step-by-step breakdown.
- **AI Powered:** Leverages the latest Gemini 2.0 Flash model for high-speed, accurate explanations.
- **Clean UI:** Modern dark-mode interface built with Flask and styled with CSS.
- **Markdown Support:** Explanations are beautifully formatted for readability using Marked.js.

## Tech Stack
- **Backend:** Python (Flask)
- **AI Integration:** Google GenAI SDK
- **Frontend:** HTML5, CSS3, JavaScript

## Setup & Installation

1. **Clone the repository**
   git clone https://github.com/LucasIftinca/AI-Code-Explainer.git
   cd AI-Code-Explainer

2. **Create and activate a virtual environment**
   python3 -m venv venv
   source venv/bin/activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Configure your API Key**
   export GEMINI_API_KEY='your_api_key_here'

5. **Run the application**
   python app.py

---
**Author:** Lucas-Ștefan Iftinca