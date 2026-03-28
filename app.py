import streamlit as st
import time

st.set_page_config(page_title="Student Study App", layout="centered")

st.title("📘 Prashanthi's Study & Quiz App")

# ---------------- SESSION STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------------- SUBJECT SELECTION ----------------
subjects = ["Maths", "Physics", "Chemistry", "Biology", "Social", "English"]
subject = st.selectbox("📚 Select Subject (10th Class)", subjects)

st.write(f"Selected Subject: **{subject}**")

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.selectbox(
    "Menu",
    ["⏱️ Study Timer", "📝 Tasks", "❓ Quiz"]
)

# ---------------- STUDY TIMER ----------------
if menu == "⏱️ Study Timer":

    st.header("Study Timer")

    study_time = st.number_input("Study Time (minutes)", min_value=1, value=1)
    break_time = st.number_input("Break Time (minutes)", min_value=1, value=1)

    if st.button("Start Timer"):

        st.info("Study session started...")

        # Study countdown
        seconds = study_time * 60
        placeholder = st.empty()

        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            placeholder.markdown(f"### 🧠 Study Time: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1

        st.success("🎉 Study time completed! Take a break.")

        # Break countdown
        st.info("Break started...")

        seconds = break_time * 60
        placeholder2 = st.empty()

        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            placeholder2.markdown(f"### ☕ Break Time: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1

        st.success("✅ Break finished!")

# ---------------- TASKS ----------------
elif menu == "📝 Tasks":

    st.header("Study Tasks")

    task = st.text_input("Enter topic / task")

    if st.button("Add Task"):
        if task:
            st.session_state.tasks.append({"task": task, "done": False})

    # Display tasks
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(t["task"])

        with col2:
            if st.button("Done", key=i):
                st.session_state.tasks[i]["done"] = True

    st.subheader("Completed Topics ✅")

    for t in st.session_state.tasks:
        if t["done"]:
            st.write("✔", t["task"])

# ---------------- QUIZ ----------------
elif menu == "❓ Quiz":

    st.header("Quiz Section")

    questions = {
        "Maths": [
            ("2 + 2 = ?", ["3", "4", "5"], "4"),
            ("5 * 3 = ?", ["10", "15", "20"], "15")
        ],
        "Physics": [
            ("Unit of force?", ["Newton", "Joule", "Watt"], "Newton")
        ],
        "Chemistry": [
            ("H2O is?", ["Water", "Oxygen", "Hydrogen"], "Water")
        ],
        "Biology": [
            ("Basic unit of life?", ["Cell", "Atom", "Tissue"], "Cell")
        ],
        "Social": [
            ("Capital of India?", ["Delhi", "Mumbai", "Chennai"], "Delhi")
        ],
        "English": [
            ("Synonym of 'Big'?", ["Large", "Small", "Tiny"], "Large")
        ]
    }

    if subject in questions:

        q_list = questions[subject]
        score = 0

        for i, (q, options, correct) in enumerate(q_list):

            st.write(f"Q{i+1}: {q}")
            answer = st.radio("Choose:", options, key=f"q{i}")

            if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
                if answer == correct:
                    st.success("Correct ✅")
                    score += 1
                else:
                    st.error("Wrong ❌")

        if st.button("Show Final Score"):
            st.info(f"Your Score: {score}/{len(q_list)}")

    else:
        st.warning("No quiz available for this subject.")
