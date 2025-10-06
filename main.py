from agent import create_graph

if __name__ == "__main__":
    graph = create_graph()

    print("LangGraph Agent - Chat Interface")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            break

        state = graph.invoke({
            "messages": [{"role": "user", "content": user_input}]
        })

        print(f"Agent: {state['messages'][-1].content}\n")