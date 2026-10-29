from pathlib import Path

import streamlit as st


APP_SCRIPT = Path(__file__).resolve().parents[1] / "app.py"

app = st.App(str(APP_SCRIPT))
