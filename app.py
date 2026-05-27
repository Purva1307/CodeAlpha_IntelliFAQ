import streamlit as st
from chatbot import get_response
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IntelliFAQ",
    page_icon="",
    layout="centered"
)

# -------- SESSION --------

if "response" not in st.session_state:
    st.session_state.response = ""


# -------- CUSTOM CSS --------

st.markdown("""
<style>

.stApp{
    background-color:#050A18;
    color:white;
}

.block-container{
    padding-top:3rem;
}

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#36D7FF;
}

.subtitle{
    text-align:center;
    color:#C8C8C8;
    margin-bottom:40px;
}

.stTextInput input{
    border-radius:20px;
    border:1px solid #36D7FF;
    background-color:#1E2235;
    color:white;
}

div.stButton > button{
    background-color:#36D7FF;
    color:black;
    border:none;
    border-radius:15px;
    height:50px;
    width:100%;
    font-weight:bold;
}

div.stButton > button:hover{
    background-color:#67E7FF;
}

.response-box{
    background:#36D7FF;
    color:black;
    padding:18px;
    border-radius:15px;
    margin-top:20px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)


# -------- HEADER --------

st.markdown(
"""
<div class='main-title'>
 IntelliFAQ
</div>

<div class='subtitle'>
AI Powered FAQ Assistant
</div>
""",
unsafe_allow_html=True
)


# -------- INPUT --------

question = st.text_input(
    "",
    placeholder="Ask anything about AI, Python, ML..."
)


# -------- SEND --------

if st.button("Send "):

    if question.strip():
        st.session_state.response = get_response(question)


# -------- RESPONSE --------

if st.session_state.response:

    st.markdown(
        f"""
        <div class='response-box'>
         {st.session_state.response}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Actual working copy button
    components.html(
        f"""
        <html>
        <body style="background-color:#050A18;">

        <button
        onclick="copyText()"
        style="
        background:#36D7FF;
        color:black;
        border:none;
        padding:10px 20px;
        border-radius:10px;
        font-weight:bold;
        cursor:pointer;">
         Copy Response
        </button>

        <script>
        function copyText() {{
            navigator.clipboard.writeText("{st.session_state.response}");
            alert("Response copied!");
        }}
        </script>

        </body>
        </html>
        """,
        height=60
    )