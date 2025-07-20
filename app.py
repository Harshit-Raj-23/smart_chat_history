from inverted_index import build_inverted_index, search_query
import streamlit as st
import re

# Load messages
@st.cache_data
def load_messages():
    try:
        with open("chat_data.txt", "r", encoding="utf-8") as chat:
            lines = [message.strip() for message in chat.readlines()]
            return lines if lines else ["(No chat history found)"]
    except FileNotFoundError:
        return ["(chat_data.txt not found)"]

messages = load_messages()
index = build_inverted_index(messages)

st.title("💬 Smart Chat History Search Engine")
st.caption("Search by phrase or keywords (e.g., 'grab coffee' or 'assignment notes')")

query = st.text_input("Enter your search query:")

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a non-empty query.")
    else:
        result_ids, keywords = search_query(query, index, messages)

        if not result_ids:
            st.info("No records found.")
        else:
            st.subheader("🧾 Matching Messages:")
            for i in sorted(result_ids):
                message = messages[i]

                # Highlight matched keywords
                for word in keywords:
                    pattern = re.compile(re.escape(word), re.IGNORECASE)
                    message = pattern.sub(r"<mark>\g<0></mark>", message)

                with st.expander(f"Result {i+1}"):
                    st.markdown(message, unsafe_allow_html=True)
