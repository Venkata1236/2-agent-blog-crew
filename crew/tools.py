import os
from crewai_tools import TavilySearchTool


def get_api_keys():
    try:
        import streamlit as st
        return (
            st.secrets["OPENAI_API_KEY"],
            st.secrets["TAVILY_API_KEY"]
        )
    except Exception:
        return (
            os.getenv("OPENAI_API_KEY"),
            os.getenv("TAVILY_API_KEY")
        )


def get_search_tool():
    """
    Returns a Tavily search tool for the Researcher agent.
    The agent uses this to search the web for real information.
    """
    _, tavily_key = get_api_keys()
    os.environ["TAVILY_API_KEY"] = tavily_key or ""

    search_tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced"
    )
    return search_tool