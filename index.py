import streamlit as st
from datetime import date

# -----------------------------
# Exam Countdown Configuration
# -----------------------------
EVENTS = [
    ("Exams Begin - RPA Exam", date(2025, 4, 30)),
    ("2 Exams Done - Computer Vision Exam", date(2025, 5, 3)),
    ("3 Exams Done - Reinforcement Learning Exam", date(2025, 5, 8)),
    ("Exams over", date(2025, 5, 10)),
]

# -----------------------------
# Helper Functions
# -----------------------------

def days_left(target: date, today: date) -> int:
    """Return the number of days between *today* and the *target* date."""
    return (target - today).days


# -----------------------------
# Main App Logic
# -----------------------------

today = date.today()
upcoming_events = [(label, d) for label, d in EVENTS if d >= today]

if upcoming_events:
    st.title("Exam Countdown")
    for label, d in upcoming_events:
        remaining = days_left(d, today)
        with st.container(border=True):
            st.markdown(f"❌ **{label}**")
            if remaining == 0:
                st.markdown("**Today!** 🎯")
            else:
                st.markdown(f"{remaining} day{'s' if remaining != 1 else ''} remaining")
else:
    # All exams have passed — show celebratory message.
    st.markdown(
        "<h1 style='text-align:center;font-size:3rem;'>Fcuk NMIMS Freedom.</h1>",
        unsafe_allow_html=True,
    )
