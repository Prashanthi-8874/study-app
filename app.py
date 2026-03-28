import streamlit as st
import time

st.set_page_config(page_title="Study Timer App", layout="centered")

st.title("📚 Study Timer with Break (Pomodoro)")

# ---------------- INPUT ----------------
study_minutes = st.number_input("Study Time (minutes)", min_value=1, value=25)
break_minutes = st.number_input("Break Time (minutes)", min_value=1, value=5)

# ---------------- SESSION STATE ----------------
if "running" not in st.session_state:
    st.session_state.running = False

if "mode" not in st.session_state:
    st.session_state.mode = "Study"

if "seconds_left" not in st.session_state:
    st.session_state.seconds_left = study_minutes * 60

# ---------------- START BUTTON ----------------
if st.button("▶ Start Timer"):
    st.session_state.running = True
    st.session_state.mode = "Study"
    st.session_state.seconds_left = study_minutes * 60

# ---------------- TIMER LOGIC ----------------
placeholder = st.empty()

if st.session_state.running:

    while st.session_state.running and st.session_state.seconds_left > 0:

        mins, secs = divmod(st.session_state.seconds_left, 60)

        placeholder.markdown(f"""
        ## {st.session_state.mode} Time ⏳
        ### {mins:02d}:{secs:02d}
        """)

        time.sleep(1)
        st.session_state.seconds_left -= 1

    # Switch mode
    if st.session_state.mode == "Study":
        st.session_state.mode = "Break"
        st.session_state.seconds_left = break_minutes * 60
    else:
        st.session_state.mode = "Study"
        st.session_state.seconds_left = study_minutes * 60

    st.session_state.running = False

    st.success(f"{st.session_state.mode} session started!")

# ---------------- STOP BUTTON ----------------
if st.button("⏹ Stop Timer"):
    st.session_state.running = False
    st.warning("Timer stopped")
