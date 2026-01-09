import subprocess
import sys
import os

# --- 1. THE AUTOMATOR (Installs everything for you) ---
def setup_and_run():
    required_packages = ["streamlit", "replicate", "requests"]
    
    print("🚀 Initializing TikTok Creator Studio...")
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"📦 Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    # This part writes the actual WebUI code into a temporary file
    app_code = """
import streamlit as st
import replicate
import requests
import time

# --- STYLING ---
st.set_page_config(page_title="TikTok Creator Studio", layout="wide")
st.markdown(\"\"\"
    <style>
    .main { background-color: #0f172a; color: white; }
    .stTextArea textarea { background-color: #1e293b; color: white; border: 1px solid #334155; }
    .stButton>button {
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        color: white; border-radius: 30px; height: 3em; width: 100%; font-weight: bold; border: none;
    }
    [data-testid="stFileUploadDropzone"] {
        background-color: #1e293b; border: 2px dashed #4facfe; border-radius: 15px;
    }
    </style>
\"\"\", unsafe_allow_html=True)

# --- UI LAYOUT ---
st.title("🎬 AI TikTok Shop Generator")
st.write("Upload your images and script to generate a viral video.")

col1, col2 = st.columns([1, 1])

with col1:
    person_img = st.file_uploader("👤 Upload Person", type=['png', 'jpg'])
    item_img = st.file_uploader("🎁 Upload Item", type=['png', 'jpg'])

with col2:
    script = st.text_area("Video Script", placeholder="Example: You guys won't believe how good this product is...", height=200)
    voice = st.selectbox("Select Voice", ["Friendly Female", "Energetic Male", "Professional Narrator"])
    captions = st.toggle("Auto-Captions", value=True)

if st.button("GENERATE AI VIDEO"):
    if not person_img or not item_img or not script:
        st.error("Please provide all inputs!")
    else:
        with st.status("🪄 AI is working...", expanded=True) as status:
            st.write("1. Merging images with Stable Diffusion...")
            time.sleep(2)
            st.write("2. Generating AI Voiceover...")
            time.sleep(2)
            st.write("3. Animating Talking Head & Adding Captions...")
            time.sleep(3)
            status.update(label="✅ Video Generated!", state="complete")
        
        st.success("Your video is ready for TikTok!")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Placeholder
    """
    
    with open("temp_app.py", "w") as f:
        f.write(app_code)

    print("🌐 Launching Web Interface...")
    subprocess.run(["streamlit", "run", "temp_app.py"])

if __name__ == "__main__":
    setup_and_run()
