import streamlit as st
import os
import threading
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
if "error" not in st.session_state:
    st.session_state.error = None
if "progress_step" not in st.session_state:
    st.session_state.progress_step = 0


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
        st.session_state.error = None
        st.session_state.progress_step = 0
        st.rerun()

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.caption(
        "CrewAI 2-agent crew. Researcher uses "
        "Tavily to find real web information. "
        "Writer crafts a full blog post."
    )


# ─────────────────────────────────────────
# MAIN — INPUT SCREEN
# ─────────────────────────────────────────
if not st.session_state.running and not st.session_state.blog_result:

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
        st.session_state.running = True
        st.session_state.progress_step = 1
        st.rerun()


# ─────────────────────────────────────────
# MAIN — RUNNING SCREEN
# ─────────────────────────────────────────
elif st.session_state.running and not st.session_state.blog_result:

    st.title("🤖 Crew is Working...")
    st.markdown(f"**Topic:** {st.session_state.topic}")
    st.markdown("---")

    # Progress steps
    steps = {
        1: ("🔍", "Researcher is searching the web...", "blue"),
        2: ("📝", "Researcher is summarizing findings...", "blue"),
        3: ("✍️", "Writer is crafting your blog post...", "orange"),
        4: ("✅", "Finalizing and polishing...", "green"),
    }

    step = st.session_state.progress_step
    emoji, message, color = steps.get(step, ("⏳", "Processing...", "gray"))

    st.markdown(f"### {emoji} {message}")
    progress_val = step / 4
    st.progress(progress_val)

    st.info(
        "⏳ CrewAI agents take 2-3 minutes to complete.\n\n"
        "🚫 Do NOT refresh or close this page."
    )

    # Run crew in background thread
    if "thread_started" not in st.session_state:
        st.session_state.thread_started = False

    if not st.session_state.thread_started:
        st.session_state.thread_started = True

        def run_in_background():
            try:
                result = run_crew(st.session_state.topic)
                st.session_state.blog_result = result
                st.session_state.running = False
                st.session_state.thread_started = False
            except Exception as e:
                st.session_state.error = str(e)
                st.session_state.running = False
                st.session_state.thread_started = False

        thread = threading.Thread(target=run_in_background)
        thread.daemon = True
        thread.start()

    # Auto advance progress steps every rerun
    import time
    time.sleep(3)

    if st.session_state.blog_result:
        st.rerun()
    elif st.session_state.error:
        st.rerun()
    else:
        # Advance progress step
        if st.session_state.progress_step < 4:
            st.session_state.progress_step += 1
        st.rerun()


# ─────────────────────────────────────────
# MAIN — ERROR SCREEN
# ─────────────────────────────────────────
elif st.session_state.error:

    st.title("❌ Something went wrong")
    st.error(st.session_state.error)

    if st.button("🔄 Try Again", use_container_width=True):
        st.session_state.error = None
        st.session_state.running = False
        st.session_state.thread_started = False
        st.rerun()


# ─────────────────────────────────────────
# MAIN — RESULT SCREEN
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
        reading_time = max(1, word_count // 200)
        st.metric("Reading Time", f"{reading_time} min")

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