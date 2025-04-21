import os
from med_chatbot.vector_store import get_or_create_vector_store, get_vector_store
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


def init_chatbot(vectorstore):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="deepseek-r1-distill-llama-70b", streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()]
    )
    retriever = vectorstore.as_retriever()

    system_message = """You are Garry, an AI assistant specialized in medical reasoning.
    When answering questions, first show your step-by-step reasoning process,
    then provide your final conclusion. I WANT YOU TO FOLLOW streaming approach And EVERYTIME GIVE YOUR URL REFERENCES AT THE END OF THE ANSWER.

    CORE RULES:
    1. REJECT ALL NON-MEDICAL QUERIES immediately with: "I only answer medical questions. Please ask about health, symptoms, treatments, or medical conditions."
    2. DO NOT engage in general conversation or pleasantries
    3. DO DRAW LINES WHICH SEPERATE THE thinking/reasoning part from the Original Answer part
    4. ONLY provide medical information in this format:

    ### Medical Response Format:
    1. Topic Verification:
    * Medical Category: [diagnosis/treatment/prevention]
    * Medical Field: [relevant specialty]
    * Urgency Level: [routine/urgent/emergency]

    2. Clinical Information:
    * Medical Definition: [term + simple explanation]
    * Key Medical Facts: [bullet-point list]
    * Scientific Background: [brief medical context]

    3. Medical Guidance:
    * Standard Protocol: [medical guidelines]
    * Warning Signs: [when to seek care]
    * Professional Advice: [medical recommendations]

    RESPONSE VALIDATION:
    - Must contain medical terminology
    - Must include medical evidence basis
    - Must have healthcare disclaimer
    - Must stay within medical scope

    AUTOMATIC REJECTION:
    - Small talk/greetings
    - Non-medical topics
    - Personal opinions
    - General advice

    MANDATORY DISCLAIMER:
    > Medical Notice: This is general medical information only.
    > Consult healthcare professionals for personal medical advice.
    > Emergency conditions require immediate medical attention."""

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),  # The user's latest input
        ]
    )

    # Create a history-aware retriever that will use LLM to contextualize queries
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # System prompt for answering the user's question based on retrieved documents
    qa_system_prompt = (
        "You are a knowledgeable and concise medical assistant. "
        "Use the provided medical context to answer the health-related question accurately. "
        "If you are unsure or do not know the answer, say that you don't know. "
        "Provide a concise, evidence-based response in no more than three sentences, "
        "and avoid offering medical advice without sufficient context."
        "\n\n"
        "{context}"
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),  # Optional chat history
            ("human", "{input}"),  # User's query
        ]
    )

    # Combine documents and generate an answer using the LLM
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(
        history_aware_retriever, question_answer_chain)
    return rag_chain


def chat(rag_chain):
    chat_history = []
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            break
        result = rag_chain.invoke(
            {"input": query, "chat_history": chat_history})
        # print(f"AI: {result['answer']}")
        # Update the chat history
        chat_history.append(HumanMessage(content=query))
        chat_history.append(AIMessage(content=result["answer"]))


class Chat:
    chat_history = []

    def __init__(self, rag_chain):
        self.rag_chain = rag_chain

    def send(self, msg):
        result = self.rag_chain.invoke(
            {"input": msg, "chat_history": self.chat_history})
        print(f"AI: {result['answer']}")
        self.chat_history.append(HumanMessage(content=msg))
        self.chat_history.append(AIMessage(content=result["answer"]))
        ans = result["answer"]
        ans = ans.replace(".", ".\n\n")
        ans = ans.replace("?", "?\n\n")
        return result['answer']


class ChatBot:
    chats: dict[str, Chat] = {}

    def __init__(self):
        pdf_path = os.getenv("PDF_PATH")
        if not pdf_path:
            raise ValueError("Please set the PDF_PATH environment variable.")
        self.vectorstore = get_or_create_vector_store(pdf_path)
        self.rag_chain = init_chatbot(self.vectorstore)

    def create_chat(self, id):
        self.chats[id] = Chat(self.rag_chain)

    def send(self, id, msg):
        return self.chats[id].send(msg)

    def remove_chat(self, id):
        del self.chats[id]
