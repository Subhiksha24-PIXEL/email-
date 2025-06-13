import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools.ddg_search import DuckDuckGoSearchRun

# Hardcoded API key (⚠️ Do not use hardcoding in production!)
GOOGLE_API_KEY = "AIzaSyCHg89y9oxyvXe4vjyUSSTG1ZtlXdqmeLY"

# Initialize LLM with Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

# Add DuckDuckGo search tool
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Useful for answering questions about current events or real-time facts."
    )
]

# Initialize zero-shot agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

# Streamlit UI
st.set_page_config(page_title="Real-Time Q&A 🤖", page_icon="🔍")
st.title("Real-Time Q&A Assistant 🔍🤖")
st.write("Ask me about anything current or factual — I’ll search it for you!")

# User input
user_query = st.text_input("❓ Enter your question")
ask_button = st.button("Ask")

if ask_button:
    if not user_query.strip():
        st.warning("Please enter a question to proceed.")
    else:
        try:
            with st.spinner("Searching and answering..."):
                response = agent.run(user_query)
            st.success("✅ Here's the answer:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Oops! Something went wrong.\n\n{str(e)}")
