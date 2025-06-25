import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="✍️ Content Rewriter")
st.title("✍️ Book/Blog Content Rewriter")
st.markdown("Rewrite book or blog paragraphs into a different tone or style using OpenAI GPT.")

original_text = st.text_area("Paste the original paragraph", height=200)
tone = st.selectbox("Rewrite Tone/Style", ["Professional", "Casual", "Witty", "Poetic", "Minimalist", "Storytelling"])

def build_prompt(text, tone):
    return f'''
You are a content rewriter.

Your task is to rewrite the following paragraph in a "{tone}" tone or style. Maintain the original meaning, but adapt the language, rhythm, and structure to reflect the new tone.

Original Paragraph:
\"\"\"
{text}
\"\"\"

Rewritten Version:
'''

def rewrite_content(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=400
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"❌ Error: {e}"

if st.button("Rewrite Content"):
    if not original_text.strip():
        st.warning("Please paste the original paragraph.")
    else:
        with st.spinner("Rewriting..."):
            prompt = build_prompt(original_text, tone)
            rewritten = rewrite_content(prompt)
            st.subheader("📝 Rewritten Content")
            st.markdown(rewritten)
