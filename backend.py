from search_tools import get_all_tools
from langchain.agents import initialize_agent, Tool, AgentType
from llm import load_llm


def query(input: str): 
    return run_agent(input)


def run_agent(query): 
    llm = load_llm()
    agent_executor = initialize_agent(tools=get_all_tools(), llm=llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent_executor.run(query)
    