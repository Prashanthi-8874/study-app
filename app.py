import streamlit as st
import time

st.set_page_config(page_title="10th Study App", layout="wide")

st.title("📘 Charan's 10th Class Study + Quiz App")

# ---------------- DATA ----------------
data = {
    "Maths": {
        "syllabus": ["Algebra", "Trigonometry", "Geometry"],
        "questions": [
            ("2 + 2 = ?", ["3", "4", "5"], "4"),
            ("5 × 3 = ?", ["10", "15", "20"], "15")
        ]
    },
    "Social": {
        "syllabus": ["History", "Geography", "Civics"],
        "questions": [
            ("Capital of India?", ["Delhi", "Mumbai", "Chennai"], "Delhi"),
            ("India is a ____ country?", ["Monarchy", "Democratic", "Dictatorship"], "Democratic")
        ]
    },
    "Physics": {
        "syllabus": ["Motion", "Force", "Work"],
        "questions": [
            ("Unit of force?", ["Newton", "Joule", "Watt"], "Newton")
        ]
    }
}

# ---------------- AUDIO (UPLOAD alarm.mp3 in repo) ----------------
def play_sound():
    try:
        audio_file = open("alarm.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    except:
        st.warning("⚠️ Upload alarm.mp3 in GitHub repo for sound")

# ---------------- SUBJECT ----------------
subject = st.selectbox("📚 Select Subject", list(data.keys()))

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["📖 Syllabus", "⏱️ Timer", "❓ Quiz"])

# ---------------- SYLLABUS ----------------
with tab1:
    st.subheader(f"{subject} Syllabus")
    for topic in data[subject]["syllabus"]:
        st.write("•", topic)

# ---------------- TIMER ----------------
with tab2:
    st.subheader("Study Timer")

    study_time = st.number_input("Study Time (minutes)", 1, 120, 1)
    break_time = st.number_input("Break Time (minutes)", 1, 60, 1)

    if st.button("Start Study Session"):

        st.info("📖 Study Started...")

        # Study Timer
        seconds = study_time * 60
        placeholder = st.empty()

        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            placeholder.markdown(f"### 🧠 Study Time: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1

        st.success("🎉 Study Time Completed!")

        # Siren Alert
        st.balloons()
        st.warning("⏰ TIME UP! Take a break")

        play_sound()

        # Break Timer
        st.info("☕ Break Started")

        seconds = break_time * 60
        placeholder2 = st.empty()

        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            placeholder2.markdown(f"### ☕ Break Time: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1

        st.success("✅ Break Finished!")
        st.balloons()
        play_sound()

# ---------------- QUIZ ----------------
with tab3:
    st.subheader(f"{subject} Quiz")

    questions = data[subject]["questions"]
    score = 0

    for i, (q, options, correct) in enumerate(questions):

        st.write(f"Q{i+1}: {q}")
        ans = st.radio("Choose:", options, key=f"{subject}_{i}")

        if st.button(f"Submit Q{i+1}", key=f"submit_{i}"):
            if ans == correct:
                st.success("Correct ✅")
                score += 1
            else:
                st.error("Wrong ❌")

    if st.button("Show Final Score"):
        st.info(f"Score: {score}/{len(questions)}")
