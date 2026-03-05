import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
from PIL import Image
import base64

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="SMNG Data Portal | VIGO SAT-1",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to convert image to base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0f1e 0%, #1a1f35 100%);
    }
    
    /* Main container */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(34, 197, 94, 0.1) 100%);
        border-radius: 2rem;
        padding: 3rem 2rem;
        margin-bottom: 3rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .main-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #8b5cf6 50%, #22c55e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        text-align: center;
        font-size: 1.875rem;
        color: #8b5cf6;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .launch-badge {
        text-align: center;
        font-size: 1.25rem;
        color: #22c55e;
        background: rgba(34, 197, 94, 0.1);
        padding: 0.75rem 2rem;
        border-radius: 100px;
        display: inline-block;
        margin: 0 auto;
        border: 1px solid rgba(34, 197, 94, 0.3);
    }
    
    /* Stats Cards */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 1.5rem;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        border-color: rgba(139, 92, 246, 0.3);
    }
    
    .stat-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .stat-label {
        font-size: 1.25rem;
        color: #94a3b8;
        font-weight: 500;
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-top: 0.5rem;
    }
    
    /* Section Titles */
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 4rem 0 2rem;
        background: linear-gradient(135deg, #fff 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .section-title::after {
        content: '';
        display: block;
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #8b5cf6, #22c55e);
        margin: 1rem auto;
        border-radius: 2px;
    }
    
    /* Description Cards */
    .description-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 1.5rem;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.05);
        max-width: 900px;
        margin: 2rem auto;
    }
    
    .description-text {
        font-size: 1.125rem;
        line-height: 1.8;
        color: #cbd5e1;
        text-align: center;
    }
    
    /* PERFECT ROUND LOGO STYLING */
    .logo-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }
    
    .round-logo-frame {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        background: linear-gradient(135deg, #8b5cf6, #22c55e);
        padding: 5px;
        margin: 0 auto 1rem auto;
        box-shadow: 0 20px 40px -10px rgba(139, 92, 246, 0.5);
        transition: transform 0.3s ease;
    }
    
    .round-logo-frame:hover {
        transform: scale(1.05);
    }
    
    .round-logo-content {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: white;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    
    .round-logo-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }
    
    .logo-placeholder {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(135deg, #8b5cf6, #22c55e);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2.5rem;
        font-weight: 800;
    }
    
    .inspiration-text {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #8b5cf6, #22c55e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 1rem 0;
        letter-spacing: 1px;
    }
    
    /* About section with box content */
    .about-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 2rem;
        padding: 2.5rem;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-top: 2rem;
    }
    
    .about-text-box {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 1rem;
        padding: 1.5rem;
        border: 1px solid rgba(139, 92, 246, 0.2);
        margin-bottom: 1.5rem;
    }
    
    .about-text {
        color: #e2e8f0;
        line-height: 1.8;
        font-size: 1.1rem;
        margin: 0;
    }
    
    .about-text strong {
        color: #8b5cf6;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-top: 1.5rem;
    }
    
    .feature-item {
        background: rgba(139, 92, 246, 0.1);
        padding: 0.75rem 1rem;
        border-radius: 0.75rem;
        color: #e2e8f0;
        border: 1px solid rgba(139, 92, 246, 0.2);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .feature-item:hover {
        background: rgba(139, 92, 246, 0.2);
        transform: translateY(-2px);
    }
    
    .academy-name {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #8b5cf6, #22c55e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 2rem 0;
    }
    
    /* School badge */
    .school-badge {
        background: linear-gradient(135deg, #f59e0b, #f97316);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 100px;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
        margin: 0.5rem 0;
    }
    
    /* Chart container */
    .chart-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 1.5rem;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin: 2rem 0;
    }
    
    /* Custom divider */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #8b5cf6, #22c55e, transparent);
        margin: 3rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# MAIN CONTAINER
# -------------------------------------------------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------

st.markdown("""
<div class="hero-section">
    <div class="main-title">SMNG DATA PORTAL</div>
    <div class="sub-title">VIGO SAT-1 Achievement</div>
    <div style="text-align: center;">
        <span class="launch-badge">🚀 Successfully Launched – Feb 13, 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HISTORIC ACHIEVEMENT SECTION
# -------------------------------------------------

st.markdown("<div class='section-title'>🏆 Historic Achievement</div>", unsafe_allow_html=True)

st.markdown("""
<div class="description-card">
    <div class="description-text">
        <span class="school-badge">🏫 Government Ariyakudi School Student</span>
        <br><br>
        Students from rural backgrounds, including <span style="color: #f97316; font-weight: 700;">Government Ariyakudi School students</span>, 
        completed advanced satellite technology training at 
        <span style="color: #8b5cf6; font-weight: 600;">SMNG Academy</span> and contributed to the 
        <span style="color: #22c55e; font-weight: 600;">VIGO SAT-1 student satellite initiative.</span>
        <br><br>
        This milestone highlights innovation, STEM education, and scientific empowerment
        among young students across Tamil Nadu.
    </div>
</div>
""", unsafe_allow_html=True)

# Stats cards
st.markdown("""
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-icon">🛰️</div>
        <div class="stat-label">Satellite Built</div>
        <div class="stat-value">VIGO SAT-1</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">🎓</div>
        <div class="stat-label">Students Trained</div>
        <div class="stat-value">10+</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">🏅</div>
        <div class="stat-label">National Recognition</div>
        <div class="stat-value">ISRO Accolade</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Custom divider
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# -------------------------------------------------
# DATA VISUALIZATION SECTION
# -------------------------------------------------

st.markdown("<div class='section-title'>📊 Visualize Satellite Data</div>", unsafe_allow_html=True)

file1_path = "data/file1.csv"
file2_path = "data/file2.csv"

if os.path.exists(file1_path) and os.path.exists(file2_path):

    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    st.markdown('<p style="text-align: center; color: #94a3b8; margin-bottom: 2rem;">Satellite telemetry datasets from SMNG research projects.</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    numeric_cols1 = df1.select_dtypes(include=np.number).columns.tolist()
    numeric_cols2 = df2.select_dtypes(include=np.number).columns.tolist()

    if numeric_cols1 and numeric_cols2:
        col1, col2, col3 = st.columns(3)

        with col1:
            col1_selected = st.selectbox("📡 File 1 Column", numeric_cols1)
        with col2:
            col2_selected = st.selectbox("🛸 File 2 Column", numeric_cols2)
        with col3:
            chart_type = st.selectbox(
                "📈 Chart Type",
                ["Line Chart", "Bar Chart", "Scatter Plot"]
            )

        if chart_type == "Line Chart":
            fig = px.line(df1, y=col1_selected, title=f"{col1_selected} vs {col2_selected}")
            fig.add_scatter(y=df2[col2_selected], mode="lines", name="File 2")
        elif chart_type == "Bar Chart":
            fig = px.bar(df1, y=col1_selected, title=f"{col1_selected} vs {col2_selected}")
            fig.add_bar(y=df2[col2_selected], name="File 2")
        else:
            fig = px.scatter(df1, y=col1_selected, title=f"{col1_selected} vs {col2_selected}")
            fig.add_scatter(y=df2[col2_selected], mode="markers", name="File 2")

        fig.update_layout(
            template="plotly_dark",
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', family="Inter")
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No numeric columns found in the CSV files.")
        
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align: center; padding: 3rem; background: rgba(245, 158, 11, 0.05); border-radius: 1rem;">
        <span style="font-size: 3rem;">📁</span>
        <h3 style="color: #f59e0b; margin-top: 1rem;">Data Files Not Found</h3>
        <p style="color: #94a3b8;">Please place file1.csv and file2.csv inside the data folder</p>
    </div>
    """, unsafe_allow_html=True)

# Custom divider
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# -------------------------------------------------
# ABOUT SMNG SECTION
# -------------------------------------------------

st.markdown("<div class='section-title'>About SMNG Academy</div>", unsafe_allow_html=True)

st.markdown('<div class="about-container">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="logo-section">', unsafe_allow_html=True)
    
    logo_path = "images/smng_logo.png"
    img_base64 = get_image_base64(logo_path) if os.path.exists(logo_path) else None
    
    if img_base64:
        st.markdown(f"""
        <div class="round-logo-frame">
            <div class="round-logo-content">
                <img src="data:image/png;base64,{img_base64}" class="round-logo-img" alt="SMNG Logo">
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="round-logo-frame">
            <div class="round-logo-content">
                <div class="logo-placeholder">SMNG</div>
            </div>
        </div>
        <p style="color: #64748b; font-size: 0.8rem; text-align: center;">Place logo at: images/smng_logo.png</p>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='inspiration-text'>✨ Inspiration of kids ✨</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-text-box">
        <p class="about-text"><strong>SMNG Academy</strong> (Scientist Makes Next Generation) is a technology innovation academy focused on STEM education, robotics, artificial intelligence and satellite development.</p>
    </div>
    
    <div class="about-text-box">
        <p class="about-text">The academy empowers rural students with hands-on engineering experience, real-world scientific projects and aerospace technology training.</p>
    </div>
    
    <h4 style="color: white; font-weight: 600; margin: 1.5rem 0 1rem;">Key Focus Areas:</h4>
    <div class="features-grid">
        <div class="feature-item">Robotics and Embedded Systems</div>
        <div class="feature-item">Artificial Intelligence</div>
        <div class="feature-item">Satellite Technology</div>
        <div class="feature-item">IoT Engineering</div>
        <div class="feature-item">Rural Innovation</div>
        <div class="feature-item">STEM Education</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='academy-name'>SMNG ACADEMY</div>", unsafe_allow_html=True)

# -------------------------------------------------
# SIMPLE FOOTER - USING STREAMLIT COMPONENTS ONLY
# -------------------------------------------------

st.markdown("---")
st.markdown("## SMNG Academy")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<p style="color:#ffffff; font-size:18px; font-weight:bold;">📞 +91 73588 12100</p>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<p style="color:#ffffff; font-size:18px; font-weight:bold;">✉️ smngscademyiok@gmail.com</p>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<p style="color:#ffffff; font-size:18px; font-weight:bold;">📍 Karaikudi, Tamil Nadu</p>',
        unsafe_allow_html=True
    )

st.markdown(
    '<p style="background: linear-gradient(135deg, #8b5cf6, #22c55e); padding: 1rem; border-radius: 10px; color: white; font-weight: 500; text-align: center;">Empowering Rural Innovation</p>',
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    '<p style="color: #94a3b8; font-size: 1.1rem; text-align: center;">© 2026 SMNG Academy. All rights reserved.<br>Designed with ❤️ for the scientific community</p>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)





















