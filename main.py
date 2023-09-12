from chat import ChatGPT
# Agent-Selection Function
def agent_selection(user_prompt, chat):
    BASE_TEMPLATE = """
    [USER'S PROMPT]
    {user_prompt}

    [AGENT OPTIONS]
    1.Coding_Agent - used for coding,
    2.Google_Agent - used for googling,
    3.Brainstorm_Agent - used for brainstorming,
    4.Tool_Agent - used to perform actionable tasks

    **IF YOU WOULD LIKE TO SELECT MULTIPLE AGENTS PUT THEM IN THE ORDER OF EXECUTION IN THE LIST BELOW**

    [INSTRUCTIONS]
    Analyze the user's prompt, and to best assist the user select the most appropriate agent.

    [RESPONSE FORMAT]
    [{"Selected Agent": "Coding_Agent", "Reason": "The user's prompt is asking for help with coding."}]

    [RESPONSE]
    """
    response = ChatGPT.chat_with_gpt3("Select the best agent to handle the user's request and explain why. Follow the response format.", BASE_TEMPLATE)
    #parse the response for selected agent
    response_list = eval(response)  # Assuming the response is a string that can be evaluated to a list
    selected_agents = [agent_dict['Selected Agent'] for agent_dict in response_list]
    return selected_agents

# Agent-Execution Function
def agent_execution(user_prompt, agents):
    results = []
    for agent in agents:
        if agent == "Coding_Agent":
            results.append (f"Coding Solution for: {user_prompt}")
        elif agent == "Google_Agent":
            results.append (f"Googling for: {user_prompt}")
        elif agent == "Brainstorm_Agent":
            results.append (f"Brainstorming Ideas for: {user_prompt}")
        elif agent == "Tool_Agent":
            results.append(f"Performing actionable tasks for: {user_prompt}")
        else:
            return "Unknown agent."
    return results

def main():
    chat = ChatGPT()
    input_text = input("Enter your prompt: ")
    agents = agent_selection(input_text, chat)
    print(f"Selected Agents: {agents}")
    response = agent_execution(input_text, agents)
    print(f"Responses: {response}")


if __name__ == "__main__":
    main()