import streamlit as st
import requests
from googletrans import Translator

# 1. Setup
NEWS_API_KEY = "a6ccf081b60046d697f78d9b80333c0a" # Get this free at newsapi.org
translator = Translator()

st.set_page_config(page_title="Global News Bridge", layout="wide")
st.title("🌐 Global Lens News Bridge")
st.markdown("### Seeing the world beyond the Western data bubble.")

query = st.text_input("Enter a topic (e.g., 'Economy', 'Protest', 'Technology'):")

# We use countries that usually have very different perspectives
countries = {
    "Argentina 🇦🇷": "ar",
    "India 🇮🇳": "in",
    "France 🇫🇷": "fr",
    "Japan 🇯🇵": "jp"
}

if query:
    st.write(f"🔍 Fetching global perspectives for **{query}**...")
    cols = st.columns(len(countries))
    
    for i, (name, code) in enumerate(countries.items()):
        with cols[i]:
            st.subheader(name)
            # Fetch News
            url = f"https://newsapi.org/v2/top-headlines?q={query}&country={code}&apiKey={NEWS_API_KEY}"
            try:
                response = requests.get(url).json()
                articles = response.get("articles", [])

                if articles:
                    for art in articles[:3]:
                        title = art['title']
                        # FREE Translation
                        try:
                            translated = translator.translate(title, dest='en').text
                            st.write(f"🔗 **{translated}**")
                            st.caption(f"Original: {title}")
                        except:
                            st.write(f"🔗 {title}") # Fallback if translation fails
                        st.divider()
                else:
                    st.info("No local news found.")
            except:
                st.error("API Error")

# If nothing is typed yet
else:
    st.info("Type a topic above and press Enter to see how different countries are reporting it!")
