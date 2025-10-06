# LangGraph-Agent

![Tests](https://github.com/maryAnnab/LangGraph-Agent/workflows/Tests/badge.svg)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-latest-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-latest-blue.svg)

A production-ready conversational AI agent built with **LangGraph** and **LangChain**, demonstrating stateful workflow orchestration with **Claude 3.5 Sonnet**. Features comprehensive test coverage, CI/CD pipeline, and type-safe implementation with **Pydantic**.

## Features

- ✅ **Stateful Conversations** - Maintains context across multiple interactions using LangGraph's state management
- ✅ **Type-Safe Architecture** - Full Pydantic validation for state and message handling
- ✅ **Comprehensive Testing** - 100% test coverage with pytest and FakeListLLM
- ✅ **CI/CD Pipeline** - Automated testing with GitHub Actions on every push
- ✅ **Modern Tooling** - UV package manager for fast, reliable dependency management
- ✅ **Extensible Design** - Easy to add custom tools and multi-agent workflows

## Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.13 |
| **Framework** | LangGraph, LangChain |
| **LLM Provider** | Anthropic Claude 3.5 Sonnet |
| **Validation** | Pydantic |
| **Testing** | pytest, pytest-asyncio, pytest-cov |
| **Package Manager** | UV |
| **CI/CD** | GitHub Actions |

## Project Structure

LangGraph-Agent/
├── agent.py # Core agent logic with create_graph() and process_message()
├── main.py # Interactive CLI interface (coming soon)
├── simple.py # Single-query example demonstrating basic usage
├── tests/
│ ├── init.py
│ └── test_agent.py # 4 unit tests with FakeListLLM mocking
├── .github/
│ └── workflows/
│ └── tests.yml # CI/CD pipeline configuration
├── .env.example # Environment variables template
├── pyproject.toml # UV-managed dependencies
├── .gitignore
├── LICENSE # MIT License
└── README.md


## Prerequisites

Before running this project, ensure you have:

- **Python 3.13** or higher
- **UV package manager** ([installation guide](https://github.com/astral-sh/uv))
- **Anthropic API key** ([get one here](https://console.anthropic.com/))
- Basic understanding of LangGraph and LangChain concepts

## Installation

### 1. Clone the repository

git clone https://github.com/maryAnnab/LangGraph-Agent.git
cd LangGraph-Agent


### 2. Install UV (if not already installed)

curl -LsSf https://astral.sh/uv/install.sh | sh


### 3. Install dependencies

uv sync


This will create a virtual environment and install all dependencies from `pyproject.toml`.

### 4. Configure environment variables

cp .env.example .env


Edit `.env` and add your Anthropic API key:

ANTHROPIC_API_KEY=your_actual_api_key_here


## Usage

### Run Tests

uv run pytest -v


**Expected output:**
tests/test_agent.py::test_create_graph_structure PASSED [ 25%]
tests/test_agent.py::test_chatbot_basic_structure PASSED [ 50%]
tests/test_agent.py::test_process_message_with_fake_llm PASSED [ 75%]
tests/test_agent.py::test_graph_state_structure PASSED [100%]

============================== 4 passed in 0.71s ==============================


### Run with Coverage

uv run pytest --cov=. --cov-report=html


Open `htmlcov/index.html` to view detailed coverage report.

### Single Query Example

uv run python simple.py


**Example interaction:**
Enter a message: What is LangGraph?

LangGraph is a low-level orchestration framework for building stateful,
long-running AI agents with persistent memory and human-in-the-loop
capabilities. It's part of the LangChain ecosystem and enables complex
multi-agent workflows.


### Interactive Mode (Coming Soon)

uv run python main.py


This will launch a conversational interface with continuous chat capabilities.

## Code Example

Here's how the agent is structured:

from agent import create_graph, process_message

Create the stateful graph
graph = create_graph()

Process a single message
response = process_message("Explain AI agents in simple terms")
print(response)

Or use the graph directly for more control
state = graph.invoke({
"messages": [{"role": "user", "content": "Hello!"}]
})
print(state["messages"][-1].content)


## Testing

The project uses **pytest** with **FakeListLLM** for testing without API calls:

@patch('agent.init_chat_model')
def test_process_message_with_fake_llm(mock_init_chat_model):
"""Test with Fake LLM - no API calls needed"""
fake_llm = FakeListLLM(responses=["This is a test response"])
mock_init_chat_model.return_value = fake_llm

response = process_message("Hello")
assert response == "This is a test response"

**Test coverage includes:**
- Graph structure validation
- State management with Pydantic
- Message processing with mocked LLM
- Type hints and annotations

## CI/CD Pipeline

GitHub Actions automatically runs tests on every push and pull request:

name: Tests
on: [push, pull_request]
jobs:
test:
runs-on: ubuntu-latest
steps:
- Install UV
- Install Python 3.13
- Install dependencies with uv sync
- Run pytest -v


View workflow status: [Actions tab](https://github.com/maryAnnab/LangGraph-Agent/actions)

## Development

### Running in PyCharm on Ubuntu 22.04

1. Open the project in PyCharm
2. PyCharm will auto-detect the `.venv` created by UV
3. Configure interpreter: **Settings** → **Project** → **Python Interpreter** → Select `.venv/bin/python`
4. Run tests using the pytest runner
5. Use the integrated terminal for UV commands

### Adding Custom Tools

Extend the agent by adding tools to `agent.py`:

from langchain.tools import tool

@tool
def custom_search(query: str) -> str:
"""Search the web for information"""
# Your implementation here
return "Search results..."

Add to graph creation
def create_graph(tools=[custom_search]):
# Implementation


## Roadmap

- [ ] Interactive CLI with conversation history
- [ ] Custom tool examples (web search, calculator, etc.)
- [ ] Multi-agent workflows
- [ ] Streaming responses
- [ ] FastAPI REST API wrapper
- [ ] Docker deployment configuration
- [ ] LangSmith integration for observability

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure all tests pass: `uv run pytest -v`
5. Commit with clear messages: `git commit -m 'Add amazing feature'`
6. Push to your fork: `git push origin feature/amazing-feature`
7. Open a Pull Request

Please ensure your code:
- Passes all existing tests
- Includes tests for new features
- Follows PEP 8 style guidelines
- Updates documentation as needed

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## Author

**Anna (maryAnnab)**

- GitHub: [@maryAnnab](https://github.com/maryAnnab)
- Project Link: [LangGraph-Agent](https://github.com/maryAnnab/LangGraph-Agent)

## Acknowledgments

- Built with the [LangChain](https://www.langchain.com/) ecosystem
- Powered by [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/claude)
- Inspired by modern agentic AI architectures and stateful workflows
- Special thanks to the LangGraph community for excellent documentation

---

⭐ **If you find this project useful, please consider giving it a star!**

**Status**: ✅ Production-ready | 🧪 100% test coverage | 🚀 CI/CD enabled
