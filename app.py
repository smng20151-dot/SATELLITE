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
# GLOBAL STYLES
# --------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Navbar */
.navbar {
    background: linear-gradient(90deg, #141E30, #243B55);
    padding: 18px 40px;
    border-radius: 12px;
    color: white;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 22px;
}

/* Hero */
.hero {
    background: linear-gradient(120deg, #667eea, #764ba2);
    padding: 90px 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}

/* Section Card */
.section {
    background: white;
    padding: 40px;
    border-radius: 18px;
    margin-top: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* Achievement Section */
.achievement-section {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    padding: 60px 40px;
    border-radius: 25px;
    margin-top: 60px;
    color: white;
    text-align: center;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}

.highlight-text {
    margin-top: 20px;
    font-size: 18px;
    font-weight: 600;
    color: #ffd700;
}

.achievement-stats {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 40px;
    flex-wrap: wrap;
}

.stat-item {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    width: 200px;
    transition: 0.3s;
}

.stat-item:hover {
    transform: translateY(-8px);
    background: rgba(255,255,255,0.2);
}

.stat-icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.stat-label {
    font-size: 16px;
    font-weight: 600;
}

/* Footer */
.footer {
    margin-top: 80px;
    padding: 60px 40px;
    background: linear-gradient(90deg, #141E30, #243B55);
    color: white;
    border-radius: 20px;
    text-align: center;
}

.footer-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 20px;
    margin-bottom: 15px;
}

.footer-links {
    margin-top: 20px;
    font-size: 14px;
    color: #bbbbbb;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------
st.markdown("<div class='navbar'>🚀 SMNG Academy | Satellite & Data Intelligence Portal</div>", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
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
        st.markdown("""
<style>
/* Remove white container background */
.section {
    background-color: transparent !important;
    padding: 0px !important;
    margin-bottom: -20px !important;
}

/* Remove default block spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 0rem;
}

/* Make logo centered vertically */
.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
## 🎓 About SMNG Academy

SMNG Academy focuses on:

• Satellite & CubeSat Development  
• Robotics & Embedded Systems  
• Artificial Intelligence & Data Science  
• IoT Engineering  
• Advanced Analytics  

### 🌍 Vision
Transform rural education into global scientific excellence.

### 🎯 Mission
Empower students through real-world aerospace exposure.
""")

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
file1_path = "data/file1.csv"
file2_path = "data/file2.csv"

if os.path.exists(file1_path) and os.path.exists(file2_path):

    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    st.markdown("## 📊 Advanced Data Intelligence Dashboard")

    numeric_cols1 = df1.select_dtypes(include=np.number).columns
    numeric_cols2 = df2.select_dtypes(include=np.number).columns

    colA, colB, colC = st.columns(3)

    col1_selected = colA.selectbox("File 1 Column", numeric_cols1)
    col2_selected = colB.selectbox("File 2 Column", numeric_cols2)
    chart_type = colC.selectbox("Chart Type", 
                                ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"])

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

    fig.update_layout(template="plotly_dark", height=500)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Place file1.csv and file2.csv inside data folder.")

# --------------------------------------------------
# ACHIEVEMENT
# --------------------------------------------------
st.markdown("""
<div class='achievement-section'>

<h2>🏆 Historic Achievement</h2>

<p style="max-width:800px;margin:auto;font-size:17px;">
Students from Ariyakudi Government School successfully completed 
advanced satellite technology training at SMNG Academy and contributed 
to a student-led satellite development initiative.
</p>

<div class='highlight-text'>
⭐ A major milestone in rural STEM empowerment and scientific innovation ⭐
</div>

<div class='achievement-stats'>

<div class='stat-item'>
<div class='stat-icon'>🛰️</div>
<div class='stat-label'>Satellite Built</div>
</div>

<div class='stat-item'>
<div class='stat-icon'>🎓</div>
<div class='stat-label'>10+ Students Trained</div>
</div>

<div class='stat-item'>
<div class='stat-icon'>🏅</div>
<div class='stat-label'>National Recognition</div>
</div>

</div>

</div>
""", unsafe_allow_html=True)
# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class='footer'>
    <div class='footer-title'>
        SMNG Academy
    </div>
    <div>
        📞 73588 12100 <br>
        📍 Karaikudi, Tamil Nadu
    </div>
    <div class='footer-links'>
        © 2026 All Rights Reserved | Empowering Rural Innovation
    </div>
</div>
""", unsafe_allow_html=True)