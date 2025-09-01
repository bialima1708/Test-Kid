import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="Child Test Example", layout="centered")

# --- Questions and options ---
questions = [
    {
        "question": "How often does the child feel anxious?",
        "options": ["Never", "Sometimes", "Often"]
    },
    {
        "question": "How easily does the child make friends?",
        "options": ["Easily", "With difficulty", "Not at all"]
    },
    {
        "question": "Does the child enjoy group activities?",
        "options": ["Yes", "Sometimes", "No"]
    }
]

# --- Session state for answers ---
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(questions)
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# --- Display current question ---
q_idx = st.session_state.current_question
q = questions[q_idx]

st.progress((q_idx + 1) / len(questions))  # progress bar
st.write(f"**Question {q_idx + 1}:** {q['question']}")

# Radio buttons for answers
st.session_state.answers[q_idx] = st.radio(
    "Select an answer:", q["options"], key=q_idx
)

# --- Navigation buttons ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Back") and st.session_state.current_question > 0:
        st.session_state.current_question -= 1

with col2:
    if st.button("Next") and st.session_state.answers[q_idx] is not None:
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
        else:
            st.session_state.show_results = True

# --- Results page ---
if st.session_state.get("show_results", False):
    st.write("## ✅ Test Completed!")
    st.write("### Your Answers:")
    for i, ans in enumerate(st.session_state.answers):
        st.write(f"Q{i+1}: {ans}")

