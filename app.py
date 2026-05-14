import streamlit as st
import random
import pandas as pd

st.set_page_config(
    page_title="Career Depth, Vision High",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Trebuchet MS', sans-serif;
    background-color: #f5f9ff;
}

.main-title {
    font-size: 58px;
    font-weight: 900;
    color: #ffb400;
    text-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    letter-spacing: 2px;
}

.sub-title {
    font-size: 22px;
    color: #003366;
    font-style: italic;
    font-weight: bold;
}

.course-card {
    background: linear-gradient(to bottom right, #ffffff, #eaf4ff);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
    border: 2px solid #d6e7ff;
    text-align: center;
}

.course-title {
    color: #002855;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 15px;
}

.fee-style {
    color: green;
    font-size: 20px;
    font-weight: bold;
}

footer {
    text-align: center;
    font-size: 18px;
    color: #555;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER SECTION
# ---------------------------------------------------
col1, col2 = st.columns([1,5])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4207/4207247.png",
        width=140
    )

with col2:
    st.markdown(
        '<div class="main-title">Career Depth, Vision High</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">Empowering Future Leaders Through Excellence & Innovation</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------------------------------------------
# COURSE DATA
# ---------------------------------------------------
courses = {
    "B.C.A": {
        "duration": "3 Years",
        "fees": "₹75,000 / Year",
        "description": "Bachelor of Computer Applications focuses on programming, cloud computing, and software development."
    },

    "B.B.M": {
        "duration": "3 Years",
        "fees": "₹68,000 / Year",
        "description": "Bachelor of Business Management develops leadership and entrepreneurship skills."
    },

    "B.Com": {
        "duration": "3 Years",
        "fees": "₹60,000 / Year",
        "description": "Bachelor of Commerce includes finance, taxation, accounting, and banking concepts."
    },

    "B.A": {
        "duration": "3 Years",
        "fees": "₹45,000 / Year",
        "description": "Bachelor of Arts covers communication, literature, psychology, and social sciences."
    },

    "M.C.A": {
        "duration": "2 Years",
        "fees": "₹95,000 / Year",
        "description": "Master of Computer Applications offers advanced software engineering knowledge."
    },

    "M.B.A": {
        "duration": "2 Years",
        "fees": "₹1,20,000 / Year",
        "description": "Master of Business Administration focuses on marketing, HR, finance, and leadership."
    },

    "M.Com": {
        "duration": "2 Years",
        "fees": "₹82,000 / Year",
        "description": "Master of Commerce specializes in economics and commerce research."
    },

    "M.A": {
        "duration": "2 Years",
        "fees": "₹70,000 / Year",
        "description": "Master of Arts provides expertise in humanities and media studies."
    }
}

# ---------------------------------------------------
# COURSE SHOWCASE
# ---------------------------------------------------
st.header("🎓 Courses Offered")

course_names = list(courses.keys())
cols = st.columns(4)

for index, course in enumerate(course_names):

    with cols[index % 4]:

        st.markdown('<div class="course-card">', unsafe_allow_html=True)

        st.markdown(
            f'<div class="course-title">{course}</div>',
            unsafe_allow_html=True
        )

        if st.button(f"View Details - {course}", key=course):
            st.session_state["selected_course"] = course

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# COURSE DETAILS
# ---------------------------------------------------
if "selected_course" in st.session_state:

    selected = st.session_state["selected_course"]
    details = courses[selected]

    st.markdown("---")
    st.subheader(f"📘 {selected} Course Details")

    st.write(f"### ⏳ Duration: {details['duration']}")
    st.write(details["description"])

    st.markdown(
        f'<div class="fee-style">💰 Fees: {details["fees"]}</div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# REGISTRATION FORM
# ---------------------------------------------------
st.markdown("---")
st.header("📝 Student Registration")

with st.form("registration_form"):

    student_name = st.text_input("Student Full Name")
    student_email = st.text_input("Email Address")
    student_phone = st.text_input("Phone Number")
    student_course = st.selectbox("Select Course", course_names)
    student_address = st.text_area("Address")

    submit = st.form_submit_button("Register Now")

    if submit:

        registration_id = f"CDVH{random.randint(10000,99999)}"

        st.success("✅ Registration Successful")

        st.write(f"## Registration ID: {registration_id}")

        data = {
            "Registration ID": [registration_id],
            "Student Name": [student_name],
            "Email": [student_email],
            "Phone": [student_phone],
            "Course": [student_course],
            "Address": [student_address]
        }

        df = pd.DataFrame(data)

        st.subheader("📄 Registered Student Details")
        st.dataframe(df)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown(
    """
    <footer>
    <b>Career Depth, Vision High</b><br>
    Excellence • Innovation • Leadership
    </footer>
    """,
    unsafe_allow_html=True
)
