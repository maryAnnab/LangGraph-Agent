from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


class State(TypedDict):
    messages: Annotated[list, add_messages]


def create_graph():
    """Factory function do tworzenia grafu - łatwiejsze testowanie"""
    llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")

    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}

    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder.compile()


def process_message(user_input: str, graph=None):
    """Funkcja testowalna - przyjmuje input jako argument"""
    if graph is None:
        graph = create_graph()

    state = graph.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })
    return state["messages"][-1].content