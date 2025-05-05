import streamlit as st 
from backend import query
from langchain_core.messages import HumanMessage, AIMessage

def main(): 
    st.set_page_config(page_title='Research bot - procure nos melhores lugares os melhores artigos científicos', layout='centered')
    chat_app()
    

def load_history():
    mensagens = st.session_state['chat_history']
    for mensagem in mensagens: 

        if isinstance(mensagem,AIMessage):
            with st.chat_message('AI'):
                st.write(mensagem.content)

        elif isinstance(mensagem, HumanMessage):
            with st.chat_message('Human'):
                st.write(mensagem.content) 


def chat_app(): 
    with st.sidebar: 
        st.write("sidebar") 

    st.header("Bem-vindo ao Research Chat", divider=True)
    if "chat_history" in st.session_state: 
        load_history()
    

    nova_mensagem = st.chat_input("Pesquise documentos científicos importantes")
    
    if nova_mensagem: 
        
        st.session_state.chat_history.append(HumanMessage(content=nova_mensagem))
        chat = st.chat_message("human")
        chat.markdown(nova_mensagem)
        chat = st.chat_message("ai")
        chat.markdown("Gerando resposta...")
        reponse = query(nova_mensagem)
        st.session_state.chat_history.append(AIMessage(content=reponse))
        st.rerun()
        
    if not "chat_history" in st.session_state: 
        st.session_state['chat_history'] = []
        st.success("Inicie uma conversa!")


if __name__ == "__main__": 
    main()
