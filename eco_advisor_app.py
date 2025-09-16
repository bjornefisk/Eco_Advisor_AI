import streamlit as st

from eco_advisor.retrieval import get_relevant_context, bootstrap_index
from eco_advisor.llm import generate_answer


st.set_page_config(page_title="Eco Advisor AI", layout="wide")
st.title("🌱 Eco Advisor AI")

st.write("""
Ask any question about ecology, sustainability or green technology—  
I'll find the most relevant snippet from your documents and answer as an expert.
""")

with st.spinner("Preparing index…"):
    bootstrap_index()

user_q = st.text_area("Your question:", height=150)

if st.button("Ask Eco Advisor"):
    if not user_q.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving relevant context…"):
            ctx = get_relevant_context(user_q)
        if ctx:
            st.subheader("🔍 Retrieved Context")
            st.write(ctx)

            with st.spinner("Generating answer…"):
                reply = generate_answer(ctx, user_q)
            st.subheader("💡 Eco Advisor’s Answer")
            st.write(reply or "No answer generated.")
        else:
            st.error("No relevant context found.")


