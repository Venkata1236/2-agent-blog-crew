import os
import sys
from dotenv import load_dotenv
from crew.blog_crew import run_crew

load_dotenv()


def print_separator():
    print("\n" + "=" * 60 + "\n")


def print_welcome():
    print_separator()
    print("🤖  2-AGENT BLOG CREW — CLI MODE")
    print("    Powered by CrewAI + OpenAI + Tavily")
    print_separator()
    print("How it works:")
    print("  1. You provide a blog topic")
    print("  2. Researcher agent searches the web")
    print("  3. Writer agent creates the blog post")
    print_separator()


def check_api_keys():
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY not found in .env")
        sys.exit(1)
    if not os.getenv("TAVILY_API_KEY"):
        print("⚠️  TAVILY_API_KEY not found — research may be limited")
    print("✅ API keys loaded.\n")


def run_cli():
    print_welcome()
    check_api_keys()

    while True:
        print("📝 Enter a blog topic (or 'quit' to exit):\n")
        topic = input("Topic: ").strip()

        if not topic:
            continue

        if topic.lower() == "quit":
            print("\n👋 Goodbye!")
            break

        print(f"\n🚀 Starting crew for topic: '{topic}'\n")
        print_separator()

        try:
            result = run_crew(topic)

            print_separator()
            print("🎉 FINAL BLOG POST:")
            print_separator()
            print(result)
            print_separator()

            # Save option
            save = input("💾 Save to file? (yes/no): ").strip().lower()
            if save == "yes":
                filename = f"{topic.replace(' ', '_').lower()}_blog.md"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(result)
                print(f"✅ Saved to {filename}")

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    run_cli()