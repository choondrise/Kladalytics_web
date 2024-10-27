import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kladalytics", page_icon=":android:")

# Display app name
st.title("Kladalytics")

# Display app description
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.")

# APK download section
st.markdown(
    """
    <a href="app-release.apk" download="app-release.apk">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Android_robot.svg" alt="Android Icon" style="width: 20px; height: 20px; vertical-align: middle; margin-right: 10px;">
            Download APK
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
