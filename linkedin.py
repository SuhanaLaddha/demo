import streamlit as st
import requests

st.set_page_config(page_title="Post to LinkedIn", layout="centered")
st.title("📢 Post to Your LinkedIn Profile")

st.markdown("Use your LinkedIn access token to post directly to your profile via Python + Streamlit.")

# ✅ Fill this in with your actual URN from /v2/me or Post Inspector
member_urn = "urn:li:member:A1234BcD567EfG89"  # 🔁 Replace this if yours is different

# Inputs
access_token = st.text_input("🔑 LinkedIn Access Token", type="password")
post_text = st.text_area("📝 Your LinkedIn Post", height=150)

# On post button click
if st.button("🚀 Post to LinkedIn"):
    if not access_token or not post_text:
        st.warning("Please enter both access token and message.")
    else:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }

        post_data = {
            "author": member_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        response = requests.post(
            "https://api.linkedin.com/v2/ugcPosts",
            headers=headers,
            json=post_data
        )

        if response.status_code == 201:
            st.success("✅ Your post was successfully published!")
        else:
            st.error(f"❌ Failed! Status code: {response.status_code}")
            st.json(response.json())