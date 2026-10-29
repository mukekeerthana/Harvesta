# Harvesta — Smart Agriculture Assistant

Harvesta is a small Python + Streamlit student mini project.

## Features
- Upload a crop-leaf photo.
- Optional Gemini AI observations when `GEMINI_API_KEY` is configured.
- Demo market-price table with sample values clearly labelled as not live.

## Run on Windows
1. Install Python 3.10 or newer from https://www.python.org/downloads/ (select “Add Python to PATH”).
2. Extract this ZIP and open Command Prompt in the project folder.
3. Run:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app.py
```

## Optional Gemini API
Set the key as an environment variable; do not hardcode or upload it.

```bat
set GEMINI_API_KEY=YOUR_API_KEY_HERE
streamlit run app.py
```

Without a key, the app runs in demo mode and does not pretend to analyze the image with AI.

## Limitations
Market values are illustrative sample data, not live prices. AI observations may be inaccurate and should be confirmed by an agricultural expert. Do not use demo values for real selling decisions.

Suggested GitHub repository name: `harvesta-smart-agriculture`
