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

.premium-course-box {
    background: linear-gradient(to right, #ffffff, #f0f6ff);
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 20px;
    border: 2px solid #d6e4ff;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);
    text-align: center;
    transition: 0.3s;
}

.selected-course-box {
    background: linear-gradient(to right, #ffe0b3, #ffcc80);
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 20px;
    border: 3px solid #ff8800;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.18);
    text-align: center;
    transition: 0.3s;
}

.premium-course-title {
    font-size: 30px;
    font-weight: 900;
    color: #ff6600;
    letter-spacing: 1px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.15);
}

.course-button button {
    width: 100%;
    height: 120px;
    background-color: transparent;
    border: none;
    margin-top: -120px;
    opacity: 0;
    cursor: pointer;
}

footer {
    text-align: center;
    font-size: 18px;
    color: #ffb400;
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
        "full_name": "Bachelor of Computer Applications",
        "fees": "₹75,000 / Year",
        "semesters": 6,
        "subjects": {
            "Semester 1": ["Programming in C", "Mathematics", "Digital Fundamentals"],
            "Semester 2": ["Data Structures", "Python", "Operating Systems"],
            "Semester 3": ["Java Programming", "Database Management", "Computer Networks"],
            "Semester 4": ["Web Development", "Software Engineering", "Cloud Computing"],
            "Semester 5": ["Artificial Intelligence", "Machine Learning", "Cyber Security"],
            "Semester 6": ["Project Work", "Mobile Applications", "Data Analytics"]
        }
    },

    "B.B.M": {
        "full_name": "Bachelor of Business Management",
        "fees": "₹68,000 / Year",
        "semesters": 6,
        "subjects": {
            "Semester 1": ["Business Basics", "Accounting", "Economics"],
            "Semester 2": ["Marketing", "Business Law", "Human Resource"],
            "Semester 3": ["Finance", "Entrepreneurship", "Statistics"],
            "Semester 4": ["Management Principles", "Operations", "Taxation"],
            "Semester 5": ["Leadership", "Digital Marketing", "Business Analytics"],
            "Semester 6": ["Project", "Strategic Management", "International Business"]
        }
    },

    "B.Com": {
        "full_name": "Bachelor of Commerce",
        "fees": "₹60,000 / Year",
        "semesters": 6,
        "subjects": {
            "Semester 1": ["Financial Accounting", "Economics", "Business Studies"],
            "Semester 2": ["Corporate Accounting", "Banking", "Business Law"],
            "Semester 3": ["Taxation", "Auditing", "Cost Accounting"],
            "Semester 4": ["Management Accounting", "Statistics", "Finance"],
            "Semester 5": ["GST", "Investment Management", "Entrepreneurship"],
            "Semester 6": ["Project", "International Finance", "Research Methodology"]
        }
    },

    "B.A": {
        "full_name": "Bachelor of Arts",
        "fees": "₹45,000 / Year",
        "semesters": 6,
        "subjects": {
            "Semester 1": ["English", "History", "Political Science"],
            "Semester 2": ["Psychology", "Sociology", "Economics"],
            "Semester 3": ["Journalism", "Public Administration", "Literature"],
            "Semester 4": ["Communication Skills", "Philosophy", "Geography"],
            "Semester 5": ["Media Studies", "Creative Writing", "Human Rights"],
            "Semester 6": ["Project", "Modern History", "Social Research"]
        }
    },

    "M.C.A": {
        "full_name": "Master of Computer Applications",
        "fees": "₹95,000 / Year",
        "semesters": 4,
        "subjects": {
            "Semester 1": ["Advanced Programming", "Data Structures", "Mathematics"],
            "Semester 2": ["Cloud Computing", "AI", "Database Systems"],
            "Semester 3": ["Machine Learning", "Cyber Security", "Big Data"],
            "Semester 4": ["Project Work", "Research", "Software Architecture"]
        }
    },

    "M.B.A": {
        "full_name": "Master of Business Administration",
        "fees": "₹1,20,000 / Year",
        "semesters": 4,
        "subjects": {
            "Semester 1": ["Management", "Accounting", "Economics"],
            "Semester 2": ["Marketing", "HR", "Finance"],
            "Semester 3": ["Business Analytics", "Leadership", "Operations"],
            "Semester 4": ["Project", "Strategic Management", "International Business"]
        }
    },

    "M.Com": {
        "full_name": "Master of Commerce",
        "fees": "₹82,000 / Year",
        "semesters": 4,
        "subjects": {
            "Semester 1": ["Advanced Accounting", "Economics", "Finance"],
            "Semester 2": ["Taxation", "Research Methods", "Banking"],
            "Semester 3": ["Investment Analysis", "Corporate Law", "Auditing"],
            "Semester 4": ["Project", "Financial Markets", "Business Ethics"]
        }
    },

    "M.A": {
        "full_name": "Master of Arts",
        "fees": "₹70,000 / Year",
        "semesters": 4,
        "subjects": {
            "Semester 1": ["Advanced Literature", "Sociology", "Psychology"],
            "Semester 2": ["Communication", "Philosophy", "Political Science"],
            "Semester 3": ["Media Studies", "Human Rights", "Research"],
            "Semester 4": ["Project", "Cultural Studies", "Creative Writing"]
        }
    }
}

