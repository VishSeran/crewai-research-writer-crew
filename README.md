# CrewAI 101: Building Multi-Agent AI Systems

Build a multi-agent AI system with CrewAI — a Research Analyst agent that gathers real-time information via web search, and a Content Strategist agent that turns it into polished, reader-friendly content.

## Overview

This project demonstrates a **sequential multi-agent workflow**:

- **Research Analyst agent** — gathers up-to-date information on a topic using a real-time web search tool (SerperDev).
- **Content Strategist agent** — takes the research findings and rewrites them into clear, engaging content for a tech-savvy audience.

Together, these agents show how autonomous AI agents can collaborate to complete complex tasks that neither could do as well alone.

## What You'll Learn

- How to use **CrewAI** to automate multi-agent workflows for intelligent content generation
- The **key components of CrewAI** — agents, tasks, tools, and processes — and how they work together
- How to implement **real-world AI collaboration scenarios**, such as turning technical research into reader-friendly content
- Foundational skills to **extend and scale CrewAI workflows** across other use cases

## Requirements

This project uses the following Python libraries:

- [`crewai`](https://pypi.org/project/crewai/) — core framework for building collaborative AI workflows using agents, tasks, and processes
- [`crewai-tools`](https://pypi.org/project/crewai-tools/) — prebuilt tools (web search, file I/O, APIs) that agents can use
- [`langchain`](https://www.langchain.com/) — core utilities for working with LLMs and prompts
- [`langchain-community`](https://pypi.org/project/langchain-community/) — community-maintained LangChain integrations

Install them with:

```bash
pip install langchain==0.3.20 crewai==0.80.0 langchain-community==0.3.19 crewai-tools==0.38.0
```

## Getting Started

1. **Download or clone this repo.**

2. **Install the dependencies** listed above.

3. **Get a Serper API key** — this powers the real-time web search tool used by the Research Analyst agent. Sign up at [serper.dev](https://serper.dev/) and set it as an environment variable:

   ```bash
   export SERPER_API_KEY="your-api-key-here"
   ```

4. **Configure your LLM** — the code uses CrewAI's `LLM` class, which supports a wide range of providers (OpenAI, Anthropic, local models via Ollama, and others). Update the `model` and any required credentials to match the provider you want to use.

5. **Run it** — walk through defining agents, creating tasks, assembling a crew, and running the pipeline end to end.

## How It Works

1. **Define agents** — each with a role, goal, backstory, and set of tools (e.g., a "Senior Research Analyst" with web search access, a "Tech Content Strategist" for writing).
2. **Create tasks** — each task specifies a description, the expected output, and which agent is responsible.
3. **Assemble a Crew** — combine agents and tasks into a `Crew`, choosing a process (sequential or hierarchical) that determines how tasks are executed.
4. **Run the crew** — pass in inputs (like a topic) and let the agents collaborate to produce the final output.

## License

Add a license of your choice (e.g., MIT) here.
