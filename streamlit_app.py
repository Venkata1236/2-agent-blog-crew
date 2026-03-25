import streamlit as st
import os
from dotenv import load_dotenv
from crew.blog_crew import run_crew

load_dotenv()


# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="2-Agent Blog Crew",
    page_icon="🤖",
    layout="centered"
)


# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
if "blog_result" not in st.session_state:
    st.session_state.blog_result = None
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "running" not in st.session_state:
    st.session_state.running = False


# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.title("🤖 2-Agent Blog Crew")
    st.markdown("---")

    st.markdown("### 👥 The Crew")
    st.markdown("🔍 **Researcher Agent**")
    st.caption("Searches web, gathers facts and insights")
    st.markdown("✍️ **Writer Agent**")
    st.caption("Turns research into a polished blog post")

    st.markdown("---")

    st.markdown("### ⚙️ Process")
    st.markdown("Sequential — Researcher → Writer")

    st.markdown("---")

    if st.button("🔄 New Blog", use_container_width=True):
        st.session_state.blog_result = None
        st.session_state.topic = ""
        st.session_state.running = False
        st.rerun()

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.caption(
        "CrewAI 2-agent crew. Researcher uses "
        "Tavily to search the web. Writer uses "
        "research to generate a blog post."
    )


# ─────────────────────────────────────────
# MAIN — INPUT
# ─────────────────────────────────────────
if not st.session_state.blog_result:

    st.title("🤖 2-Agent Blog Crew")
    st.markdown(
        "Two AI agents working together — "
        "**Researcher** finds the facts, "
        "**Writer** creates the blog."
    )
    st.markdown("---")

    st.subheader("📝 What should the blog be about?")

    topic = st.text_input(
        "Blog Topic",
        placeholder="e.g. The Future of AI Agents in 2025"
    )

    # Example topics
    st.markdown("**💡 Try these:**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("The Rise of AI Agents", use_container_width=True):
            st.session_state.topic = "The Rise of AI Agents in 2025"
            st.rerun()
        if st.button("LangGraph vs CrewAI", use_container_width=True):
            st.session_state.topic = "LangGraph vs CrewAI — Which Should You Use?"
            st.rerun()
    with col2:
        if st.button("Future of Remote Work", use_container_width=True):
            st.session_state.topic = "The Future of Remote Work"
            st.rerun()
        if st.button("Python for AI Engineers", use_container_width=True):
            st.session_state.topic = "Why Python is the Best Language for AI Engineers"
            st.rerun()

    # Use starter topic if set
    final_topic = st.session_state.topic or topic

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        start = st.button(
            "🚀 Start Crew",
            use_container_width=True,
            disabled=not final_topic.strip()
        )

    if start and final_topic.strip():
        st.session_state.topic = final_topic.strip()
        st.session_state.running = True

        with st.spinner("🔍 Researcher is gathering information..."):
            st.info(
                "⏳ This takes 30-60 seconds. "
                "Researcher is searching the web, "
                "Writer is crafting your blog..."
            )
            try:
                result = run_crew(final_topic.strip())
                st.session_state.blog_result = result
                st.session_state.running = False
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.running = False


# ─────────────────────────────────────────
# MAIN — RESULT
# ─────────────────────────────────────────
else:

    st.title("🎉 Blog Post Ready!")
    st.markdown(f"**Topic:** {st.session_state.topic}")
    st.markdown("---")

    st.balloons()

    # Word count
    word_count = len(st.session_state.blog_result.split())
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Word Count", f"~{word_count}")
    with col2:
        reading_time = max(1, word_count // 200)
        st.metric("Reading Time", f"{reading_time} min")

    st.markdown("---")

    # Blog content
    st.markdown(st.session_state.blog_result)

    st.markdown("---")

    # Download
    st.download_button(
        label="⬇️ Download as Markdown",
        data=st.session_state.blog_result,
        file_name=f"{st.session_state.topic.replace(' ', '_').lower()}_blog.md",
        mime="text/markdown",
        use_container_width=True
    )