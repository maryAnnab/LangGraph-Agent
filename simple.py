from langgraph_agent.agent import create_graph, process_message

if __name__ == "__main__":
    graph = create_graph()
    user_input = input("Enter a message: ")
    state = graph.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })
    print(state["messages"][-1].content)