
from langchain_openai.chat_models import ChatOpenAI

def load_llm(): 
    return ChatOpenAI(model="gpt-4o-mini",
                      temperature=0
                      
    )
