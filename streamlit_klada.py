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
/* Hide the Streamlit footer */
footer {
    visibility: hidden;
    height: 0px;  /* Ensure no extra space is left */
}
footer:after {
    content: '';  /* Prevent content from being displayed */
    display: none;
}
</style>
"""
st.markdown(markdown_settings, unsafe_allow_html=True)
st.markdown(markdown_settings, unsafe_allow_html=True)

# Display app name
st.title("Kladalytics")

st.write("""
Release Notes – Version 1.0

Dobrodošli u prvu verziju aplikacije **Kladalytics**! 🎉  
Vaša platforma za pouzdane savjete o sportskom klađenju od certificiranih tipstera.  

### **Ključne značajke:**  
- **Certificirani tipsteri na jednom mjestu:** Pristupite savjetima provjerenih i pouzdanih tipstera za razne sportove.  
- **Raznolike opcije za sportsko klađenje:** Od nogometa i košarke do manje popularnih sportova, pronađite savjete za širok spektar igara.  
- **Pratite svoje omiljene tipstere:** Jednostavno odaberite i pratite tipstere čiji vam savjeti najviše odgovaraju.  
- **Personalizirani feed:** Primajte savjete i ažuriranja izravno u svoj feed od tipstera kojima vjerujete.  

---

### **Upute za instalaciju APK paketa na Android uređaju:**  
1. Preuzmite APK paket klikom na **gumb za preuzimanje**.  
2. Otvorite **Postavke** na vašem uređaju i idite na **Sigurnost**.  
3. Omogućite opciju **Nepoznati izvori** kako biste mogli instalirati aplikacije izvan Google Play trgovine.  
4. Pronađite preuzetu datoteku u mapi **Preuzimanja** na vašem uređaju.  
5. Kliknite na APK datoteku i pratite upute za instalaciju.  
6. Kada se instalacija završi, otvorite aplikaciju i uživajte u **Kladalytics**!  

Ako naiđete na probleme, provjerite jeste li omogućili instalaciju iz nepoznatih izvora ili kontaktirajte podršku.  

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
