import streamlit as st
import openai

def reading_page():
    st.title("🧠 Reading 🧠")
    st.divider()  # 구분선

    difficult_sentence = st.text_area("", value = "In software engineering, a pipeline consists of a chain of processing elements (processes, threads, coroutines, functions, etc.)", placeholder="전문적인 지식이 많이 포함돼 이해가 가지 않는 문장이 있나요?")
    # 제출
    submitted = st.button("✍️ 더 쉽게 쓴 문장 보러 가기 🚀")

    if submitted:
        rewrite(difficult_sentence)   

def rewrite(difficult_sentence):
    openai.api_key = st.secrets["api_key"]

    # Section 1: Translate the sentence to Korean
    st.subheader("Step 1: Translate the sentence to Korean")

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate following sentence to korean: {difficult_sentence}"}
        ]
    )

    st.write(f"Translated sentence: \n {response.choices[0].message.content}")

    # Section 2: Identify difficult terms and rewrite the sentence
    st.subheader("Step 2: Identify difficult terms and rewrite the sentence")

    prompt = f"""
    You are a helpful and personalized reading assistant.
    Based on the personal information provided below, perform the following tasks:

    1. IDENTIFY any terms in the sentence that might be difficult to understand.
    2. RESEARCH the meanings of these terms in the given context.
    3. REWRITE the sentence using simpler language, based on the definitions you found.

    You can choose various strategies when rewriting sentense. 
    Unless there is something special, please prioritize the personalized strategy.
    To simplify, To explain, To add definition, To metaphor based on personal information, etc.

    Personal Information: {st.session_state["personal_information"]}
    Sentence: {difficult_sentence}

    Answer in following format:

    1. Difficult terms:
    2. Meaning of difficult terms:
    3. Rewritten sentence:
    4. Chosen strategy:
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    st.write(f"Simplified sentence: \n {response.choices[0].message.content}")

    # Section 3: Re-translate the simplified sentence to Korean
    st.subheader("Step 3: Re-translate the simplified sentence to Korean")
    

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate following sentence to korean: {response.choices[0].message.content}"}
        ]
    )

    st.write(f"Re-translated sentence: \n {response.choices[0].message.content}")