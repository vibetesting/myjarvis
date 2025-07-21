from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from vector_store import query_vector_store

# Use a free transformer model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")  # or replace with local model

def get_rag_response(query: str):
    query_embedding = embedding_model.embed_query(query)
    matches = query_vector_store(query_embedding)

    context = "\n".join([m['text'] for m in matches])

    prompt = f"""Use the following references to answer the user's query:
    CONTEXT:
    {context}
    
    USER QUESTION:
    {query}
    """

    return llm.predict(prompt)
