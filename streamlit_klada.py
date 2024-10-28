import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kladalytics", page_icon=":android:")
# HTML/CSS to set the background GIF and title color
markdown_settings = """
<style>
h1 {
    color: green;  /* Set title color to green */
}
strong {
    color: green;  /* Set bold text color to green */
}
</style>
"""
st.markdown(markdown_settings, unsafe_allow_html=True)

# Display app name
st.title("Kladalytics")

st.write("""
Release Notes – Version 1.0

Welcome to the first release of Kladalytics! 🎉 Your go-to platform for reliable sports betting tips from 
certified tipsters. Here’s what you can expect in this initial version:

**Key Features:**
- **Certified Tipsters in One Place**: Access tips from verified and trusted tipsters across various sports.
- **Diverse Sports Betting Options**: From football and basketball to niche sports, find tips for a wide range of games.
- **Follow Your Favorite Tipsters**: Easily choose and follow tipsters whose insights match your preferences.
- **Personalized Feed**: Get tips and updates directly in your feed from the tipsters you trust.

**Why You’ll Love It:**
- Comprehensive coverage of popular and emerging sports, with expert tips for each.
- User-friendly and sleek design to make finding tips and navigating the app simple.
- Regular updates and tips to keep you informed and ready for each game.

This is just the start! Stay tuned for more features and improvements based on your feedback.
""")

# Path to your APK file
apk_file_path = "./app-release.apk"

# Read the APK file as bytes
with open(apk_file_path, "rb") as file:
    apk_bytes = file.read()

# Download button with an Android icon
st.download_button(
    label="Download APK",
    data=apk_bytes,
    file_name="kladalytics.apk",
    mime="application/vnd.android.package-archive"
)
