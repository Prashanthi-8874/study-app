import streamlit as st
import time

st.set_page_config(page_title="Student Study App", layout="centered")

st.title("📘 Charan's Study & Quiz App")

# SESSION STATE
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# SUBJECTS
subjects = ["Maths", "Physics", "Chemistry", "Biology", "Social", "English"]
subject = st.selectbox("📚 Select Subject (10th Class)", subjects)

st.write(f"Selected Subject: **{subject}**")

# SIDEBAR MENU
menu = st.sidebar.selectbox("Menu", ["⏱️ Study Timer", "📝 Tasks", "❓ Quiz"])

# TIMER
if menu == "⏱️ Study Timer":
    st.header("Study Timer")

    study_time = st.number_input("Study Time (minutes)", 1, 60, 1)
    break_time = st.number_input("Break Time (minutes)", 1, 30, 1)

    if st.button("Start Timer"):
        st.info("Study session started...")

        seconds = study_time * 60
        placeholder = st.empty()

        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            placeholder.markdown(f"### 🧠 Study Time: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1

        st.success("🎉 Study completed!")

# TASKS
elif menu == "📝 Tasks":
    st.header("Study Tasks")

    task = st.text_input("Enter topic")

    if st.button("Add Task"):
        if task:
            st.session_state.tasks.append({"task": task, "done": False})

    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([3,1])

        with col1:
            st.write(t["task"])

        with col2:
            if st.button("Done", key=i):
                st.session_state.tasks[i]["done"] = True

    st.subheader("Completed Topics")
    for t in st.session_state.tasks:
        if t["done"]:
            st.write("✔", t["task"])

# QUIZ
elif menu == "❓ Quiz":
    st.header("Quiz Section")

    questions = {
        "Maths": [("2+2=?", ["3","4","5"], "4")],
        "Physics": [("Unit of force?", ["Newton","Joule"], "Newton")]
    }

    if subject in questions:
        score = 0
        q_list = questions[subject]

        for i, (q, options, correct) in enumerate(q_list):
            st.write(q)
            ans = st.radio("Choose", options, key=i)

            if st.button("Submit", key=f"b{i}"):
                if ans == correct:
                    st.success("Correct")
                    score += 1
                else:
                    st.error("Wrong")

        if st.button("Final Score"):
            st.info(f"Score: {score}/{len(q_list)}")
