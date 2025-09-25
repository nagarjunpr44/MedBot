# main.py
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["PINECONE_API_KEY"] = os.environ.get("PINECONE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

def init_rag_chain():
    embeddings = download_hugging_face_embeddings()
    index_name = "medicalchatbot"

    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    chatModel = ChatOpenAI(model="gpt-4o")
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain

# Initialize once
rag_chain = init_rag_chain()

def ask_question(question: str) -> str:
    response = rag_chain.invoke({"input": question})
    return response["answer"]
