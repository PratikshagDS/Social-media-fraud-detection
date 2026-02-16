import streamlit as st
import joblib
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Social Media Fraud Detection",
    page_icon="🚨",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
body { background-color: #f5f7fa; }
.main-title { text-align: center; font-size: 45px; font-weight: bold; color: #2ECC71; }
.sub-title { text-align: center; font-size: 18px; color: gray; }
.card { padding: 20px; border-radius: 15px; background-color: white; box-shadow: 0px 0px 15px rgba(0,0,0,0.1); margin-top: 20px; }
div.stButton > button { background-color: #2ECC71; color: white; border-radius: 12px; height: 3em; width: 100%; font-size: 18px; font-weight: bold; }
.result-box { padding: 20px; border-radius: 15px; text-align: center; font-size: 25px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("<div class='main-title'>🚨 Social Media Fraud Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Detect fraudulent social media accounts using Machine Learning</div>", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("⚙ Platform Selection")
platform = st.sidebar.selectbox(
    "Choose Social Media Platform",
    ["Instagram", "Twitter", "Facebook", "LinkedIn"]
)

# ---------------- LOAD MODEL ---------------- #
if platform == "Instagram":
    model = joblib.load("XGB_instagram.pkl")
elif platform == "Twitter":
    model = joblib.load("XGB_twitter.pkl")
elif platform == "Facebook":
    model = joblib.load("RF_facebook.pkl")
else:
    model = joblib.load("RF_linkdin.pkl")

# ---------------- INPUT FORM ---------------- #
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧾 Enter Account Details")

col1, col2 = st.columns(2)
with col1:
    followers_count = st.number_input("👥 Followers", min_value=0)
    following_count = st.number_input("➡ Following", min_value=0)
    posts_count = st.number_input("📝 Posts", min_value=0)
    account_age_days = st.number_input("📅 Account Age (days)", min_value=0)
    has_profile_pic = st.selectbox("🖼 Profile Picture?", [0, 1])

with col2:
    bio_length = st.number_input("📌 Bio Length", min_value=0)
    verified = st.selectbox("✔ Verified?", [0, 1])
    engagement_rate = st.number_input("📊 Engagement Rate (%)", min_value=0.0)
    avg_posts_per_day = st.number_input("📈 Avg Posts Per Day", min_value=0.0)
    follower_following_ratio = st.number_input("⚖ Follower/Following Ratio", min_value=0.0)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PREDICTION BUTTON ---------------- #
if st.button("🔍 Predict Account Type 🚀"):
    # Prepare input dataframe
    input_df = pd.DataFrame([{
        "followers_count": followers_count,
        "following_count": following_count,
        "posts_count": posts_count,
        "account_age_days": account_age_days,
        "has_profile_pic": has_profile_pic,
        "bio_length": bio_length,
        "verified": verified,
        "engagement_rate": engagement_rate,
        "avg_posts_per_day": avg_posts_per_day,
        "follower_following_ratio": follower_following_ratio
    }])
    
    try:
        result = model.predict(input_df)
        prediction = int(result[0])
        
        # Display result
        if prediction == 1:
            st.markdown(
                "<div class='result-box' style='background-color:#ffcccc; color:red;'>🚨 Fraud Account Detected</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box' style='background-color:#ccffcc; color:green;'>✅ Genuine Account</div>",
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error(f"Prediction failed: {e}")