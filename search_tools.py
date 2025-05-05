from langchain_community.tools import DuckDuckGoSearchResults 
from langchain.agents import  Tool, load_tools, create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from llm import load_llm

prompt_str = """
    
    Responda sempre em português e siga rigorosamente o formato Thought/Action/Action Input/Observation.  
    Sua função é responder perguntas científicas da forma mais completa e embasada possível.  
    Você deve obrigatoriamente utilizar ferramentas para buscar e apresentar **artigos científicos relevantes** sobre o tema, preferencialmente revisados por pares ou publicados em bases acadêmicas confiáveis.

    Você tem acesso às seguintes ferramentas:

    {tools}

    Use estritamente o seguinte formato:

    Question: a pergunta científica feita pelo usuário  
    Thought: pense cuidadosamente sobre o que deve ser feito para encontrar uma resposta fundamentada  
    Action: a ação a ser tomada, deve ser uma das seguintes [{tool_names}]  
    Action Input: a entrada para a ação, baseada na pergunta  
    Observation: o resultado da ação (por exemplo, lista de artigos ou resumos)  
        ... (esta sequência Thought/Action/Action Input/Observation pode se repetir N vezes)  
    Thought: agora sei a resposta final, com base nos artigos encontrados  
    Final Answer: apresente a resposta completa em português, incluindo **os artigos utilizados**, com título, autores (se disponíveis) e link (se aplicável)

    Início!

    Question: {input}  
    Thought: {agent_scratchpad}
    """

def get_arxiv_tool(query: str): 
    llm = load_llm()
    tool =  load_tools(
        ["arxiv"],
        )
    
    prompt = PromptTemplate(
        input_variables=["input", "tools", "tool_names", "agent_scratchpad"],
        template=prompt_str,

    )
    agent = create_react_agent(llm=llm, tools=tool, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool, verbose=True, handle_parsing_errors=True)
    return agent_executor.invoke({"input": query})


def duck_duck_go_search(query: str):
    search = DuckDuckGoSearchResults()
    return search.invoke(query)

def get_all_tools(): 
    return [
        #Tool(
        #    name="Buscador para a engine arxiv",
        #   func=get_arxiv_tool, 
        #    description="Busca artigos científicos para o buscador arxiv"
        #), 
        Tool(
            name="Buscador para a engine DuckDuckGo",
            func=duck_duck_go_search,
            description="Busca de maneira geral usando o DuckDuckGo"
        ),
        Tool(
            name="Retornar nomes específicos",
            func=retornar_nomes, 
            description="Retorna o nome de filhos de pessoas específicas"
        )
    ]
def retornar_nomes(pessoa): 
   if pessoa == "Tatiane":
       return "Elza"
   return "Eliabe"
   




