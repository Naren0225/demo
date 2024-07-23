import streamlit as st
from st_pages import Page, show_pages

# Header with background image
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Show pages in the sidebar
show_pages([
    Page("pages/home.py", "Home", "🏠"),
    Page("pages/path.py", "Pathology", "⚕️"),
    Page("pages/xray.py", "X-Ray", "🩻"),
    Page("pages/about.py", "About", "ℹ️")
])

# Sidebar with Image (GIF)
st.sidebar.image("https://i.imgur.com/xbwZCPR.gif", use_column_width=True)
# st.sidebar.image("scan.png", use_column_width=True)

st.snow()
st.title("Welcome To Scantec!")
st.write("This is a web app for medical image analysis.")
st.write("It is developed by Scantec, a team of students from the Christ university")
st.subheader("Watch our Introduction Video")
video_url = "https://www.youtube.com/watch?v=your_video_id"  # Replace with your video URL
st.video(video_url)

