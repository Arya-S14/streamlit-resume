import streamlit as st
from streamlit_lottie import st_lottie
import json

# Load local JSON files
def load_lottie_file(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

# Load animations
coding_animation = load_lottie_file("animations/coding.json")
event_animation = load_lottie_file("animations/event.json")

# Set dark theme through Streamlit settings
st.set_page_config(page_title="Arya Sabale's Resume", page_icon="✨", layout="wide")
st.markdown(
    """
    <style>
   
    /* Add responsiveness to the app */
    body {
        width: 100%;
        margin: 0 auto;
    }
    /* Adjust font sizes for mobile devices */
    h1, h2, h3 {
        font-size: 1.5em;
    }
    /* Make images responsive */
    img {
        max-width: 100%;
        height: auto;
    }


    /* Title shadow */
    h1 {
        text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.6);
    }

    /* Make the background dark and text white */
    body {
        background-color: #2e2e2e;
        color: white;
    }

    /* Section title adjustments */
    h2, h3 {
        color: #fff;
    }

    /* Divider styling */
    .streamlit-expanderHeader {
        color: #fff;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Header section
st.title("Arya Sabale")
st.subheader("BTech in Computer Science and Engineering (AI & ML)")
st.divider()
st.markdown("<h2>🔷 <b>Contact Information</b></h2>", unsafe_allow_html=True)

st.markdown("""
- **Email:** aryaofficialaas14@gmail.com  
- **Location:** Maharashtra, India  
- **LinkedIn:** [Arya Sabale LinkedIn](https://www.linkedin.com/in/arya-sabale-171721250?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
- **GitHub:** [Arya Sabale GitHub](https://github.com/Aryu-S14)  
""")
st.divider()

# Summary section
st.markdown("<h2>🔷 <b>Summary</b></h2>", unsafe_allow_html=True)
st.write("A dedicated student with expertise in programming languages including Java, HTML, CSS, JavaScript, and Python. Passionate about technology and leadership fostering teamwork, and driving engagement.")
st.divider()

# Lottie animation for summary
if coding_animation:
    st_lottie(coding_animation, height=300, key="coding")
else:
    st.warning("Coding animation failed to load.")

# Experience section
st.markdown("<h2>🔷 <b>Experience</b></h2>", unsafe_allow_html=True)
st.markdown("### School Leader")
st.write("*Nirmala Convent School (06/2018 - 03/2019)*")
st.write("- Represented the student body as School Leader.")
st.write("- Led initiatives to improve discipline, leadership, and teamwork among students.")
st.divider()

# Education section
st.markdown("<h2>🔷 <b>Education</b></h2>", unsafe_allow_html=True)
st.markdown("""
- **SSC**: Nirmala Convent School (X  92.60% )  
- **HSC**: Maharaja Sayajirao Vidyalaya Junior College  (XII  85.17%)
- **Diploma in Computer Engineering**: Karmaveer Bhaurao Patil Polytechnic ( 92.40% ) 
- **Bachelor's in CSE (AI & ML)**: Bract's Vishwakarma Institute of Information Technology (2024-2027)  ( 9.21 CGPA )
""")
st.divider()

# Key Achievements section
st.markdown("<h2>🔷 <b>Key Achievements</b></h2>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
    - Currently Selected as ISP at Intershala .
    - Secured Rank in Different Intercollegiate Coding Competitions.  
    - Excelled in Different Intercollege Non-Tech Competitions(Presentation).  
    - Organized successful college events with high participant satisfaction.  
    - Secured Top Spot in My Academics.  
    """)
st.divider()

# Lottie animation for achievements
if event_animation:
    st_lottie(event_animation, height=300, key="event")
else:
    st.warning("Event animation failed to load.")

# Skills section
st.markdown("<h2>🔷 <b>Skills</b></h2>", unsafe_allow_html=True)
st.markdown("""
- **Languages**: Java, HTML, CSS, JavaScript, Python  
- **Leadership**: Team management, Event organization 
- **Database Management**: MySQL, MongoDB, or FireBase.
- **Design**: Proficiency in tools like Canva and Figma.
- **Teamwork**: Collaboration on group projects or events.             
""")
st.divider()

# Projects section
st.markdown("<h2>🔷 <b>Projects</b></h2>", unsafe_allow_html=True)
st.markdown("### Cafe Craft - Android Application")
st.write("- Developed an Android app for managing cafe orders, bookings, and events efficiently.")
st.markdown("### Vaccination - Android Application")
st.write("- Developed an Android app for Tracking Vaccination Schedule for babies")
st.markdown("### Movie Ticket Booking System-Java")
st.write("- Developed an system for managing movie ticket bookings.")

st.divider()

# Footer
st.write("~Arya")
