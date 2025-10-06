from agent import create_graph

if __name__ == "__main__":
    graph = create_graph()
    user_input = input("Enter a message: ")
    state = graph.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })
    print(state["messages"][-1].content)