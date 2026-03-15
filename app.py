import streamlit as st
import requests
from openai import OpenAI

# 1. Setup (Use your OpenAI Key here)
client = OpenAI(api_key="a6ccf081b60046d697f78d9b80333c0a")
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

st.title("🌐 Global Lens News Bridge")

query = st.text_input("Enter a topic:", "Climate Change")

countries = {
    "Argentina": "ar",
    "France": "fr",
    "India": "in",
    "Japan": "jp"
}

if query:
    cols = st.columns(len(countries))
    for i, (name, code) in enumerate(countries.items()):
        with cols[i]:
            st.header(name)
            url = f"https://newsapi.org/v2/top-headlines?q={query}&country={code}&apiKey={NEWS_API_KEY}"
            data = requests.get(url).json()
            
            for article in data.get("articles", [])[:2]:
                title = article['title']
                
                # Use AI to translate and explain the cultural context
                translation = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": f"Translate this headline to English and tell me in 1 sentence why this perspective might be different from Western news: {title}"}]
                )
                
                st.write(f"**Original:** {title}")
                st.info(translation.choices[0].message.content)
                st.write("---")
