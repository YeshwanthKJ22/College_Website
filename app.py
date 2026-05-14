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

.semester-box {
    background-color: #eef5ff;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    border-left: 5px solid #003366;
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

    st.write(f"### Full Course Name: {details['full_name']}")
    st.write(f"### 💰 Fees Structure: {details['fees']}")
    st.write(f"### 📚 Number of Semesters: {details['semesters']}")

    st.markdown("## Semester Wise Subjects")

    for semester, subjects in details["subjects"].items():

        st.markdown('<div class="semester-box">', unsafe_allow_html=True)

        st.write(f"### {semester}")

        for subject in subjects:
            st.write(f"• {subject}")

        st.markdown('</div>', unsafe_allow_html=True)

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
