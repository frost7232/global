import streamlit as st
import requests
from deep_translator import GoogleTranslator

# 1. Setup
# Get your FREE key at newsapi.org (No credit card needed)
NEWS_API_KEY = "a6ccf081b60046d697f78d9b80333c0a" 

st.set_page_config(page_title="Global Lens", layout="wide")
st.title("🌐 Global Lens News Bridge")
st.markdown("### Breaking the Western Data Bubble with Real-Time Translation")

# 2. User Input
query = st.text_input("Enter a global topic (e.g., 'Economy', 'Energy', 'Protest'):", "Technology")

# Choose countries that usually have very different cultural views
countries = {
    "India 🇮🇳": "in",
    "Argentina 🇦🇷": "ar",
    "France 🇫🇷": "fr",
    "Japan 🇯🇵": "jp"
}

if query:
    st.write(f"🔍 Fetching local news about **{query}** and translating to English...")
    cols = st.columns(len(countries))
    
    for i, (name, code) in enumerate(countries.items()):
        with cols[i]:
            st.subheader(name)
            
            # Fetch News from that specific country
            url = f"https://newsapi.org/v2/top-headlines?q={query}&country={code}&apiKey={NEWS_API_KEY}"
            try:
                response = requests.get(url).json()
                articles = response.get("articles", [])

                if articles:
                    for art in articles[:3]: # Show top 3
                        title = art['title']
                        
                        # FREE Translation using Google backend
                        translated_title = GoogleTranslator(source='auto', target='en').translate(title)
                        
                        st.write(f"🔗 **{translated_title}**")
                        if title != translated_title:
                            st.caption(f"Original: {title}")
                        st.divider()
                else:
                    st.info("No local headlines found for this topic.")
            except Exception as e:
                st.error("Connection error. Check your NewsAPI key.")

else:
    st.info("Type a topic above to see how the world is reporting it.")
