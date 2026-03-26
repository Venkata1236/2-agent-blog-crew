import streamlit as st
import os
from dotenv import load_dotenv
from crew.blog_crew import run_crew

load_dotenv()

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

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.title("🤖 2-Agent Blog Crew")
    st.markdown("---")
    st.markdown("### 👥 The Crew")
    st.markdown("🔍 **Researcher Agent**")
    st.caption("Searches web, gathers facts")
    st.markdown("✍️ **Writer Agent**")
    st.caption("Turns research into blog post")
    st.markdown("---")
    st.markdown("### ⚙️ Process")
    st.markdown("Sequential — Researcher → Writer")
    st.markdown("---")
    if st.button("🔄 New Blog", use_container_width=True):
        st.session_state.blog_result = None
        st.session_state.topic = ""
        st.rerun()
    st.markdown("---")
    st.caption("CrewAI 2-agent crew using Tavily search + GPT-4o-mini.")


# ─────────────────────────────────────────
# MAIN — INPUT
# ─────────────────────────────────────────
if not st.session_state.blog_result:

    st.title("🤖 2-Agent Blog Crew")
    st.markdown(
        "**Researcher** finds the facts → "
        "**Writer** creates the blog."
    )
    st.markdown("---")

    st.subheader("📝 What should the blog be about?")

    topic = st.text_input(
        "Blog Topic",
        placeholder="e.g. The Future of AI Agents in 2025"
    )

    st.markdown("**💡 Try these:**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("The Rise of AI Agents", use_container_width=True):
            st.session_state.topic = "The Rise of AI Agents in 2025"
            st.rerun()
        if st.button("LangGraph vs CrewAI", use_container_width=True):
            st.session_state.topic = "LangGraph vs CrewAI"
            st.rerun()
    with col2:
        if st.button("Future of Remote Work", use_container_width=True):
            st.session_state.topic = "The Future of Remote Work"
            st.rerun()
        if st.button("Python for AI Engineers", use_container_width=True):
            st.session_state.topic = "Python for AI Engineers"
            st.rerun()

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

        st.markdown("---")
        st.markdown("### 🤖 Crew is Working...")
        st.warning(
            "⏳ Please wait 2-3 minutes.\n\n"
            "🔍 Researcher is searching the web...\n\n"
            "✍️ Writer is crafting your blog...\n\n"
            "🚫 Do NOT refresh this page."
        )

        with st.spinner("Running crew — this takes 2-3 minutes..."):
            try:
                result = run_crew(final_topic.strip())
                st.session_state.blog_result = result
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")


# ─────────────────────────────────────────
# MAIN — RESULT
# ─────────────────────────────────────────
else:
    st.title("🎉 Blog Post Ready!")
    st.markdown(f"**Topic:** {st.session_state.topic}")
    st.markdown("---")

    st.balloons()

    word_count = len(st.session_state.blog_result.split()) if st.session_state.blog_result else 0
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Word Count", f"~{word_count}")
    with col2:
        st.metric("Reading Time", f"{max(1, word_count // 200)} min")

    st.markdown("---")
    st.markdown(st.session_state.blog_result)
    st.markdown("---")

    st.download_button(
        label="⬇️ Download as Markdown",
        data=st.session_state.blog_result,
        file_name=f"{st.session_state.topic.replace(' ', '_').lower()}_blog.md",
        mime="text/markdown",
        use_container_width=True
    )