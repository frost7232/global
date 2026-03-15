import streamlit as st
import requests
from googletrans import Translator

# 1. Setup
API_KEY = "a6ccf081b60046d697f78d9b80333c0a"  
translator = Translator()

st.title("🌐 Global Lens News Bridge")
st.write("See how the world describes the same topic.")

# 2. User Input
query = st.text_input("Enter a topic (e.g., 'Climate Change', 'AI', 'Soccer'):")

# Define which countries/languages you want to 'bridge'
countries = {
    "United States": {"code": "us", "lang": "en"},
    "Argentina": {"code": "ar", "lang": "es"},
    "France": {"code": "fr", "lang": "fr"},
    "India": {"code": "in", "lang": "hi"}
}

if query:
    cols = st.columns(len(countries))
    
    for i, (name, info) in enumerate(countries.items()):
        with cols[i]:
            st.header(name)
            
            # Fetch News from that specific country
            url = f"https://newsapi.org/v2/top-headlines?q={query}&country={info['code']}&apiKey={API_KEY}"
            response = requests.get(url).json()
            articles = response.get("articles", [])

            if articles:
                for art in articles[:3]: # Just the top 3
                    title = art['title']
                    # Translate to English (or your prompt language)
                    translated = translator.translate(title, dest='en').text
                    
                    st.markdown(f"**Original:** {title}")
                    st.success(f"**Translated:** {translated}")
                    st.write("---")
            else:
                st.write("No local news found for this topic.")
