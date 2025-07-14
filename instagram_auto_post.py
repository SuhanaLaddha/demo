import os
import time
import threading
import streamlit as st
import schedule
from instagrapi import Client

# ===================== CONFIGURATION =====================
USERNAME = "suhanaladdha"
PASSWORD = "nannu@suhana0606"
SESSION_FILE = "session.json"
TEMP_IMAGE_PATH = "temp.jpg"
# =========================================================

# ---------------- Instagram Login ------------------------
def login_instagram():
    cl = Client()
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
        try:
            cl.login(USERNAME, PASSWORD)
        except Exception:
            st.warning("⚠️ Session expired, retrying login...")
            cl.set_settings({})
            cl.login(USERNAME, PASSWORD)
            cl.dump_settings(SESSION_FILE)
    else:
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(SESSION_FILE)
    return cl

# ---------------- Post Function --------------------------
def post_to_instagram(image_path, caption):
    try:
        client = login_instagram()
        client.photo_upload(image_path, caption)
        return "✅ Post uploaded successfully!"
    except Exception as e:
        return f"❌ Error during posting: {e}"

# ---------------- Scheduler Setup ------------------------
def start_scheduler(post_time, caption):
    def job():
        if os.path.exists(TEMP_IMAGE_PATH):
            post_to_instagram(TEMP_IMAGE_PATH, caption)
        else:
            print("Image not found. Skipping scheduled post.")

    schedule.every().day.at(post_time).do(job)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(60)

    threading.Thread(target=run_scheduler, daemon=True).start()
    return f"⏰ Scheduled daily post at {post_time}"

# ------------------ Streamlit UI -------------------------
st.set_page_config(page_title="📸 Insta Auto Poster", layout="centered")
st.title("📸 Instagram Auto Poster")
st.markdown("Automate Instagram photo uploads using Python + Streamlit!")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
caption = st.text_area("Enter Caption", max_chars=2200)

col1, col2 = st.columns(2)
with col1:
    post_now = st.button("📤 Post Now")
with col2:
    enable_schedule = st.checkbox("🕒 Schedule Post")

if enable_schedule:
    post_time = st.time_input("Choose Daily Time")
else:
    post_time = None

status = st.empty()

# Handle Immediate Post
if post_now:
    if uploaded_file and caption:
        with open(TEMP_IMAGE_PATH, "wb") as f:
            f.write(uploaded_file.read())
        result = post_to_instagram(TEMP_IMAGE_PATH, caption)
        status.success(result if "✅" in result else result)
    else:
        st.warning("⚠️ Please upload an image and enter a caption.")

# Handle Scheduling
if enable_schedule and post_time:
    if uploaded_file and caption:
        with open(TEMP_IMAGE_PATH, "wb") as f:
            f.write(uploaded_file.read())
        scheduled_str = post_time.strftime("%H:%M")
        msg = start_scheduler(scheduled_str, caption)
        st.success(msg)
    elif not uploaded_file:
        st.warning("⚠️ Upload an image to schedule the post.")
    elif not caption:
        st.warning("⚠️ Add a caption to schedule the post.")