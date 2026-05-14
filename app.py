
import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Career Depth, Vision High", layout="wide")

# -----------------------------
# College Header
# -----------------------------
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #003366;
    }
    .sub-title {
        font-size: 18px;
        color: #444444;
    }
    .course-card {
        padding: 15px;
        border-radius: 12px;
        background-color: #f2f7ff;
        border: 1px solid #d9e6ff;
        margin-bottom: 15px;
    }
    .fee-text {
        color: green;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=100
    )

with col2:
    st.markdown('<div class="main-title">Career Depth, Vision High</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Empowering Students for a Bright Future</div>', unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# Course Data
# -----------------------------
courses = {
    "B.C.A": {
        "duration": "3 Years",
        "description": "Bachelor of Computer Applications focuses on software development, programming, and computer technologies.",
        "fees": "₹75,000 per year"
    },
    "B.B.M": {
        "duration": "3 Years",
        "description": "Bachelor of Business Management develops leadership, management, and entrepreneurship skills.",
        "fees": "₹65,000 per year"
    },
    "B.Com": {
        "duration": "3 Years",
        "description": "Bachelor of Commerce covers accounting, finance, taxation, and business studies.",
        "fees": "₹60,000 per year"
    },
    "B.A": {
        "duration": "3 Years",
        "description": "Bachelor of Arts includes humanities, social sciences, and communication studies.",
        "fees": "₹45,000 per year"
    },
    "M.C.A": {
        "duration": "2 Years",
        "description": "Master of Computer Applications provides advanced knowledge in software engineering and IT.",
        "fees": "₹95,000 per year"
    },
    "M.B.A": {
        "duration": "2 Years",
        "description": "Master of Business Administration focuses on business strategy, leadership, and marketing.",
        "fees": "₹1,20,000 per year"
    },
    "M.Com": {
        "duration": "2 Years",
        "description": "Master of Commerce specializes in finance, economics, and business management.",
        "fees": "₹80,000 per year"
    },
    "M.A": {
        "duration": "2 Years",
        "description": "Master of Arts provides advanced education in humanities and social sciences.",
        "fees": "₹70,000 per year"
    }
}

# -----------------------------
# Course Showcase
# -----------------------------
st.header("Courses Offered")

course_names = list(courses.keys())

cols = st.columns(4)

for i, course in enumerate(course_names):
    with cols[i % 4]:
        with st.container():
            st.markdown(f"""
                <div class="course-card">
                    <h3>{course}</h3>
                    <p>Click below to view details</p>
                </div>
            """, unsafe_allow_html=True)

            if st.button(f"View {course}", key=course):
                st.session_state["selected_course"] = course

# -----------------------------
# Course Details
# -----------------------------
if "selected_course" in st.session_state:
    selected = st.session_state["selected_course"]
    details = courses[selected]

    st.markdown("---")
    st.subheader(f"{selected} Course Details")

    st.write(f"**Duration:** {details['duration']}")
    st.write(f"**Course Description:** {details['description']}")
    st.markdown(f"<div class='fee-text'>Fees: {details['fees']}</div>", unsafe_allow_html=True)

# -----------------------------
# Registration Section
# -----------------------------
st.markdown("---")
st.header("Student Registration")

with st.form("registration_form"):
    student_name = st.text_input("Student Full Name")
    student_email = st.text_input("Email Address")
    student_phone = st.text_input("Phone Number")
    selected_course = st.selectbox("Select Course", course_names)
    student_address = st.text_area("Address")

    submitted = st.form_submit_button("Register Now")

    if submitted:
        registration_id = f"CDVH{random.randint(10000, 99999)}"

        st.success("Registration Successful!")
        st.write(f"### Registration ID: {registration_id}")

        registration_data = {
            "Registration ID": [registration_id],
            "Student Name": [student_name],
            "Email": [student_email],
            "Phone": [student_phone],
            "Course": [selected_course],
            "Address": [student_address]
        }

        df = pd.DataFrame(registration_data)

        st.subheader("Registered Student Details")
        st.dataframe(df)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<center><b>Career Depth, Vision High</b> © 2026 | All Rights Reserved</center>",
    unsafe_allow_html=True
)
