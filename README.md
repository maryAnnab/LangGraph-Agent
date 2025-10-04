# LangGraph-Agent

An intelligent AI agent built with LangGraph and LangChain for creating stateful, orchestrated workflows with advanced reasoning capabilities.

## About

This project demonstrates the implementation of an agentic AI system using LangGraph, a low-level orchestration framework for building long-running, stateful agents. The agent leverages LangChain components to create sophisticated workflows that can handle complex tasks with persistent memory and human-in-the-loop capabilities.

## Features

- **Stateful Agent Architecture**: Maintains context across multiple interactions
- **Tool Integration**: Extensible framework for adding custom tools and capabilities
- **LangChain Integration**: Leverages the LangChain ecosystem for robust AI functionality
- **Modular Design**: Clean, maintainable code structure for easy customization

## Technologies

- **Python 3.x**: Core programming language
- **LangGraph**: Agent orchestration and workflow management
- **LangChain**: LLM framework and tools
- **python-dotenv**: Environment variable management
- **Anthropic/OpenAI**: LLM providers (configurable)

## Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher installed
- API keys for your chosen LLM provider (Anthropic, OpenAI, etc.)
- Basic understanding of AI agents and LangChain concepts

## Installation

### 1. Clone the repository
git clone https://github.com/maryAnnab/LangGraph-Agent.git
cd LangGraph-Agent


### 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate # On Ubuntu/Linux


### 3. Install dependencies
pip install -U langgraph langchain python-dotenv


### 4. Configure environment variables
Create a `.env` file in the project root:
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env


## Usage

### Running the Agent

python main.py


### Basic Example

from langgraph.prebuilt import create_react_agent

Initialize the agent with tools
agent = create_react_agent(
model="anthropic:claude-3-7-sonnet-latest",
tools=[your_custom_tools],
prompt="You are a helpful AI assistant"
)

Invoke the agent
response = agent.invoke({
"messages": [{"role": "user", "content": "Your query here"}]
})


## Project Structure

LangGraph-Agent/
├── main.py # Main agent implementation
├── tools/ # Custom tools directory
├── requirements.txt # Project dependencies
├── .env # Environment variables (not tracked)
└── README.md # Project documentation


## Development

### Running in PyCharm on Ubuntu 22.04

1. Open the project in PyCharm
2. Configure Python interpreter to use the virtual environment
3. Ensure the environment indicator shows green (active)
4. Run the main script using the Run configuration

### Using Uvicorn (Optional)

For API deployment:
uvicorn app:app --reload --host 0.0.0.0 --port 8000


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss proposed modifications.

## Roadmap

- [ ] Add more specialized tools
- [ ] Implement multi-agent workflows
- [ ] Add comprehensive test coverage
- [ ] Create deployment documentation
- [ ] Add examples for common use cases

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Tutorial](https://github.com/langchain-ai/langgraph)

## Author

**maryAnnab**
- GitHub: [@maryAnnab](https://github.com/maryAnnab)

## Acknowledgments

Built with the LangChain ecosystem and inspired by modern agentic AI architectures.

---

## 🚧 Project Status

**This project is currently under active development.** Features and documentation are being continuously improved and expanded. Check back regularly for updates, or watch this repository to stay informed about new releases.

---

⭐ If you find this project useful, please consider giving it a star!
