import streamlit as st
from rag_core import build_retriever, ask, FALLBACK

st.set_page_config(page_title="Python Foundations KB", page_icon="🐍")
st.title("🐍 Python Foundations Knowledge Bot")
st.caption("A document-grounded guide to Python basics. Answers use the selected knowledge base and show their sources.")
with st.sidebar:
    st.header("Your session")
    api_key = st.text_input("Gemini API key", type="password", help="Used in this session only; never written to disk.")
    uploads = st.file_uploader("Use your own documents (optional)", type=["pdf", "txt", "md"], accept_multiple_files=True)
    st.caption("With no uploads, the bot searches the sample Python guides in the repository.")
    st.markdown("**Suggested questions**")
    suggestions = ["What is a Python variable?", "How does a for loop work?", "What is the difference between a list and a dictionary?", "When should I use a function?"]
    if "question" not in st.session_state:
        st.session_state.question = ""
    for i, suggestion in enumerate(suggestions):
        if st.button(suggestion, key=f"suggest_{i}", use_container_width=True):
            st.session_state.question = suggestion

if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("Sources"):
                for source in msg["sources"]:
                    st.markdown(f"**[{source['id']}] {source['source']}**, page {source['page']}  \n{source['excerpt']}")

question = st.chat_input("Ask a question about Python fundamentals")
if not question and st.session_state.question:
    question = st.session_state.question
    st.session_state.question = ""
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        if not api_key:
            answer, sources = "Add your Gemini API key in the sidebar to ask a question.", []
        else:
            try:
                with st.spinner("Reading the knowledge base…"):
                    retriever = build_retriever(api_key, uploads)
                    answer, sources = ask(retriever, api_key, question)
            except Exception as exc:
                answer, sources = f"I couldn't process that request: {exc}", []
        st.markdown(answer)
        if sources:
            with st.expander("Sources"):
                for source in sources:
                    st.markdown(f"**[{source['id']}] {source['source']}**, page {source['page']}  \n{source['excerpt']}")
    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
