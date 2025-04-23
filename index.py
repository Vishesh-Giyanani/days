import streamlit as st
from datetime import date



AI_EVENTS = [
    ("Exams Begin ‑ RPA Exam",             date(2025, 4, 30)),
    ("2 Exams Done ‑ Computer Vision Exam",               date(2025, 5, 3)),
    ("3 Exams Done ‑Reinforcement Learning Exam",        date(2025, 5, 8)),
    ("Exams get over",                     date(2025, 5, 10)),
]

CS_EVENTS = [
    ("Exams Begin ‑ REMA Exam",            date(2025, 4, 28)),
    ("2 Exams Done ‑ ISA Exam",            date(2025, 5, 2)),
    ("3 Exams Done ‑ MC Exam",             date(2025, 5, 10)),
    ("Exams get Over",                     date(2025, 5, 12)),
]

# ────────────────────────────────────────────────
# Helper
# ────────────────────────────────────────────────

def days_left(target: date, today: date) -> int:
    """Return *target − today* in days."""
    return (target - today).days


# ────────────────────────────────────────────────
# Page layout & toggle (top‑right)
# ────────────────────────────────────────────────

# Use columns so the toggle hugs the right side
left, right = st.columns([0.8, 0.2])
with right:
    is_ai = st.toggle("AI ↔︎ CS", value=True, key="track_toggle", help="Switch between AI and CS exam schedules")

selected_events = AI_EVENTS if is_ai else CS_EVENTS
track_label = "" if is_ai else ""

# ────────────────────────────────────────────────
# Main view
# ────────────────────────────────────────────────

today = date.today()
upcoming_events = [(label, d) for label, d in selected_events if d >= today]

if upcoming_events:
    st.title(f"{track_label} Exam Countdown")
    for label, d in upcoming_events:
        remaining = days_left(d, today)
        with st.container(border=True):
            st.markdown(f"❌ **{label}**")
            if remaining == 0:
                st.markdown("**Today!** 🎯")
            else:
                st.markdown(f"{remaining} day{'s' if remaining != 1 else ''} remaining")
else:
    st.markdown(
        "<h1 style='text-align:center;font-size:3rem;'>Fcuk NMIMS Freedom.</h1>",
        unsafe_allow_html=True,
    )
