import streamlit as st
from controller.headlinesController import HeadlinesController

st.title("NewsBro Demo")

st.header("Sam Altman & OpenAI News")

controller = HeadlinesController()

headlines = controller.getHeadlines().serialize()
# jsonify(headlines.serialize())
st.json(headlines)