# ---------------------------------------------------
# COLLEGE INFRASTRUCTURE SECTION
# ---------------------------------------------------
st.header("🏛️ College Infrastructure")

left_col, right_col = st.columns(2)

with left_col:

    st.markdown("""
    ### Campus Facilities

    - Smart Digital Classrooms
    - Advanced Computer Laboratories
    - High Speed Wi-Fi Campus
    - Modern Library
    - Placement & Training Center
    - Innovation Labs
    - Seminar Halls
    - Sports Facilities
    """)

with right_col:

    st.markdown("""
    ### Why Choose Our College?

    - Industry Oriented Curriculum
    - Experienced Faculty
    - Placement Assistance
    - Career Development Programs
    - Internship Opportunities
    - Practical Learning Environment
    - Student Friendly Campus
    """)

# ---------------------------------------------------
# PREMIUM COURSES SECTION
# ---------------------------------------------------
st.markdown("---")

st.header("🎓 Courses Offered")

course_names = list(courses.keys())

if "selected_course" not in st.session_state:
    st.session_state["selected_course"] = course_names[0]

# ---------------------------------------------------
# QUERY PARAMS FOR CLICKABLE COURSE BOXES
# ---------------------------------------------------
query_params = st.query_params

if "course" in query_params:

    selected_course = query_params["course"]

    if selected_course in courses:
        st.session_state["selected_course"] = selected_course

cols = st.columns(4)

for index, course in enumerate(course_names):

    with cols[index % 4]:

        selected = st.session_state["selected_course"] == course

        box_class = (
            "selected-course-box"
            if selected
            else "premium-course-box"
        )

        select_symbol = "✅ SELECTED" if selected else "👉 SELECT"

        st.markdown(
            f"""
            <a href='/?course={course}' target='_self'
            style='text-decoration:none;'>

                <div class="{box_class}">

                    <div class="premium-course-title">
                        {course}
                    </div>

                    <br>

                    <div style="
                        font-size:18px;
                        font-weight:bold;
                        color:#003366;
                        background-color:white;
                        padding:10px;
                        border-radius:10px;
                        display:inline-block;
                        box-shadow:0px 2px 6px rgba(0,0,0,0.15);
                    ">
                        {select_symbol}
                    </div>

                </div>

            </a>
            """,
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# COURSE DETAILS
# ---------------------------------------------------
selected = st.session_state["selected_course"]
details = courses[selected]

st.markdown("---")

st.subheader(f"📘 {selected} Course Details")

st.write(f"### Full Course Name: {details['full_name']}")
st.write(f"### 💰 Fees Structure: {details['fees']}")
st.write(f"### 📚 Number of Semesters: {details['semesters']}")

st.markdown("## Semester Wise Subjects")

for semester, subjects in details["subjects"].items():

    st.write(f"### {semester}")

    for subject in subjects:
        st.write(f"• {subject}")

# ---------------------------------------------------
# REGISTRATION + AI BOT SECTION
# ---------------------------------------------------
st.markdown("---")

left_col, right_col = st.columns(2)

# ---------------------------------------------------
# STUDENT REGISTRATION
# ---------------------------------------------------
with left_col:

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
# AI BOT SECTION
# ---------------------------------------------------
with right_col:

    st.header("🤖 AI Bot Assistant")

    user_question = st.text_input("Ask Your Question")

    if user_question:

        question = user_question.lower()

        if "fees" in question:
            response = "Course fees range between ₹45,000 and ₹1,20,000 per year."

        elif "admission" in question:
            response = "Admissions are currently open for all courses."

        elif "placement" in question:
            response = "Placement support is available for IT, Banking, HR and Marketing sectors."

        elif "bca" in question:
            response = "BCA focuses on Programming, AI, Web Development and Software Engineering."

        elif "mba" in question:
            response = "MBA develops Leadership, Marketing and Business Management skills."

        else:
            response = "Our college provides quality education, career development and placement assistance."

        st.success(response)

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
