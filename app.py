import streamlit as st
from data.careers import CAREERS
from utils.analyzer import analyze_skills, get_recommendations

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🧠 AI Career Mentor")

st.markdown("""
Welcome to **AI Career Mentor**.

This application analyzes your current skills and generates a personalized learning roadmap to help you achieve your dream career in technology.

Fill in the details below and click **Generate Roadmap**.
""")

st.divider()

# -----------------------------
# User Information
# -----------------------------
name = st.text_input("👤 Enter Your Name")

career = st.selectbox(
    "🎯 Select Your Career Goal",
    list(CAREERS.keys())
)

experience = st.select_slider(
    "📈 Experience Level",
    options=[
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

skills = st.text_area(
    "💻 Enter Your Current Skills (comma separated)",
    placeholder="Example: Python, Git, HTML, CSS"
)

st.divider()

generate = st.button(
    "🚀 Generate Roadmap",
    use_container_width=True
)

# -----------------------------
# Analysis
# -----------------------------
if generate:

    if name == "":
        st.error("Please enter your name.")

    elif skills == "":
        st.error("Please enter your skills.")

    else:

        st.success("Analysis started successfully!")

        user_skills = skills.split(",")

        matched, missing, score = analyze_skills(user_skills, career)
        projects, courses, learning_time = get_recommendations(career)

        # -----------------------------
        # Career Analysis
        # -----------------------------
        st.subheader("📊 Career Analysis")

        st.metric("Career Score", f"{score}%")

        st.progress(score / 100)

        if score >= 80:
            level = "🟢 Career Ready"

        elif score >= 60:
            level = "🟡 Intermediate"

        elif score >= 40:
            level = "🟠 Beginner"

        else:
            level = "🔴 Just Starting"

        st.info(f"Career Readiness: {level}")

        st.write("---")

        # -----------------------------
        # Skills You Have
        # -----------------------------
        st.subheader("✅ Skills You Already Have")

        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.warning("No matching skills found.")

        st.write("---")

        # -----------------------------
        # Missing Skills
        # -----------------------------
        st.subheader("❌ Skills You Should Learn")

        for skill in missing:
            st.error(skill)

        st.write("---")

        # -----------------------------
        # Recommended Projects
        # -----------------------------
        st.subheader("🚀 Recommended Projects")

        for project in projects:
            st.write(f"✅ {project}")

        st.write("---")

        # -----------------------------
        # Recommended Courses
        # -----------------------------
        st.subheader("📚 Recommended Courses")

        for course in courses:
            st.write(f"📖 {course}")

        st.write("---")

        # -----------------------------
        # Learning Time
        # -----------------------------
        st.subheader("⏳ Estimated Learning Time")

        st.success(learning_time)