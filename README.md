# AI Resume Analyzer

AI Resume Analyzer is a Streamlit application for reviewing resumes, improving ATS compatibility, building polished resumes, and exploring relevant job opportunities.

## Features

- Standard and AI-powered resume analysis
- ATS score and keyword matching insights
- Resume builder with downloadable documents
- Resume analytics dashboard
- Job search and LinkedIn scraping tools
- Feedback collection and admin tools

## Requirements

- Python 3.10 or newer
- Google Chrome for browser-based job search features
- API credentials configured in your environment when using AI analysis

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501).

On Windows, `startup.bat` can also be used to start the application. The project includes a Streamlit configuration that hides the Deploy toolbar option.

## Project Structure

```text
app.py                 Streamlit application entrypoint
style/                 Shared UI styling
utils/                 Resume parsing, analysis, and generation
dashboard/             Analytics dashboard
jobs/                  Job search and scraper features
config/                Roles, courses, and database helpers
feedback/              Feedback form and storage
```

## Security

Do not commit API keys, passwords, uploaded resumes, generated databases, or other private data. Review [SECURITY.md](SECURITY.md) before deploying the application.
