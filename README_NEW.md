# AI Resume Analyzer

A Streamlit application for reviewing resumes, building a resume, exploring job-search resources, and viewing analysis activity.

## Features

- **Resume analyzer:** Extracts text from PDF and DOCX resumes and provides resume feedback. AI-powered analysis uses Google Gemini when configured.
- **Resume builder:** Create a resume using the application's guided form.
- **Dashboard:** View resume and analysis information saved by the application.
- **Job search:** Explore job-search resources and roles.
- **Feedback:** Submit feedback from within the app.

Some capabilities, including AI analysis, job search, and OCR for scanned PDFs, may require API credentials or additional system software.

## Requirements

- Python 3.10 or newer
- pip
- Windows, macOS, or Linux

For OCR of scanned PDFs, install Tesseract OCR and Poppler separately and make them available to the application. Ordinary text-based PDF and DOCX extraction does not require OCR.

## Run locally

Open a terminal in the project directory.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell prevents environment activation, either allow local scripts for your user or run the commands below without activating the environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit prints a local URL in the terminal when the app starts. Open that URL in your browser.

## Configure AI analysis

AI analysis requires a Google AI API key. Create a `.env` file in the project directory and add:

```dotenv
GOOGLE_API_KEY=your_google_api_key
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey). Keep API keys private; do not commit `.env` or paste credentials into source files. Without a configured key, AI-powered analysis may not be available.

## Data and privacy

The application initializes local SQLite databases for application data. Uploaded resumes can contain sensitive personal information; only upload files you are authorized to process. When you use AI analysis, resume text may be sent to the configured AI provider for processing. Review the provider's privacy terms and the project's [AI model notes](AI_MODELS.md) before using that feature.

Do not use the included local database files as durable production storage. Back up or remove locally stored data as appropriate for your use.

## Project layout

```text
app.py                  Streamlit application entry point
config/                 Application configuration and database helpers
dashboard/              Dashboard views
feedback/               Feedback features
jobs/                   Job-search features
utils/                  Resume analysis and resume-building helpers
style/                  Application styles
assets/                 Images and other static assets
requirements.txt        Python dependencies
AI_MODELS.md            AI provider and analysis notes
DEPLOYMENT.md           Deployment guidance
```

## Deployment

For deployment-specific instructions, see [DEPLOYMENT.md](DEPLOYMENT.md). Hosting requirements vary: OCR, browser automation, persistent storage, and Streamlit session support may require additional configuration.

## Disclaimer

This tool provides automated suggestions, not professional career, hiring, or legal advice. Review and verify generated content before using it.
