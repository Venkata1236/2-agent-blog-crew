import os
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crew.tools import get_search_tool
from dotenv import load_dotenv

load_dotenv()


def get_api_key():
    try:
        import streamlit as st
        return st.secrets["OPENAI_API_KEY"]
    except Exception:
        return os.getenv("OPENAI_API_KEY")


@CrewBase
class BlogCrew:
    """
    2-Agent Blog Writing Crew.
    Researcher gathers info → Writer creates blog post.
    """
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        os.environ["OPENAI_API_KEY"] = get_api_key() or ""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[get_search_tool()],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            verbose=True,
            allow_delegation=False
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher()
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_task"],
            agent=self.writer(),
            context=[self.research_task()]  # writer gets researcher output
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.writer()],
            tasks=[self.research_task(), self.write_task()],
            process=Process.sequential,
            verbose=True
        )


def run_crew(topic: str) -> str:
    """
    Runs the blog crew for a given topic.
    Returns the final blog post as a string.
    """
    blog_crew = BlogCrew()
    result = blog_crew.crew().kickoff(inputs={"topic": topic})
    return str(result)