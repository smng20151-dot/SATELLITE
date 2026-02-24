import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="SMNG Academy Portal", layout="wide")

# --------------------------------------------------
# GLOBAL STYLE + GOOGLE FONTS
# --------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #f2f4f8;
}

.navbar {
    background: linear-gradient(90deg, #141E30, #243B55);
    padding: 15px 40px;
    border-radius: 12px;
    color: white;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 22px;
}

.hero {
    background: linear-gradient(120deg, #667eea, #764ba2);
    padding: 90px 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}

.section {
    background: white;
    padding: 40px;
    border-radius: 18px;
    margin-top: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

.footer-main {
    margin-top: 60px;
    padding: 60px 40px;
    background: linear-gradient(90deg, #141E30, #243B55);
    color: white;
    border-radius: 20px;
}

.footer-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 20px;
    margin-bottom: 15px;
}

.footer-text {
    font-size: 15px;
    line-height: 1.7;
    color: #dddddd;
}

.footer-bottom {
    text-align:center;
    margin-top:40px;
    padding-top:20px;
    border-top:1px solid rgba(255,255,255,0.2);
    font-size:14px;
    color:#bbbbbb;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------
st.markdown("<div class='navbar'>🚀 SMNG Academy | Satellite & Data Intelligence Portal</div>", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<div class='hero'>
    <h1 style="font-family:Montserrat;font-weight:800;">
    Advanced STEM & Satellite Innovation
    </h1>
    <p style="font-size:20px;">
    Empowering Ariyakudi Government School Students Through Aerospace & AI
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT SECTION
# --------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    if os.path.exists("images/smng_logo.png"):
        st.image("images/smng_logo.png", width=220)

with col2:
    st.markdown("""
## 🎓 About SMNG Academy

SMNG Academy is a future-driven STEM innovation institution focused on:

• Satellite Systems & CubeSat Development  
• Robotics & Embedded Technologies  
• Artificial Intelligence & Data Science  
• IoT & Smart Engineering  
• Advanced Visualization & Analytics  

### 🌍 Vision
To transform rural education into global scientific excellence.

### 🎯 Mission
Deliver real-world aerospace exposure and empower students
to build, analyze, and innovate through applied science.
""")

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# DATA VISUALIZATION DASHBOARD
# --------------------------------------------------
file1_path = "data/file1.csv"
file2_path = "data/file2.csv"

if os.path.exists(file1_path) and os.path.exists(file2_path):

    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    st.markdown("""
    <div style='margin-top:40px;padding:50px;
    background:linear-gradient(120deg,#0f2027,#203a43,#2c5364);
    border-radius:25px;color:white;'>
    <h2 style='font-family:Montserrat;font-weight:800;'>
    📊 Advanced Data Intelligence Dashboard
    </h2>
    </div>
    """, unsafe_allow_html=True)

    numeric_cols1 = df1.select_dtypes(include=np.number).columns
    numeric_cols2 = df2.select_dtypes(include=np.number).columns

    colA, colB, colC = st.columns(3)

    col1_selected = colA.selectbox("File 1 Column", numeric_cols1)
    col2_selected = colB.selectbox("File 2 Column", numeric_cols2)
    chart_type = colC.selectbox(
        "Chart Type",
        ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"]
    )

    if chart_type == "Line Chart":
        fig = px.line(df1, y=col1_selected)
        fig.add_scatter(y=df2[col2_selected], mode='lines', name="File 2")

    elif chart_type == "Bar Chart":
        fig = px.bar(df1, y=col1_selected)
        fig.add_bar(y=df2[col2_selected], name="File 2")

    elif chart_type == "Area Chart":
        fig = px.area(df1, y=col1_selected)
        fig.add_scatter(y=df2[col2_selected], mode='lines', name="File 2")

    else:
        fig = px.scatter(df1, y=col1_selected)
        fig.add_scatter(y=df2[col2_selected], mode='markers', name="File 2")

    fig.update_layout(
        template="plotly_dark",
        title="SMNG Comparative Data Analysis",
        font=dict(family="Montserrat", size=16),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📌 Statistical Insights")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("File 1 Mean", round(df1[col1_selected].mean(), 2))
    m2.metric("File 2 Mean", round(df2[col2_selected].mean(), 2))
    m3.metric("File 1 Max", round(df1[col1_selected].max(), 2))
    m4.metric("File 2 Max", round(df2[col2_selected].max(), 2))

else:
    st.warning("Place file1.csv and file2.csv inside data folder.")

# --------------------------------------------------
# ACHIEVEMENT SECTION
# --------------------------------------------------
st.markdown("""
<div style='margin-top:60px;padding:70px 50px;
background:linear-gradient(120deg,#1e3c72,#2a5298);
border-radius:25px;color:white;'>

<h2 style='font-family:Montserrat;font-weight:800;'>
🛰 Historic Achievement – Ariyakudi Government School × SMNG Academy
</h2>

<p style='font-size:18px;line-height:1.8;'>
Students from Ariyakudi Government School completed advanced satellite
technology training at SMNG Academy and contributed to a
student-led satellite development initiative.

This represents a major milestone in rural STEM empowerment
and scientific innovation.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
# --------------------------------------------------
# ULTRA MINIMAL STYLISH FOOTER
# --------------------------------------------------

# --------------------------------------------------
# ULTRA MINIMAL STYLISH FOOTER
# --------------------------------------------------

st.markdown("""
<style>
.footer-luxury {
    margin-top: 100px;
    padding: 40px 0;
    background: linear-gradient(90deg, #0f172a, #1e293b);
    text-align: center;
}

.footer-text {
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 1px;
    background: linear-gradient(90deg, #38bdf8, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.footer-sub {
    margin-top: 8px;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='footer-luxury'>
    <div class='footer-text'>
        SMNG Academy
    </div>
            <div class='footer-phone'>
        📞 73588 12100
    </div>
    <div class='footer-sub'>
        © 2026 All Rights Reserved 🚀
    </div>
</div>
""", unsafe_allow_html=True)