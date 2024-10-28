import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kladalytics", page_icon=":android:")

# Display app name
st.title("Kladalytics")

# Display app description
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.")

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
